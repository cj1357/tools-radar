const { spawn } = require('child_process');
const http = require('http');
const fs = require('fs');
const path = require('path');

const chromePath = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';

function startServer(port = 4321) {
  const server = http.createServer((req, res) => {
    let reqPath = req.url.split('?')[0];
    let p = path.join(__dirname, '..', 'site', 'dist', reqPath === '/' ? 'index.html' : reqPath);
    if (!path.extname(p)) {
      if (fs.existsSync(path.join(p, 'index.html'))) {
        p = path.join(p, 'index.html');
      }
    }
    if (fs.existsSync(p) && fs.statSync(p).isFile()) {
      const ext = path.extname(p);
      const ctMap = {
        '.html': 'text/html; charset=utf-8',
        '.css': 'text/css',
        '.js': 'text/javascript',
        '.svg': 'image/svg+xml',
        '.png': 'image/png',
        '.json': 'application/json'
      };
      res.writeHead(200, { 'Content-Type': ctMap[ext] || 'application/octet-stream' });
      res.end(fs.readFileSync(p));
    } else {
      res.writeHead(404);
      res.end('Not found: ' + reqPath);
    }
  });

  return new Promise((resolve) => {
    server.listen(port, () => {
      resolve(server);
    });
  });
}

async function runDiagnosis() {
  const server = await startServer(4321);
  console.log('Static server started on port 4321');

  const chrome = spawn(chromePath, [
    '--headless=new',
    '--remote-debugging-port=9222',
    '--window-size=375,667',
    '--disable-gpu',
    '--no-sandbox',
    'about:blank'
  ]);

  await new Promise(r => setTimeout(r, 1200));

  const routes = [
    '/tool/fastrelease',
    '/',
    '/vs/postiz-vs-buffer',
    '/best/open-source-developer-tools',
    '/guides/developer-guide-autonomous-ai-coding-agents',
    '/submit',
    '/methodology'
  ];

  try {
    const targets = await new Promise((resolve, reject) => {
      http.get('http://127.0.0.1:9222/json', (res) => {
        let data = '';
        res.on('data', chunk => data += chunk);
        res.on('end', () => resolve(JSON.parse(data)));
      }).on('error', reject);
    });

    const pageTarget = targets.find(t => t.type === 'page');
    if (!pageTarget) {
      throw new Error('No page target found');
    }
    const wsUrl = pageTarget.webSocketDebuggerUrl;
    console.log(`Connecting to page target: ${pageTarget.id} (${pageTarget.title})`);
    const ws = new WebSocket(wsUrl);

    let msgId = 1;
    function sendCommand(method, params = {}) {
      return new Promise((resolve, reject) => {
        const id = msgId++;
        const handler = (evt) => {
          const resp = JSON.parse(evt.data);
          if (resp.id === id) {
            ws.removeEventListener('message', handler);
            if (resp.error) {
              console.error(`CDP error on ${method}:`, resp.error);
              reject(resp.error);
            } else {
              resolve(resp.result);
            }
          }
        };
        ws.addEventListener('message', handler);
        ws.send(JSON.stringify({ id, method, params }));
      });
    }

    await new Promise(r => { ws.onopen = r; });

    // Enable required domains
    await sendCommand('Page.enable');
    await sendCommand('DOM.enable');

    // Emulate iPhone SE (375x667, dpr=2, mobile=true)
    await sendCommand('Emulation.setDeviceMetricsOverride', {
      width: 375,
      height: 667,
      deviceScaleFactor: 2,
      mobile: true,
      screenOrientation: { angle: 0, type: 'portraitPrimary' }
    });
    await sendCommand('Network.setUserAgentOverride', {
      userAgent: 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Mobile/15E148 Safari/604.1'
    });

    console.log('\n======================================================');
    console.log('DIAGNOSING MOBILE VIEWPORT OVERFLOW AT 375px (iPhone SE)');
    console.log('======================================================\n');

    for (const route of routes) {
      const url = `http://127.0.0.1:4321${route}`;
      await sendCommand('Page.navigate', { url });
      // wait for load
      await new Promise(r => setTimeout(r, 1000));

      const evalResult = await sendCommand('Runtime.evaluate', {
        expression: `(() => {
          const winW = window.innerWidth;
          const scrollW = document.documentElement.scrollWidth;
          const clientW = document.documentElement.clientWidth;
          const bodyScrollW = document.body.scrollWidth;
          const bodyClientW = document.body.clientWidth;

          const overflowing = [];
          document.querySelectorAll('*').forEach(el => {
            const rect = el.getBoundingClientRect();
            // Check elements extending past right viewport
            if (rect.right > winW + 1) {
              overflowing.push({
                tag: el.tagName.toLowerCase(),
                id: el.id,
                className: (typeof el.className === 'string' ? el.className : '').slice(0, 50),
                rectWidth: Math.round(rect.width),
                rectRight: Math.round(rect.right),
                scrollWidth: el.scrollWidth,
                clientWidth: el.clientWidth,
                snippet: (el.innerText || el.textContent || '').slice(0, 60).replace(/\\s+/g, ' ')
              });
            }
          });

          return {
            winW,
            scrollW,
            clientW,
            bodyScrollW,
            bodyClientW,
            hasOverflow: scrollW > winW + 1,
            overflowCount: overflowing.length,
            overflowing: overflowing.slice(0, 10)
          };
        })()`,
        returnByValue: true
      });

      const res = evalResult.result.value;
      const statusIcon = res.hasOverflow ? '❌ OVERFLOW' : '✅ CLEAN';
      console.log(`[${statusIcon}] Route: ${route}`);
      console.log(`  Window: ${res.winW}px | DocScroll: ${res.scrollW}px | BodyScroll: ${res.bodyScrollW}px`);
      if (res.hasOverflow) {
        console.log(`  ⚠️ Overflow delta: +${res.scrollW - res.winW}px`);
        console.log(`  Top overflowing elements (${res.overflowCount} total):`);
        res.overflowing.forEach((item, i) => {
          console.log(`    #${i+1} <${item.tag}${item.id ? ' id="'+item.id+'"' : ''}${item.className ? ' class="'+item.className+'"' : ''}>`);
          console.log(`       width: ${item.rectWidth}px, right: ${item.rectRight}px, scrollW: ${item.scrollWidth}px`);
          console.log(`       text: "${item.snippet}"`);
        });
      }
      console.log('------------------------------------------------------');
    }

    ws.close();
  } catch (err) {
    console.error('Diagnosis failed:', err);
  } finally {
    chrome.kill();
    server.close();
  }
}

runDiagnosis();
