# ToolsRadar Design System & Art Direction Specification

Designed according to `/awwwards` Site of the Day evaluation criteria: Design 40%, Usability 30%, Creativity 20%, Content 10%.

---

## 1. Concept Card

- **Idea**: Real-time intelligence radar discovering, benchmarking, and curating tomorrow's breakthrough developer tools, autonomous AI agents, and open-source alternatives.
- **Metaphor**: High-precision aerospace radar scope and developer telemetry laboratory (polar grids, sweeping beam, blip coordinates, tactile HUD inspect panels).
- **Signature**: Interactive 2D Canvas Radar Scope with active sweeping beam, live tool blips mapped to categories and traction, particle ping waves, and instant HUD telemetry cards on hover.
- **Emotion**: Surgical, authoritative, exploratory, exhilaratingly fast.
- **Motion verb**: "Sweep like radar, snap like precision instruments, settle like telemetry readouts."
- **Screenshot moment**: The Hero section with the illuminated polar radar scope, real-time sweeping beam illuminating high-traction blips, paired with the Breakthrough Spotlight magazine card.

---

## 2. Art Direction System

### Palette Tokens
```css
:root {
  --bg-ground: #07080a;        /* Deep obsidian void */
  --surface: #0e0f14;          /* Precision dark slate */
  --surface-raised: #13141c;   /* Elevated panel */
  --surface-card: rgba(15, 16, 23, 0.78);
  --border-hairline: rgba(255, 255, 255, 0.07);
  --border-hover: rgba(56, 189, 248, 0.35);
  --border-active: rgba(56, 189, 248, 0.6);
  --beam-cyan: #38bdf8;        /* Radar sweep primary */
  --beam-cyan-glow: rgba(56, 189, 248, 0.25);
  --aurora-purple: #a855f7;    /* AI & High Signal */
  --neon-emerald: #10b981;     /* Open Source & Verified */
  --amber-traction: #f59e0b;   /* Breakout momentum */
  --text-ink: #f8fafc;         /* Crisp primary typography */
  --text-secondary: #94a3b8;   /* Balanced body copy */
  --text-muted: #64748b;       /* Micro telemetry labels */
}
```

### Typography
- **Headings & Display**: `-apple-system, BlinkMacSystemFont, "Geist", "Inter", sans-serif` with negative letter-spacing (`-0.035em`) and deliberate optical tracking.
- **Data & Telemetry**: `ui-monospace, "JetBrains Mono", SFMono-Regular, Menlo, Monaco, Consolas, monospace`.
- **Fluid Scale**:
  - Hero Display: `clamp(2.4rem, 5vw, 3.8rem)`
  - Section Headings: `clamp(1.5rem, 3vw, 2.1rem)`
  - Card Titles: `1.15rem`
  - Body Text: `1rem` with `1.65` line-height
  - Micro Telemetry: `0.75rem` uppercase with `0.05em` letter-spacing

### Grid & Layout Rhythm
- Max container width: `1220px`
- Section gap: `5rem` to `6rem` vertical breathing space
- Radius tokens:
  - Small pills: `6px` / `8px`
  - Cards: `16px`
  - Hero containers: `22px`

---

## 3. Motion Engine & Choreography
- **Smooth Inertia**: Lenis for smooth scrolling without scroll-jacking.
- **GSAP Ticker**: Synchronized animations via GSAP ticker.
- **Staggered Reveal**: Sections stagger in upon viewport intersection.
- **Interactive Cursor Glow**: Tool cards calculate radial gradient cursor position on `pointermove`.
- **Accessibility**: Zero animations or smooth scroll when `prefers-reduced-motion: reduce` is active.
