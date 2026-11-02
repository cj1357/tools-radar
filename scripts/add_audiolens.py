# -*- coding: utf-8 -*-
"""
Add AudioLens (GitHub Issue #2 submission by SimZhou)
to all_tools.json and editorial_reviews.json
"""

import json
import os
import sys

data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data"))
all_tools_path = os.path.join(data_dir, "all_tools.json")
reviews_path = os.path.join(data_dir, "editorial_reviews.json")

AUDIOLENS_TOOL = {
    "id": "audiolens",
    "name": "AudioLens",
    "tagline": "Audio playback, multi-channel waveforms, and spectrogram analysis directly in VS Code",
    "summary": "AudioLens is an open-source Visual Studio Code extension engineered for speech AI researchers, audio DSP developers, and machine learning engineers. It eliminates the friction of switching to external audio editors by embedding multi-channel waveform playback, real-time FFT spectrogram visualization, and audio telemetry directly into the editor. Featuring support for Remote SSH workspaces, raw headerless PCM decoding, and Kaldi archive inspection, it provides immediate acoustic inspection alongside code and dataset manifests.",
    "url": "https://marketplace.visualstudio.com/items?itemName=simzhou.audiolens",
    "github_url": "https://github.com/SimZhou/vscode-audiolens",
    "source": "submission",
    "category": "developer-tools",
    "tags": [
        "VS Code Extension",
        "Audio Processing",
        "Spectrogram",
        "Waveform",
        "Speech AI",
        "DSP",
        "Open Source",
        "Apache 2.0"
    ],
    "pricing_model": "Free",
    "stars": 67,
    "primary_alternative": "Audacity",
    "is_self_hostable": True,
    "no_signup_required": True,
    "signal_score": 89,
    "verdict": "An indispensable VS Code extension for machine learning speech engineers and DSP developers, bringing multi-channel waveform playback, real-time spectrogram analysis, and raw PCM inspection directly into the editor without external GUI bloat.",
    "key_features": [
        {
            "title": "Integrated Waveforms & Spectrograms",
            "description": "Inspect synchronized multi-channel waveforms and Fourier transform spectrograms on a shared interactive timeline with mute and solo controls."
        },
        {
            "title": "Acoustic Telemetry & Metrics",
            "description": "Calculate RMS power, peak decibels, clipping ratios, crest factors, and frequency distributions for any highlighted audio selection."
        },
        {
            "title": "Remote SSH & Raw PCM Support",
            "description": "Stream audio directly from remote Linux training servers via VS Code Remote SSH, decode raw headerless PCM, and inspect Kaldi archives."
        }
    ],
    "use_cases": [
        "Inspecting synthetic speech output and dataset audio quality directly within VS Code while training TTS/STT neural models",
        "Auditing audio datasets stored on remote GPU clusters over SSH without manually downloading multi-gigabyte audio files",
        "Validating raw PCM sample formats, sample rates, and clipping boundaries during embedded audio DSP firmware development"
    ],
    "pros": [
        "Permissive Apache-2.0 open-source license with complete code transparency and zero commercial restrictions",
        "Eliminates window-switching context overhead by keeping audio inspection adjacent to training code and manifests",
        "Robust support for machine learning speech formats including Kaldi archives, raw PCM, and multi-channel WAVs"
    ],
    "cons": [
        "Restricted to the Visual Studio Code ecosystem (or compatible forks like Cursor and VSCodium)",
        "Focuses on visual inspection, playback, and analysis rather than destructive multitrack audio editing"
    ],
    "target_audience": "Speech AI researchers, machine learning engineers, audio DSP developers, and data scientists working with acoustic datasets.",
    "comparison_vs_alt": "Unlike launching heavyweight standalone audio software like Audacity or plotting static spectrograms with matplotlib and librosa, AudioLens renders interactive, responsive audio playback directly within VS Code editor tabs.",
    "install_command": "code --install-extension simzhou.audiolens",
    "date_added": "2026-11-02",
    "featured": False
}

