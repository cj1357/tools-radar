# -*- coding: utf-8 -*-
import urllib.request, ssl, re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def inspect(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=10, context=ctx) as r:
        html = r.read().decode('utf-8', errors='ignore')
        title = re.search(r'<title>(.*?)</title>', html, re.I)
        desc = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', html, re.I)
        print('URL:', url)
        print('Title:', title.group(1) if title else 'None')
        print('Desc:', desc.group(1) if desc else 'None')
        headers = re.findall(r'<h[1-3][^>]*>(.*?)</h[1-3]>', html, re.I)
        print('Headers:', [re.sub(r'<[^>]+>', '', h).strip() for h in headers[:8]])

inspect('https://cloudbrowser.tv')
print('='*50)
inspect('https://tryreelai.com/')
