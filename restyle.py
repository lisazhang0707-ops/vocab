with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Find the style block boundaries
start_marker = "<style>"
end_marker = "</style>"

start_idx = content.index(start_marker) + len(start_marker)
end_idx = content.index(end_marker)

new_css = """
  * { margin: 0; padding: 0; box-sizing: border-box; }
  
  @keyframes fadeInUp {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
  }
  
  @keyframes glowPulse {
    0%, 100% { text-shadow: 0 0 4px rgba(232,200,160,0.2); }
    50% { text-shadow: 0 0 12px rgba(232,200,160,0.5); }
  }
  
  @keyframes progressFlow {
    0% { background-position: 0% 50%; }
    100% { background-position: 300% 50%; }
  }
  
  body { font-family: 'Segoe UI', system-ui, -apple-system, sans-serif; background: #1a1d2e; color: #c8c0d8; min-height: 100vh; display: flex; flex-direction: column; align-items: center; padding: 24px 16px; }
  
  h1 {
    font-size: 1.4rem;
    background: linear-gradient(90deg, #e0c8a0, #b8a0d0);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 2px;
    font-weight: 600;
  }
  
  .eb { color: #8896a8; font-size: 0.8rem; margin-bottom: 20px; }
  
  .card-wrap { width: 100%; max-width: 600px; position: relative; animation: fadeInUp 0.5s ease-out; }
  
  .card {
    background: #242840;
    border-radius: 20px;
    padding: 32px 28px 28px;
    min-height: 280px;
    cursor: pointer;
    transition: transform 0.3s, box-shadow 0.3s;
    display: flex;
    flex-direction: column;
    box-shadow: 0 8px 32px rgba(0,0,0,0.5), 0 2px 8px rgba(0,0,0,0.3);
    position: relative;
    overflow: hidden;
    perspective: 1000px;
  }
  
  .card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 3px;
    background: linear-gradient(90deg, #c8a868, #a888c8);
  }
  
  .card:hover {
    transform: translateY(-3px);
    box-shadow: 0 12px 40px rgba(0,0,0,0.55), 0 4px 12px rgba(0,0,0,0.35);
  }
  
  .word-row { display: flex; align-items: center; gap: 10px; margin-bottom: 4px; flex-wrap: wrap; }
  
  .word {
    font-size: 2rem;
    font-weight: 700;
    background: linear-gradient(135deg, #e0c8a0, #b8a0d0);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    letter-spacing: 0.02em;
    transition: text-shadow 0.3s;
  }
  .word:hover { animation: glowPulse 1.5s ease-in-out infinite; }
  
  .level-tag { font-size: 0.65rem; padding: 2px 7px; border-radius: 4px; font-weight: 600; letter-spacing: 0.02em; margin-left: 2px; }
  
  .word-speaker {
    background: none;
    border: none;
    cursor: pointer;
    font-size: 1.3rem;
    padding: 4px 8px;
    border-radius: 8px;
    transition: all 0.2s;
    color: #8896a8;
  }
  .word-speaker:hover { background: #303558; color: #b8a0d0; transform: scale(1.1); }
  .word-speaker.playing { color: #8ab88a; }
  
  .meta { display: flex; gap: 12px; align-items: center; margin-bottom: 16px; flex-wrap: wrap; }
  .pron { color: #6a7a8e; font-size: 0.9rem; }
  .pos { background: #303558; color: #a8b8c8; font-size: 0.75rem; padding: 2px 8px; border-radius: 4px; }
  
  .section { display: none; margin-top: 12px; }
  .section-label { font-size: 0.72rem; color: #6a7a8e; text-transform: uppercase; letter-spacing: 0.06em; margin-bottom: 4px; }
  
  .def { color: #c8c0d8; font-size: 1rem; line-height: 1.8; }
  .ex-en { color: #a8b8c8; font-size: 0.88rem; line-height: 1.8; font-style: italic; display: flex; align-items: flex-start; gap: 8px; }
  .ex-cn { color: #7a8a9e; font-size: 0.85rem; line-height: 1.8; margin-top: 4px; padding-left: 0; }
  
  .syntax {
    color: #a090b8;
    font-size: 0.82rem;
    line-height: 1.8;
    margin-top: 8px;
    padding: 10px 12px;
    background: #1e2338;
    border-radius: 8px;
    border-left: 3px solid #7a6a9e;
    white-space: pre-line;
  }
  .syntax-label { font-size: 0.7rem; color: #7a6a9e; text-transform: uppercase; letter-spacing: 0.06em; margin-bottom: 4px; }
  
  .tip {
    color: #c8a868;
    font-size: 0.85rem;
    line-height: 1.8;
    margin-top: 14px;
    padding-top: 12px;
    border-top: 1px solid #303558;
  }
  
  .speaker-btn {
    background: none;
    border: none;
    cursor: pointer;
    padding: 0;
    margin-top: 6px;
    color: #8896a8;
    display: flex;
    align-items: center;
    gap: 5px;
    font-size: 0.78rem;
    transition: color 0.2s;
  }
  .speaker-btn:hover { color: #b8a0d0; }
  
  .status-bar { width: 100%; max-width: 600px; display: flex; justify-content: space-between; align-items: center; margin-top: 10px; font-size: 0.78rem; color: #6a7a8e; }
  .due-count { color: #d08060; }
  .streak { color: #8ab88a; }
  .today-left { color: #8896a8; }
  
  .nav { display: flex; gap: 8px; margin-top: 14px; width: 100%; max-width: 600px; }
  .nav button {
    flex: 1;
    padding: 11px 8px;
    border: none;
    border-radius: 24px;
    font-size: 0.88rem;
    cursor: pointer;
    font-weight: 500;
    transition: all 0.2s;
  }
  .nav button:active { transform: scale(0.95); }
  .nav button.forgot { background: #2a1e1e; color: #d08060; }
  .nav button.forgot:hover { background: #3a2828; transform: scale(1.05); }
  .nav button.hard { background: #2d2818; color: #c0a850; }
  .nav button.hard:hover { background: #3d3828; transform: scale(1.05); }
  .nav button.good { background: #1d2d22; color: #8ab88a; }
  .nav button.good:hover { background: #2d3d32; transform: scale(1.05); }
  .nav button.easy { background: #1d2230; color: #7088c0; }
  .nav button.easy:hover { background: #2d3240; transform: scale(1.05); }
  
  .hint { color: #5a6a7e; font-size: 0.75rem; text-align: center; margin-top: 10px; }
  
  .done-msg {
    width: 100%; max-width: 600px; min-height: 280px;
    background: #242840; border-radius: 20px;
    display: flex; flex-direction: column; align-items: center; justify-content: center;
    gap: 16px; color: #8896a8; text-align: center; padding: 40px;
  }
  .done-msg .big { font-size: 3rem; }
  .done-msg p { font-size: 1rem; }
  .done-msg .sub { font-size: 0.85rem; color: #6a7a8e; }
  
  .progress-wrap { width: 100%; max-width: 600px; margin-top: 16px; }
  .prog-bar { height: 3px; background: #303558; border-radius: 2px; overflow: hidden; }
  .prog-fill {
    height: 100%;
    background: linear-gradient(90deg, #c8a868, #a888c8, #8ab88a, #c8a868);
    background-size: 300% 100%;
    animation: progressFlow 3s linear infinite;
    transition: width 0.4s;
  }
  .prog-label { display: flex; justify-content: space-between; font-size: 0.72rem; color: #6a7a8e; margin-top: 5px; }
  
  .reset-btn {
    background: #303558;
    border: 1px solid #404868;
    color: #8896a8;
    font-size: 0.75rem;
    padding: 5px 12px;
    border-radius: 6px;
    cursor: pointer;
    margin-top: 8px;
    transition: all 0.2s;
  }
  .reset-btn:hover { background: #404868; color: #a8a8b8; }
  
  .practice-wrap { width: 100%; max-width: 600px; margin-top: 24px; animation: fadeInUp 0.5s ease-out 0.1s both; }
  .practice-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; }
  .practice-title { font-size: 0.9rem; color: #8896a8; }
  .practice-badge { background: #303558; color: #b8a0d0; font-size: 0.7rem; padding: 2px 8px; border-radius: 10px; }
  
  .practice-area {
    background: #242840;
    border-radius: 16px;
    padding: 16px;
    border: 1px solid #303558;
  }
  
  .voice-target {
    background: #1e2338;
    border-radius: 12px;
    padding: 10px 12px;
    margin-bottom: 10px;
    border: 1px solid #303558;
  }
  .voice-target-label { font-size: 0.7rem; color: #6a7a8e; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 6px; }
  .voice-target-text { font-size: 0.95rem; color: #a8b8c8; line-height: 1.6; font-style: italic; }
  .voice-target-pron { font-size: 0.8rem; color: #6a7a8e; margin-top: 4px; }
  
  .phonetic-info { display: none; margin-top: 8px; background: #1e2338; border-radius: 12px; padding: 10px 12px; border: 1px solid #303558; font-size: 0.82rem; line-height: 1.7; }
  .phonetic-info.show { display: block; }
  .phonetic-toggle { background: none; border: 1px solid #303558; color: #8896a8; font-size: 0.72rem; padding: 3px 8px; border-radius: 6px; cursor: pointer; margin-top: 6px; transition: all 0.15s; }
  .phonetic-toggle:hover { background: #303558; color: #a8a8b8; }
  .phonetic-toggle.active { border-color: #a888c8; color: #b8a0d0; }
  .phonetic-section { margin-bottom: 8px; }
  .phonetic-section:last-child { margin-bottom: 0; }
  .phonetic-label { font-size: 0.68rem; color: #6a7a8e; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 3px; }
  .phonetic-content { color: #8896a8; }
  .phonetic-content .stress { color: #d08060; font-weight: 600; text-decoration: underline; text-decoration-color: #d08060; }
  .phonetic-content .liaison { color: #b8a0d0; }
  .phonetic-content .weak { color: #6a7a8e; font-style: italic; }
  .phonetic-content .pause { color: #c0a850; font-weight: bold; }
  .phonetic-content .intl { color: #8ab88a; }
  .phonetic-raw { color: #6a7a8e; font-size: 0.78rem; line-height: 1.6; margin-top: 4px; }
  
  .annotated-sentence { line-height: 2; font-size: 0.95rem; }
  .annotated-sentence .a-stress { color: #d08060; font-weight: 700; text-decoration: underline wavy #d08060; }
  .annotated-sentence .a-liaison { color: #b8a0d0; text-decoration: underline dotted #b8a0d0; }
  .annotated-sentence .a-weak { color: #6a7a8e; }
  .annotated-sentence .a-pause { color: #c0a850; font-weight: bold; padding: 0 2px; }
  .annotated-sentence .a-normal { color: #a8b8c8; }
  
  .voice-transcript {
    min-height: 52px;
    background: #1a1d2e;
    border: 1px solid #303558;
    border-radius: 12px;
    padding: 10px 12px;
    margin-bottom: 10px;
    font-size: 0.92rem;
    color: #c8c0d8;
    line-height: 1.6;
  }
  .voice-transcript-placeholder { color: #6a7a8e; font-size: 0.85rem; }
  
  .voice-mic-row { display: flex; gap: 10px; align-items: center; margin-bottom: 10px; }
  .mic-btn {
    width: 56px; height: 56px; border-radius: 50%; border: none;
    cursor: pointer; display: flex; align-items: center; justify-content: center;
    font-size: 1.6rem; transition: all 0.2s; flex-shrink: 0;
    background: linear-gradient(135deg, #c8a868, #a888c8);
    color: #1a1d2e;
  }
  .mic-btn:hover { transform: scale(1.08); filter: brightness(1.15); }
  .mic-btn.recording { background: linear-gradient(135deg, #d08060, #c05050); animation: pulse 1s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{box-shadow:0 0 0 0 rgba(208,128,96,0.4)} 50%{box-shadow:0 0 0 14px rgba(208,128,96,0)} }
  .mic-status { font-size: 0.82rem; color: #6a7a8e; flex: 1; }
  .mic-status.active { color: #d08060; }
  
  .voice-compare { display: none; margin-top: 10px; background: #1e2338; border-radius: 12px; padding: 10px 12px; border: 1px solid #303558; }
  .voice-compare.show { display: block; }
  .compare-label { font-size: 0.7rem; color: #6a7a8e; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 6px; }
  .compare-row { display: flex; gap: 10px; align-items: flex-start; }
  .compare-col { flex: 1; }
  .compare-tag { font-size: 0.65rem; padding: 1px 5px; border-radius: 3px; margin-bottom: 3px; display: inline-block; }
  .compare-tag.yours { background: #2a1e1e; color: #d08060; }
  .compare-tag.target { background: #1e2838; color: #b8a0d0; }
  .compare-word { font-size: 0.88rem; line-height: 1.6; }
  .compare-word.wrong { color: #d08060; background: #2a1e1e; padding: 1px 4px; border-radius: 3px; }
  .compare-word.correct { color: #8ab88a; }
  .compare-word.missed { color: #c0a850; background: #2d2818; padding: 1px 4px; border-radius: 3px; text-decoration: underline; }
  
  .voice-actions { display: flex; gap: 8px; flex-wrap: wrap; }
  .voice-actions button {
    background: #303558;
    border: none;
    color: #a8b8c8;
    font-size: 0.78rem;
    padding: 6px 12px;
    border-radius: 8px;
    cursor: pointer;
    display: flex; align-items: center; gap: 5px;
    transition: all 0.15s;
  }
  .voice-actions button:hover { background: #404868; }
  .voice-actions button.primary { background: #1e2838; color: #b8a0d0; }
  .voice-actions button.primary:hover { background: #2d3850; }
  
  .practice-feedback { margin-top: 10px; font-size: 0.82rem; line-height: 1.6; padding: 10px 12px; border-radius: 8px; display: none; }
  .practice-feedback.error { background: #2a1e1e; color: #d08060; border: 1px solid #3a2828; display: block; }
  .practice-feedback.ok { background: #1d2d22; color: #8ab88a; border: 1px solid #2d3d32; display: block; }
  .practice-hint { font-size: 0.75rem; color: #6a7a8e; margin-top: 6px; }
  
  .practice-textarea { display: none; }
  
  .clickable-word { cursor: pointer; border-bottom: 1px dashed #8896a8; padding: 0 1px; transition: background 0.15s; border-radius: 2px; }
  .clickable-word:hover { background: #303558; }
  .clickable-word.added { border-bottom-color: #8ab88a; color: #8ab88a; }
  
  .modal-overlay { display: none; position: fixed; inset: 0; background: rgba(0,0,0,0.7); z-index: 1000; align-items: center; justify-content: center; padding: 20px; }
  .modal-overlay.show { display: flex; animation: fadeInUp 0.3s ease-out; }
  .modal { background: #242840; border-radius: 20px; padding: 24px; width: 100%; max-width: 440px; box-shadow: 0 12px 48px rgba(0,0,0,0.6); }
  .modal-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; }
  .modal-title { font-size: 1rem; color: #e0c8a0; }
  .modal-close { background: none; border: none; color: #8896a8; font-size: 1.2rem; cursor: pointer; padding: 4px; transition: color 0.15s; }
  .modal-close:hover { color: #c8c0d8; }
  .modal-word { font-size: 1.4rem; color: #b8a0d0; font-weight: 700; margin-bottom: 12px; }
  .modal-field { margin-bottom: 12px; }
  .modal-label { font-size: 0.72rem; color: #6a7a8e; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 4px; }
  .modal-input {
    width: 100%;
    background: rgba(26,29,46,0.8);
    backdrop-filter: blur(6px);
    border: 1px solid #303558;
    border-radius: 10px;
    color: #c8c0d8;
    font-size: 0.88rem;
    padding: 10px 12px;
    font-family: inherit;
    outline: none;
    box-sizing: border-box;
    transition: border-color 0.2s;
  }
  .modal-input:focus { border-color: #a888c8; box-shadow: 0 0 0 2px rgba(168,136,200,0.15); }
  .modal-input::placeholder { color: #6a7a8e; }
  .modal-actions { display: flex; gap: 8px; margin-top: 16px; }
  .modal-actions button {
    flex: 1;
    padding: 10px;
    border: none;
    border-radius: 24px;
    font-size: 0.88rem;
    cursor: pointer;
    transition: all 0.2s;
  }
  .modal-cancel { background: #303558; color: #8896a8; }
  .modal-cancel:hover { background: #404868; }
  .modal-confirm { background: linear-gradient(135deg, #c8a868, #a888c8); color: #1a1d2e; font-weight: 600; }
  .modal-confirm:hover { filter: brightness(1.1); }
  .modal-tip { font-size: 0.75rem; color: #6a7a8e; margin-top: 8px; line-height: 1.5; }
""".lstrip()

new_content = content[:start_idx] + "\n" + new_css + "\n" + content[end_idx:]

with open("index.html", "w", encoding="utf-8") as f:
    f.write(new_content)

print("✅ Style block replaced successfully")

count = new_content.count("<style>")
count2 = new_content.count("</style>")
print(f"Style tags: {count} opening, {count2} closing")