AUDIOLENS_DOSSIER = {
    "article_title": "AudioLens Architecture & Engineering Dossier: In-Editor Web Audio Signal Processing and Spectrogram Synthesis in VS Code",
    "reading_time": "5 min read",
    "editorial_verdict_callout": "AudioLens eliminates window-switching friction for machine learning speech researchers, bringing multi-channel waveform playback, real-time spectrograms, and remote PCM analysis directly into VS Code.",
    "chapters": [
        {
            "id": "architecture-mechanics",
            "number": "01",
            "title": "Architectural Foundation & Execution Mechanics",
            "content": (
                "AudioLens is architected as a native Visual Studio Code extension built on top of the VS Code Custom Editor and Webview APIs. "
                "Rather than executing external binary sub-processes, the extension runs directly within an isolated Webview runtime, taking full "
                "advantage of the modern browser Web Audio API, Web Workers, and hardware-accelerated HTML5 2D Canvas rendering pipelines. The "
                "audio decoding layer ingests standard formats (WAV, FLAC, MP3, OGG) through native Web Audio decoders, while incorporating custom "
                "stream parsers for machine learning specific formats, such as Kaldi archive files (.ark/.scp) and headerless raw PCM streams. When "
                "opening raw PCM, the user defines exact bit depths, sample rates, channel configurations, and endianness parameters, which AudioLens "
                "dynamically converts into uncompressed Float32Array audio buffers. Spectrogram generation executes via a custom Fast Fourier Transform "
                "(FFT) implementation running inside Web Workers to avoid blocking the main UI thread during intensive spectral convolutions. Crucially, "
                "AudioLens functions seamlessly across VS Code Remote SSH tunnels; audio data is streamed asynchronously from remote Linux training nodes "
                "through the extension host IPC channel directly into the client Webview buffer, enabling instantaneous playback without downloading entire datasets."
            )
        },
        {
            "id": "ergonomics-developer-experience",
            "number": "02",
            "title": "Developer Ergonomics & CLI / API Surface",
            "content": (
                "Developer ergonomics in AudioLens are tuned specifically for high-velocity machine learning research, speech dataset curation, "
                "and digital signal processing workflows. Opening an audio file presents a synchronized dual-view timeline rendering per-channel "
                "waveforms alongside continuous Fourier spectrograms. Users can scrub through timelines, isolate individual audio channels using intuitive "
                "mute and solo toggles, and drag-select arbitrary temporal regions with millisecond precision for targeted loop playback. An integrated "
                "Selection Analysis inspector instantly computes essential acoustic telemetry, including root-mean-square (RMS) energy, peak levels in dBFS, "
                "crest factor ratios, clipping percentage counts, zero-crossing rates, and dominant frequency centroids. The spectrogram visualization "
                "exposes granular parameter controls: developers can adjust FFT window sizes (from 256 to 4096 bins), toggle windowing functions (Hann, "
                "Hamming, Blackman), calibrate decibel dynamic range floors, and select scientific color palettes like Viridis or Magma. Because AudioLens "
                "registers as a standard custom editor in VS Code, engineers can dock audio inspection tabs directly beside PyTorch DataLoader scripts "
                "or training loss dashboards, completely eliminating the mental friction of switching between external audio suites like Audacity and terminal code, "
                "significantly accelerating rapid iterative experimentation during acoustic model training cycles."
            )
        },
        {
            "id": "licensing-tco-audit",
            "number": "03",
            "title": "Total Cost of Ownership (TCO) & Licensing Audit",
            "content": (
                "From a licensing and compliance perspective, AudioLens is distributed under the permissive Apache License 2.0, providing complete source "
                "code inspectability, commercial deployment freedom, and intellectual property safety for enterprise machine learning teams. Because the "
                "extension installs directly from the open Visual Studio Code Marketplace or Open VSX Registry, organizations incur zero software procurement "
                "costs or recurring seat license liabilities. AudioLens requires no user accounts, external SaaS registrations, or proprietary cloud backend "
                "services; all signal processing, decoding, and spectral calculations execute strictly on the local workstation or within the connected "
                "Remote SSH session. This zero-cloud, local-first operational architecture ensures absolute data privacy for confidential speech recordings, "
                "proprietary voice synthesis models, and defense-related acoustics research. Total Cost of Ownership is effectively zero dollars, as the "
                "tooling runs within existing IDE resource footprints without background daemon overhead, persistent database requirements, or continuous "
                "dependency maintenance. Enterprise teams can audit the full TypeScript codebase on GitHub to satisfy internal open-source security compliance guidelines, "
                "making it an ideal, frictionless addition to secure corporate research environments, audio data labs, and commercial deep learning engineering pipelines "
                "seeking reliable local-first tools without recurrent SaaS subscription overhead."
            )
        },
        {
            "id": "production-verdict",
            "number": "04",
            "title": "Production Readiness Verdict & Deployment Guidance",
            "content": (
                "AudioLens earns an unreserved production adoption recommendation for machine learning speech engineers, audio DSP firmware developers, "
                "and data scientists building automatic speech recognition (ASR) or text-to-speech (TTS) systems. Having instant, visual and acoustic "
                "telemetry embedded directly within the code editor fundamentally accelerates dataset cleaning, audio augmentation verification, and "
                "model inference debugging. However, development leads must respect its clear architectural boundaries: AudioLens is fundamentally an "
                "audio inspection, diagnostics, and playback tool, not a full-featured multitrack Digital Audio Workstation (DAW). It deliberately does "
                "not support destructive audio editing, multi-track time-stretching, VST plugin hosting, or audio cutting operations, which remain the domain "
                "of dedicated desktop software. Additionally, extremely large multi-hour uncompressed audio files may encounter Webview memory constraints, "
                "making it best suited for audio clips, utterances, and dataset batches under a few hundred megabytes. For speech engineers tired of launching "
                "heavyweight external editors or authoring one-off matplotlib scripts just to inspect audio waveforms, AudioLens is an indispensable daily developer utility "
                "that dramatically streamlines speech and audio engineering workflows while preserving peak developer concentration across active coding sessions, "
                "continuous integration audits, and machine learning model evaluation pipelines."
            )
        }
    ]
}

