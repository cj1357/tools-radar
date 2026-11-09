# -*- coding: utf-8 -*-
import os

file_path = r"d:\_projectsTYweb\tools-radar\site\src\components\RadarScope.astro"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update draw() empty width/height check
old_draw = """    // Main Draw Loop
    function draw() {
      // Auto-realign if DOM layout settles or shifts after initial paint
      const curRect = stage.getBoundingClientRect();
      if (Math.abs(curRect.width - width) > 1 || Math.abs(curRect.height - height) > 1) {
        resize();
      }

      ctx.clearRect(0, 0, width, height);"""

new_draw = """    // Main Draw Loop
    function draw() {
      // Auto-realign if DOM layout settles or shifts after initial paint
      const curRect = stage.getBoundingClientRect();
      if (Math.abs(curRect.width - width) > 1 || Math.abs(curRect.height - height) > 1) {
        resize();
      }
      if (width === 0 || height === 0) {
        animationFrameId = requestAnimationFrame(draw);
        return;
      }

      ctx.clearRect(0, 0, width, height);"""

assert old_draw.replace("\r\n", "\n") in content.replace("\r\n", "\n"), "old_draw not found"

# 2. Update sweepAngle calculation
old_sweep = """      // 3. Sweeping Radar Beam (Conic Gradient Simulation)
      if (!isPaused) {
        sweepAngle = (sweepAngle + 0.016) % (Math.PI * 2);
      } else {
        sweepAngle = (sweepAngle + 0.003) % (Math.PI * 2);
      }"""

new_sweep = """      // 3. Sweeping Radar Beam (Conic Gradient Simulation)
      const isReduced = typeof window !== 'undefined' && window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
      const normalStep = isReduced ? 0.008 : 0.016;
      const pausedStep = isReduced ? 0.002 : 0.003;
      sweepAngle = (sweepAngle + (isPaused ? pausedStep : normalStep)) % (Math.PI * 2);"""

assert old_sweep.replace("\r\n", "\n") in content.replace("\r\n", "\n"), "old_sweep not found"

# 3. Update start loop and add visibility listeners
old_loop = """    // Start loop if not reduced motion
    if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
      draw();
    } else {
      // Static single draw
      sweepAngle = Math.PI / 4;
      draw();
      cancelAnimationFrame(animationFrameId);
    }"""

new_loop = """    // Start animation loop reliably across all browsers & system settings
    function startAnimation() {
      if (!animationFrameId) {
        animationFrameId = requestAnimationFrame(draw);
      }
    }

    function stopAnimation() {
      if (animationFrameId) {
        cancelAnimationFrame(animationFrameId);
        animationFrameId = null;
      }
    }

    // Auto-resume loop when tab becomes active / visible (handles background tab freeze & energy saver)
    document.addEventListener('visibilitychange', () => {
      if (document.hidden) {
        stopAnimation();
      } else {
        resize();
        startAnimation();
      }
    });

    window.addEventListener('focus', () => {
      if (!animationFrameId) {
        resize();
        startAnimation();
      }
    });

    // Start animation loop
    startAnimation();"""

assert old_loop.replace("\r\n", "\n") in content.replace("\r\n", "\n"), "old_loop not found"

# Apply replacements preserving CRLF if present
is_crlf = "\r\n" in content
nl = "\r\n" if is_crlf else "\n"

content_norm = content.replace("\r\n", "\n")
content_norm = content_norm.replace(old_draw.replace("\r\n", "\n"), new_draw.replace("\r\n", "\n"))
content_norm = content_norm.replace(old_sweep.replace("\r\n", "\n"), new_sweep.replace("\r\n", "\n"))
content_norm = content_norm.replace(old_loop.replace("\r\n", "\n"), new_loop.replace("\r\n", "\n"))

final_content = content_norm.replace("\n", "\r\n") if is_crlf else content_norm

with open(file_path, "w", encoding="utf-8") as f:
    f.write(final_content)

print("RadarScope.astro successfully updated!")
