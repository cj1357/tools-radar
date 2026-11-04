# -*- coding: utf-8 -*-
"""
Generate a pixel-perfect 1200x630 OpenGraph & Twitter Card default image for ToolsRadar
using the exact official favicon.svg vector logo, gradient typography, and Edge headless renderer.
"""

import os
import subprocess
import tempfile
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@500;600;700&family=Plus+Jakarta+Sans:wght@500;600;700;800;900&display=swap');

  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }

  body {
    width: 1200px;
    height: 630px;
    background: #08080b;
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    color: #f4f4f5;
    position: relative;
    overflow: hidden;
  }

  /* Cyber Grid Background */
  .grid-bg {
    position: absolute;
    inset: 0;
    background-image: 
      radial-gradient(circle at 1px 1px, rgba(255, 255, 255, 0.08) 1px, transparent 0);
    background-size: 36px 36px;
    z-index: 1;
  }

  /* Radial Ambient Glows */
  .glow-cyan {
    position: absolute;
    right: -100px;
    top: 50%;
    transform: translateY(-50%);
    width: 750px;
    height: 750px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(56, 189, 248, 0.18) 0%, rgba(129, 140, 248, 0.08) 40%, transparent 70%);
    z-index: 2;
  }

  .glow-purple {
    position: absolute;
    left: -120px;
    top: -100px;
    width: 600px;
    height: 600px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(168, 85, 247, 0.12) 0%, transparent 65%);
    z-index: 2;
  }

  /* Radar HUD Container (Right Side) */
  .radar-hud {
    position: absolute;
    right: 80px;
    top: 50%;
    transform: translateY(-50%);
    width: 480px;
    height: 480px;
    z-index: 3;
  }

  /* Left Hero Content */
  .hero-content {
    position: absolute;
    left: 80px;
    top: 60px;
    bottom: 60px;
    width: 620px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    z-index: 10;
  }

  /* Live Telemetry Badge */
  .status-badge {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    background: rgba(18, 18, 23, 0.85);
    border: 1px solid rgba(56, 189, 248, 0.3);
    border-radius: 9999px;
    padding: 7px 18px;
    width: fit-content;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.4);
  }

  .live-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: #10b981;
    box-shadow: 0 0 10px #10b981, 0 0 20px #10b981;
  }

  .status-text {
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 0.06em;
    color: #e4e4e7;
    font-family: 'JetBrains Mono', monospace;
  }

  /* Brand Row with Exact SVG Icon */
  .brand-row {
    display: flex;
    align-items: center;
    gap: 18px;
    margin-top: 14px;
    margin-bottom: 6px;
  }

  .nav-brand-text {
    font-size: 50px;
    font-weight: 900;
    letter-spacing: -0.04em;
    line-height: 1;
    display: flex;
    align-items: center;
  }

  .brand-text-tools {
    color: #ffffff;
  }

  .brand-text-radar {
    background: linear-gradient(135deg, #38bdf8 0%, #818cf8 60%, #c084fc 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }

  /* Headline */
  .main-headline {
    font-size: 38px;
    font-weight: 800;
    line-height: 1.25;
    letter-spacing: -0.03em;
    color: #ffffff;
    margin-bottom: 12px;
  }

  .gradient-headline {
    background: linear-gradient(135deg, #38bdf8 0%, #a855f7 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }

  /* Subtitle */
  .lead-desc {
    font-size: 19px;
    line-height: 1.55;
    color: #a1a1aa;
    max-width: 580px;
    margin-bottom: 18px;
  }

  /* Feature Pills */
  .feature-pills {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
  }

  .pill {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    font-size: 14px;
    font-weight: 700;
    padding: 7px 14px;
    border-radius: 8px;
    font-family: 'JetBrains Mono', monospace;
  }

  .pill-cyan {
    background: rgba(56, 189, 248, 0.1);
    border: 1px solid rgba(56, 189, 248, 0.35);
    color: #7dd3fc;
  }

  .pill-purple {
    background: rgba(168, 85, 247, 0.1);
    border: 1px solid rgba(168, 85, 247, 0.35);
    color: #d8b4fe;
  }

  .pill-emerald {
    background: rgba(16, 185, 129, 0.1);
    border: 1px solid rgba(16, 185, 129, 0.35);
    color: #6ee7b7;
  }

  .pill-amber {
    background: rgba(245, 158, 11, 0.1);
    border: 1px solid rgba(245, 158, 11, 0.35);
    color: #fcd34d;
  }

  /* Footer Line */
  .footer-row {
    display: flex;
    align-items: center;
    gap: 14px;
    padding-top: 14px;
    border-top: 1px solid rgba(255, 255, 255, 0.1);
    font-family: 'JetBrains Mono', monospace;
    font-size: 15px;
  }

  .footer-domain {
    color: #38bdf8;
    font-weight: 700;
  }

  .footer-caption {
    color: #71717a;
  }

  /* Outer Border Frame */
  .frame-border {
    position: absolute;
    inset: 0;
    border: 1px solid rgba(56, 189, 248, 0.35);
    pointer-events: none;
    z-index: 20;
  }
</style>
</head>
<body>
  <div class="frame-border"></div>
  <div class="grid-bg"></div>
  <div class="glow-cyan"></div>
  <div class="glow-purple"></div>

  <!-- Left Main Content -->
  <div class="hero-content">
    <div>
      <div class="status-badge">
        <span class="live-dot"></span>
        <span class="status-text">LIVE RADAR TELEMETRY • 975+ VERIFIED TOOLS</span>
      </div>

      <!-- Exact Official Logo & Gradient Brand Text -->
      <div class="brand-row">
        <!-- SVG Inlined Directly from favicon.svg with exact geometry -->
        <svg xmlns="http://www.w3.org/2000/svg" width="60" height="60" viewBox="0 0 48 48" fill="none">
          <defs>
            <linearGradient id="tr-bg" x1="0" y1="0" x2="48" y2="48" gradientUnits="userSpaceOnUse">
              <stop offset="0%" stop-color="#0c0e17"/>
              <stop offset="100%" stop-color="#05070a"/>
            </linearGradient>
            <linearGradient id="tr-beam" x1="24" y1="24" x2="42" y2="10" gradientUnits="userSpaceOnUse">
              <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.85"/>
              <stop offset="70%" stop-color="#818cf8" stop-opacity="0.3"/>
              <stop offset="100%" stop-color="#c084fc" stop-opacity="0"/>
            </linearGradient>
            <filter id="tr-glow" x="-20%" y="-20%" width="140%" height="140%">
              <feGaussianBlur stdDeviation="1.8" result="blur"/>
              <feComposite in="SourceGraphic" in2="blur" operator="over"/>
            </filter>
          </defs>
          <rect width="48" height="48" rx="12" fill="url(#tr-bg)"/>
          <rect width="48" height="48" rx="12" stroke="rgba(56, 189, 248, 0.45)" stroke-width="1.4"/>
          <line x1="24" y1="7" x2="24" y2="41" stroke="rgba(129, 140, 248, 0.22)" stroke-width="1" stroke-dasharray="2 2"/>
          <line x1="7" y1="24" x2="41" y2="24" stroke="rgba(129, 140, 248, 0.22)" stroke-width="1" stroke-dasharray="2 2"/>
          <circle cx="24" cy="24" r="17" stroke="rgba(129, 140, 248, 0.3)" stroke-width="1.2"/>
          <circle cx="24" cy="24" r="11.5" stroke="rgba(56, 189, 248, 0.5)" stroke-width="1.2"/>
          <circle cx="24" cy="24" r="6" stroke="rgba(56, 189, 248, 0.85)" stroke-width="1.4"/>
          <path d="M 24 24 L 38 12 A 17 17 0 0 0 24 7 Z" fill="url(#tr-beam)"/>
          <line x1="24" y1="24" x2="38" y2="12" stroke="#38bdf8" stroke-width="1.8" stroke-linecap="round" filter="url(#tr-glow)"/>
          <circle cx="24" cy="24" r="2.8" fill="#ffffff" filter="url(#tr-glow)"/>
        </svg>

        <span class="nav-brand-text">
          <span class="brand-text-tools">Tools</span><span class="brand-text-radar">Radar</span>
        </span>
      </div>

      <h1 class="main-headline">
        The Intelligence Radar for<br>
        <span class="gradient-headline">Breakthrough DevTools & AI</span>
      </h1>

      <p class="lead-desc">
        Independent real-time tracking of high-signal software, autonomous AI agents, and privacy-first open-source alternatives.
      </p>

      <div class="feature-pills">
        <span class="pill pill-cyan">⚡ Daily Automated Crawls</span>
        <span class="pill pill-purple">📖 4-Chapter Dossiers</span>
        <span class="pill pill-emerald">🔄 OSS Alternatives</span>
        <span class="pill pill-amber">🐳 Self-Hostable</span>
      </div>
    </div>

    <!-- Bottom Footer Row -->
    <div class="footer-row">
      <span class="footer-domain">https://lordorange.top</span>
      <span class="footer-caption">• Real-Time Software Intelligence Directory</span>
    </div>
  </div>

  <!-- Right Side: Big Radar HUD Graphic -->
  <div class="radar-hud">
    <svg width="480" height="480" viewBox="0 0 480 480" fill="none">
      <defs>
        <radialGradient id="hud-sweep" cx="50%" cy="50%" r="50%">
          <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.35"/>
          <stop offset="70%" stop-color="#818cf8" stop-opacity="0.1"/>
          <stop offset="100%" stop-color="#c084fc" stop-opacity="0"/>
        </radialGradient>
      </defs>

      <!-- Concentric Range Rings -->
      <circle cx="240" cy="240" r="220" stroke="rgba(56, 189, 248, 0.18)" stroke-width="1.5"/>
      <circle cx="240" cy="240" r="160" stroke="rgba(56, 189, 248, 0.25)" stroke-width="1.5"/>
      <circle cx="240" cy="240" r="100" stroke="rgba(56, 189, 248, 0.35)" stroke-width="1.5"/>
      <circle cx="240" cy="240" r="40" stroke="rgba(56, 189, 248, 0.55)" stroke-width="1.5"/>

      <!-- Crosshairs -->
      <line x1="240" y1="10" x2="240" y2="470" stroke="rgba(56, 189, 248, 0.2)" stroke-width="1.2" stroke-dasharray="4 4"/>
      <line x1="10" y1="240" x2="470" y2="240" stroke="rgba(56, 189, 248, 0.2)" stroke-width="1.2" stroke-dasharray="4 4"/>
      
      <!-- 45-degree diagonals -->
      <line x1="84" y1="84" x2="396" y2="396" stroke="rgba(56, 189, 248, 0.12)" stroke-width="1"/>
      <line x1="84" y1="396" x2="396" y2="84" stroke="rgba(56, 189, 248, 0.12)" stroke-width="1"/>

      <!-- Radar Scanning Sweep Wedge -->
      <path d="M 240 240 L 420 120 A 220 220 0 0 0 240 20 Z" fill="url(#hud-sweep)"/>
      <line x1="240" y1="240" x2="420" y2="120" stroke="#38bdf8" stroke-width="2.5" stroke-linecap="round"/>

      <!-- Target Blips -->
      <!-- Blip 1: Emerald -->
      <circle cx="150" cy="160" r="14" stroke="rgba(16, 185, 129, 0.4)" stroke-width="1"/>
      <circle cx="150" cy="160" r="5" fill="#10b981"/>

      <!-- Blip 2: Cyan -->
      <circle cx="340" cy="150" r="16" stroke="rgba(56, 189, 248, 0.45)" stroke-width="1"/>
      <circle cx="340" cy="150" r="6" fill="#38bdf8"/>

      <!-- Blip 3: Amber -->
      <circle cx="310" cy="330" r="14" stroke="rgba(245, 158, 11, 0.4)" stroke-width="1"/>
      <circle cx="310" cy="330" r="5" fill="#f59e0b"/>

      <!-- Blip 4: Purple -->
      <circle cx="170" cy="320" r="12" stroke="rgba(168, 85, 247, 0.4)" stroke-width="1"/>
      <circle cx="170" cy="320" r="4.5" fill="#a855f7"/>

      <!-- Center Pulse Core -->
      <circle cx="240" cy="240" r="6" fill="#ffffff"/>
      <circle cx="240" cy="240" r="12" stroke="#38bdf8" stroke-width="1.5"/>
    </svg>
  </div>
</body>
</html>
"""

def generate_og():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_path = os.path.join(base_dir, "site", "public", "og-default.png")

    edge_paths = [
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    ]
    browser = None
    for p in edge_paths:
        if os.path.exists(p):
            browser = p
            break

    if not browser:
        print("[ERROR] Neither Edge nor Chrome found on system.")
        return False

    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as f:
        f.write(HTML_TEMPLATE)
        temp_html = f.name

    try:
        cmd = [
            browser,
            "--headless",
            "--disable-gpu",
            "--hide-scrollbars",
            f"--window-size=1200,630",
            f"--screenshot={output_path}",
            temp_html
        ]
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
        if os.path.exists(output_path) and os.path.getsize(output_path) > 1000:
            print(f"[SUCCESS] Pixel-perfect OpenGraph card generated at: {output_path}")
            print(f"File size: {os.path.getsize(output_path)} bytes")
            return True
        else:
            print(f"[ERROR] Failed to generate screenshot: {res.stderr}")
            return False
    finally:
        if os.path.exists(temp_html):
            os.remove(temp_html)

if __name__ == "__main__":
    generate_og()