def validate_and_merge():
    print("=== Step 1: Verifying AudioLens Word Counts (180-220 words per chapter) ===")
    counts = []
    for ch in AUDIOLENS_DOSSIER["chapters"]:
        words = len(ch["content"].split())
        counts.append(words)
        print(f"  Ch {ch['number']} ({ch['id']}): {words} words")
        assert 180 <= words <= 220, f"Error: AudioLens Ch {ch['number']} word count {words} out of range [180, 220]"
    print(f"  -> All 4 chapters OK: {counts}")

    print("\n=== Step 2: Ingesting into all_tools.json ===")
    with open(all_tools_path, "r", encoding="utf-8") as f:
        master_tools = json.load(f)
    
    existing_ids = {t["id"] for t in master_tools}
    if AUDIOLENS_TOOL["id"] not in existing_ids:
        master_tools.append(AUDIOLENS_TOOL)
        with open(all_tools_path, "w", encoding="utf-8") as f:
            json.dump(master_tools, f, indent=2, ensure_ascii=False)
        print(f"Added AudioLens to all_tools.json. Total tools now: {len(master_tools)}")
    else:
        print("AudioLens already exists in all_tools.json")

    print("\n=== Step 3: Ingesting into editorial_reviews.json ===")
    with open(reviews_path, "r", encoding="utf-8") as f:
        master_reviews = json.load(f)

    if "audiolens" not in master_reviews:
        master_reviews["audiolens"] = AUDIOLENS_DOSSIER
        with open(reviews_path, "w", encoding="utf-8") as f:
            json.dump(master_reviews, f, indent=2, ensure_ascii=False)
        print(f"Added AudioLens dossier to editorial_reviews.json. Total reviews now: {len(master_reviews)}")
    else:
        print("AudioLens dossier already exists in editorial_reviews.json")

    print("\n[SUCCESS] AudioLens ingested cleanly!")

if __name__ == "__main__":
    validate_and_merge()
