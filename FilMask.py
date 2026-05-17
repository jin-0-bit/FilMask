<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<title>FilMask · 消失的爱人</title>
<style>
* { margin: 0; padding: 0; box-sizing: border-box; -webkit-tap-highlight-color: transparent; user-select: none; }
body {
  font-family: -apple-system, "PingFang SC", "Microsoft YaHei", sans-serif;
  background: #000;
  color: #f5f0e8;
  overflow: hidden;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}

.phone {
  width: 100%;
  max-width: 420px;
  height: 100vh;
  max-height: 920px;
  background: #0a0a0f;
  position: relative;
  overflow: hidden;
  box-shadow: 0 0 60px rgba(212,115,74,0.15);
}

/* ===== 抖音背景 ===== */
.tiktok-feed { position: absolute; inset: 0; z-index: 1; }
.tiktok-video {
  position: absolute; inset: 0;
  background: #000;
  overflow: hidden;
}
.tiktok-feed-video{
  position: absolute; inset: 0;
  width: 100%; height: 100%;
  object-fit: cover;
  display: none;
  opacity: 0;
  transition: opacity 0.35s ease;
}
.tiktok-info { position: absolute; bottom: 100px; left: 16px; right: 80px; z-index: 2; }
.tiktok-username { font-size: 16px; font-weight: 600; margin-bottom: 8px; }
.tiktok-caption { font-size: 14px; opacity: 0.95; line-height: 1.5; }
.tiktok-tag { color: #d4734a; }
.tiktok-side { position: absolute; right: 12px; bottom: 130px; display: flex; flex-direction: column; gap: 18px; z-index: 3; }
.tiktok-side-btn { display: flex; flex-direction: column; align-items: center; font-size: 11px; opacity: 0.95; }
.tiktok-side-icon { width: 44px; height: 44px; border-radius: 50%; background: rgba(255,255,255,0.12); display: flex; align-items: center; justify-content: center; font-size: 22px; margin-bottom: 4px; }

/* ===== 卡片 ===== */
.filmask-container { position: absolute; inset: 30px 14px 75px 14px; z-index: 10; display: flex; align-items: center; justify-content: center; }
.filmask-container{
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.35s ease;
}
.filmask-container.shown{
  opacity: 1;
  pointer-events: auto;
}

.filmask-card {
  width: 100%; height: 100%;
  background: #0d0d12;
  border: 1px solid rgba(201,169,97,0.3);
  border-radius: 18px;
  overflow: hidden; position: relative;
  display: none !important;
  flex-direction: column;
  box-shadow: 0 20px 60px rgba(0,0,0,0.6), 0 0 40px rgba(212,115,74,0.1);
}
.filmask-card.active {
  display: flex !important;
  animation: cardIn 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}
.filmask-card.exit-left { animation: cardExitLeft 0.3s forwards; }
.filmask-card.exit-right { animation: cardExitRight 0.3s forwards; }
@keyframes cardIn { from { opacity: 0; transform: scale(0.92) translateY(20px); } to { opacity: 1; transform: scale(1) translateY(0); } }
@keyframes cardExitLeft { to { opacity: 0; transform: translateX(-100px) scale(0.9); } }
@keyframes cardExitRight { to { opacity: 0; transform: translateX(100px) scale(0.9); } }

.filmask-card::before {
  content: ''; position: absolute; inset: 0;
  background: 
    radial-gradient(ellipse at top right, rgba(212,115,74,0.1), transparent 50%),
    radial-gradient(ellipse at bottom left, rgba(201,169,97,0.05), transparent 50%);
  pointer-events: none;
}
.filmask-card::after {
  content: ''; position: absolute; inset: 0;
  background: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='100' height='100'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='3'/%3E%3C/filter%3E%3Crect width='100' height='100' filter='url(%23n)' opacity='0.04'/%3E%3C/svg%3E");
  pointer-events: none;
}

/* LOGO */
.card-header {
  display: flex; justify-content: space-between; align-items: center;
  padding: 16px 18px 12px;
  border-bottom: 1px solid rgba(201,169,97,0.2);
  position: relative; z-index: 2;
  flex-shrink: 0;
}
.logo-wrap { display: flex; align-items: center; gap: 10px; position: relative; }
.logo-icon {
  font-size: 22px;
  background: linear-gradient(135deg, #d4734a, #c9a961);
  -webkit-background-clip: text; background-clip: text;
  -webkit-text-fill-color: transparent;
  filter: drop-shadow(0 0 8px rgba(212,115,74,0.5));
}
.logo {
  font-family: 'Georgia', 'Times New Roman', serif;
  font-size: 22px; font-weight: 900; font-style: italic;
  letter-spacing: 1px;
  background: linear-gradient(135deg, #d4734a 0%, #e89968 50%, #c9a961 100%);
  -webkit-background-clip: text; background-clip: text;
  -webkit-text-fill-color: transparent;
  text-shadow: 0 0 20px rgba(212,115,74,0.3);
  position: relative;
}
.logo::after {
  content: ''; position: absolute; bottom: -3px; left: 0; right: 0;
  height: 1px;
  background: linear-gradient(90deg, transparent, #c9a961, transparent);
}
.logo-tag {
  font-family: 'Courier New', monospace;
  font-size: 8px; letter-spacing: 2px;
  color: rgba(201,169,97,0.6);
  margin-left: 4px; align-self: flex-end; margin-bottom: 4px;
}
.card-progress { display: flex; gap: 4px; }
.progress-dot { width: 18px; height: 2px; background: rgba(201,169,97,0.2); border-radius: 1px; transition: all 0.3s; }
.progress-dot.active { background: linear-gradient(90deg, #d4734a, #c9a961); box-shadow: 0 0 8px rgba(212,115,74,0.6); }

.card-body {
  flex: 1; overflow-y: auto;
  padding: 12px 18px;
  position: relative; z-index: 2;
}
.card-body::-webkit-scrollbar { display: none; }

/* ★★ 升级版：section-label 更大更亮更醒目 ★★ */
.section-label {
  font-family: 'Courier New', monospace;
  font-size: 13px;
  letter-spacing: 2.5px;
  color: #ffd88a;
  margin-bottom: 10px;
  opacity: 1;
  font-weight: 700;
  text-shadow: 0 0 12px rgba(255, 216, 138, 0.4);
  display: flex;
  align-items: center;
  gap: 6px;
}

.divider {
  height: 1px;
  background: linear-gradient(90deg, transparent, rgba(201,169,97,0.3), transparent);
  margin: 14px 0;
}

/* 卡片1：骚话标题 */
.hook-title {
  font-size: 15px;
  font-weight: 700;
  text-align: center;
  margin: 0 auto 14px;
  line-height: 1.4;
  letter-spacing: 0.5px;
  background: linear-gradient(135deg, #f5f0e8 0%, #d4734a 50%, #c9a961 100%);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  text-shadow: 0 0 20px rgba(212,115,74,0.2);
  padding: 8px 28px;
  position: relative;
  display: block;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.hook-title::before, .hook-title::after {
  content: '✦';
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  color: #d4734a;
  font-size: 11px;
  opacity: 0.7;
  -webkit-text-fill-color: #d4734a;
}
.hook-title::before { left: 4px; }
.hook-title::after { right: 4px; }

.character-image-box {
  width: 75%;
  max-width: 240px;
  aspect-ratio: 4/5;
  margin: 0 auto 14px;
  background: linear-gradient(135deg, #1a1015, #2a1a20);
  border: 1px solid rgba(201,169,97,0.3);
  border-radius: 8px;
  position: relative; overflow: hidden;
  display: flex; align-items: center; justify-content: center;
  box-shadow: 0 8px 24px rgba(0,0,0,0.4);
}
.character-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  transform: scale(1.02);
}
.character-image-placeholder {
  font-family: 'Courier New', monospace;
  font-size: 11px; color: rgba(201,169,97,0.4);
  letter-spacing: 2px; text-align: center;
}
.character-image-corner {
  position: absolute; width: 18px; height: 18px;
  border: 1px solid rgba(201,169,97,0.6);
}
.character-image-corner.tl { top: 6px; left: 6px; border-right: none; border-bottom: none; }
.character-image-corner.tr { top: 6px; right: 6px; border-left: none; border-bottom: none; }
.character-image-corner.bl { bottom: 6px; left: 6px; border-right: none; border-top: none; }
.character-image-corner.br { bottom: 6px; right: 6px; border-left: none; border-top: none; }

.character-monologue {
  padding: 12px 14px;
  background: linear-gradient(135deg, rgba(212,115,74,0.06), rgba(201,169,97,0.04));
  border-left: 3px solid #d4734a;
  border-radius: 6px;
  margin-bottom: 10px;
  position: relative;
}
.monologue-mark {
  position: absolute; top: -4px; left: 10px;
  font-size: 28px; color: #d4734a;
  opacity: 0.4; font-family: Georgia, serif; line-height: 1;
}
.monologue-text {
  font-size: 12.5px;
  line-height: 1.7;
  color: rgba(245,240,232,0.92);
  font-style: italic;
  padding-left: 6px;
}
.character-source {
  font-family: 'Courier New', monospace;
  font-size: 11px;
  color: rgba(201,169,97,0.75);
  letter-spacing: 1.5px;
  text-align: right;
  padding-right: 4px;
  margin-bottom: 10px;
}
.character-source::before { content: '— '; color: #c9a961; }
.character-source strong { color: #d4734a; font-weight: 600; }

.guess-row {
  text-align: center;
  padding: 8px;
  background: rgba(0,0,0,0.2);
  border-radius: 6px;
  border: 1px dashed rgba(201,169,97,0.2);
}
.guess-question { font-size: 12px; color: #f5f0e8; margin-bottom: 3px; }
.guess-hint {
  font-size: 9px; color: rgba(201,169,97,0.6);
  font-family: 'Courier New', monospace; letter-spacing: 1px;
}

.card-footer {
  padding: 12px 18px 16px;
  display: flex; gap: 10px;
  position: relative; z-index: 2;
  border-top: 1px solid rgba(201,169,97,0.1);
  flex-shrink: 0;
}
.btn {
  flex: 1; padding: 12px;
  border: none; border-radius: 8px;
  font-size: 13px; font-weight: 600;
  cursor: pointer; font-family: inherit;
  letter-spacing: 1px; transition: all 0.2s;
}
.btn:active { transform: scale(0.96); }
.btn-yes { background: linear-gradient(135deg, #d4734a, #b8593a); color: #fff; box-shadow: 0 4px 12px rgba(212,115,74,0.3); }
.btn-no { background: rgba(201,169,97,0.1); color: #c9a961; border: 1px solid rgba(201,169,97,0.3); }

/* 卡片2 */
.story-section { display: flex; gap: 12px; margin-bottom: 14px; }
.story-poster {
  width: 90px; height: 130px;
  background: linear-gradient(135deg, #1a1015, #2a1a20);
  border: 1px solid rgba(201,169,97,0.2);
  border-radius: 4px; flex-shrink: 0;
  display: flex; align-items: center; justify-content: center;
  font-family: 'Courier New', monospace;
  font-size: 9px; color: rgba(201,169,97,0.4);
  letter-spacing: 1px; text-align: center;
  overflow: hidden;
}
.story-poster img { width: 100%; height: 100%; object-fit: cover; display: block; }
.story-text { flex: 1; min-width: 0; }
.story-title { font-size: 18px; font-weight: 700; color: #f5f0e8; margin-bottom: 4px; line-height: 1.3; }
.story-meta { font-size: 10px; color: #c9a961; font-family: 'Courier New', monospace; letter-spacing: 1px; margin-bottom: 8px; }
.story-summary { font-size: 12px; line-height: 1.6; color: rgba(245,240,232,0.85); }

.trailer-label {
  font-family: 'Courier New', monospace;
  font-size: 13px; letter-spacing: 2.5px;
  color: #ffd88a; margin-bottom: 10px;
  font-weight: 700;
  text-shadow: 0 0 12px rgba(255, 216, 138, 0.4);
  display: flex; justify-content: space-between; align-items: center;
}
.trailer-label span:last-child { font-size: 10px; opacity: 0.7; }
.trailer-video-box {
  width: 100%; aspect-ratio: 16/9;
  background: linear-gradient(135deg, #1a1015, #2a1a20);
  border: 1px solid rgba(201,169,97,0.2);
  border-radius: 8px; position: relative;
  display: flex; align-items: center; justify-content: center;
  margin-bottom: 10px; cursor: pointer; overflow: hidden;
}
.trailer-video-el{
  position: absolute; inset: 0;
  width: 100%; height: 100%;
  object-fit: cover;
  opacity: 0.92;
}
.trailer-video-box.playing .trailer-play,
.trailer-video-box.playing .trailer-duration { opacity: 0; transform: scale(0.9); }
.trailer-play, .trailer-duration { transition: all 0.2s; }
.trailer-play {
  width: 50px; height: 50px; border-radius: 50%;
  background: rgba(212,115,74,0.9);
  display: flex; align-items: center; justify-content: center;
  color: #fff; font-size: 18px;
  box-shadow: 0 4px 20px rgba(212,115,74,0.5);
}
.trailer-duration {
  position: absolute; bottom: 8px; right: 8px;
  background: rgba(0,0,0,0.7); color: #fff;
  padding: 2px 6px; border-radius: 3px;
  font-size: 10px; font-family: 'Courier New', monospace;
}
.trailer-corner { position: absolute; width: 16px; height: 16px; border: 1px solid rgba(201,169,97,0.5); }
.trailer-corner.tl { top: 6px; left: 6px; border-right: none; border-bottom: none; }
.trailer-corner.tr { top: 6px; right: 6px; border-left: none; border-bottom: none; }
.trailer-corner.bl { bottom: 6px; left: 6px; border-right: none; border-top: none; }
.trailer-corner.br { bottom: 6px; right: 6px; border-left: none; border-top: none; }
.trailer-cta {
  font-size: 11px; color: rgba(201,169,97,0.7);
  text-align: center;
  font-family: 'Courier New', monospace;
  letter-spacing: 1px; margin-bottom: 14px;
}
.theater-btn {
  width: 100%; padding: 14px;
  background: linear-gradient(135deg, rgba(212,115,74,0.15), rgba(201,169,97,0.1));
  border: 1px solid rgba(212,115,74,0.4);
  border-radius: 10px; color: #f5f0e8;
  cursor: pointer; display: flex;
  align-items: center; justify-content: space-between;
  font-family: inherit; transition: all 0.2s;
}
.theater-btn:active { transform: scale(0.98); background: rgba(212,115,74,0.25); }
.theater-btn-left { display: flex; align-items: center; gap: 12px; }
.theater-icon {
  width: 36px; height: 36px; border-radius: 8px;
  background: linear-gradient(135deg, #d4734a, #c9a961);
  display: flex; align-items: center; justify-content: center;
  font-size: 18px;
}
.theater-text { text-align: left; }
.theater-name { font-size: 13px; font-weight: 700; color: #f5f0e8; margin-bottom: 2px; }
.theater-desc { font-size: 10px; color: rgba(201,169,97,0.8); font-family: 'Courier New', monospace; letter-spacing: 1px; }
.theater-arrow { font-size: 20px; color: #d4734a; }

/* 卡片3 */
.derivative-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin-bottom: 16px; }
.derivative-item {
  aspect-ratio: 1;
  background: linear-gradient(135deg, #1a1015, #2a1a20);
  border: 1px solid rgba(201,169,97,0.2);
  border-radius: 6px; position: relative;
  display: flex; flex-direction: column; justify-content: flex-end;
  padding: 8px; overflow: hidden;
  cursor: pointer; transition: all 0.2s;
}
.derivative-item:active { transform: scale(0.97); }
.derivative-thumb {
  position: absolute; inset: 0;
  display: flex; align-items: center; justify-content: center;
  font-family: 'Courier New', monospace;
  font-size: 9px; color: rgba(201,169,97,0.3);
  letter-spacing: 1px;
}
.derivative-video-el{
  position: absolute; inset: 0;
  width: 100%; height: 100%;
  object-fit: cover;
  display: block;
  opacity: 0.9;
  filter: contrast(1.05) saturate(1.05);
}
.derivative-overlay {
  position: absolute; inset: 0;
  background: linear-gradient(to top, rgba(0,0,0,0.85) 0%, transparent 50%);
}
.derivative-tag {
  position: absolute; top: 6px; left: 6px;
  background: rgba(212,115,74,0.9); color: #fff;
  font-size: 9px; padding: 2px 6px; border-radius: 2px;
  font-family: 'Courier New', monospace;
  letter-spacing: 1px; z-index: 2;
}
.derivative-title { position: relative; z-index: 2; font-size: 11px; line-height: 1.4; color: #f5f0e8; font-weight: 500; }
.derivative-views { position: relative; z-index: 2; font-size: 9px; color: #c9a961; font-family: 'Courier New', monospace; margin-top: 2px; }

.review-prompt {
  padding: 14px;
  background: rgba(201,169,97,0.05);
  border: 1px solid rgba(201,169,97,0.2);
  border-radius: 8px;
}
.review-question { font-size: 14px; color: #f5f0e8; margin-bottom: 12px; text-align: center; line-height: 1.6; }
.review-question strong { color: #d4734a; }
.review-buttons { display: flex; gap: 10px; }
.review-btn {
  flex: 1; padding: 12px;
  border-radius: 6px; font-size: 13px;
  font-weight: 600; cursor: pointer;
  border: 1px solid; background: transparent;
  color: #f5f0e8; font-family: inherit;
  transition: all 0.2s;
}
/* 投票按钮：白框更醒目 */
.review-btn.forgive,
.review-btn.no-forgive{
  border: 2px solid transparent;
  color: #f5f0e8;
  background: rgba(255,255,255,0.04);
  box-shadow: 0 0 18px rgba(0,0,0,0.22);
}
.review-btn.forgive:active,
.review-btn.no-forgive:active { background: rgba(255,255,255,0.16); transform: scale(0.96); }

/* 主题色系：提高明度但不突兀 */
.review-btn.forgive{
  border-color: rgba(255, 216, 138, 0.9);
  color: #ffe7b0;
  background: linear-gradient(135deg, rgba(201,169,97,0.22), rgba(201,169,97,0.08));
  box-shadow: 0 0 18px rgba(201,169,97,0.16);
}
.review-btn.no-forgive{
  border-color: rgba(255, 150, 110, 0.92);
  color: #ffd1bf;
  background: linear-gradient(135deg, rgba(212,115,74,0.24), rgba(212,115,74,0.08));
  box-shadow: 0 0 18px rgba(212,115,74,0.18);
}
.review-btn.forgive:hover,
.review-btn.no-forgive:hover{
  filter: brightness(1.05);
}
.review-btn.forgive:active,
.review-btn.no-forgive:active{
  background: rgba(0,0,0,0.12);
}
.review-stats {
  display: flex; justify-content: space-around;
  margin-top: 10px; font-size: 10px;
  color: rgba(201,169,97,0.6);
  font-family: 'Courier New', monospace;
}

/* ★ 新增：投票下方的全网提示 ★ */
.vote-hint {
  text-align: center;
  margin-top: 14px;
  padding: 10px 14px;
  font-size: 13px;
  font-weight: 700;
  color: #ffd88a;
  letter-spacing: 1px;
  text-shadow: 0 0 12px rgba(255, 216, 138, 0.5);
  animation: voteHintPulse 2s ease-in-out infinite;
}
.vote-hint::before { content: '🔥 '; }
.vote-hint::after { content: ' 🔥'; }
@keyframes voteHintPulse {
  0%, 100% { transform: scale(1); opacity: 0.95; }
  50% { transform: scale(1.03); opacity: 1; }
}

/* 评论页 */
#card3-f .card-body,
#card3-nf .card-body {
  display: flex;
  flex-direction: column;
  padding-bottom: 12px;
}

.camp-header {
  padding: 12px 14px;
  background: linear-gradient(135deg, rgba(212,115,74,0.1), rgba(201,169,97,0.05));
  border: 1px solid rgba(212,115,74,0.3);
  border-radius: 10px;
  margin-bottom: 12px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-shrink: 0;
}
.camp-info { display: flex; flex-direction: column; gap: 3px; }
.camp-label { font-family: 'Courier New', monospace; font-size: 10px; letter-spacing: 2px; color: rgba(201,169,97,0.7); }
.camp-name { font-size: 15px; font-weight: 700; color: #d4734a; }
.camp-count { font-size: 10px; color: #c9a961; font-family: 'Courier New', monospace; }
.camp-switch-btn {
  padding: 8px 12px;
  background: rgba(0,0,0,0.4);
  border: 1px solid rgba(201,169,97,0.4);
  border-radius: 6px;
  color: #c9a961;
  font-size: 11px;
  cursor: pointer;
  font-family: inherit;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 2px;
  flex-shrink: 0;
}
.camp-switch-btn:active { background: rgba(201,169,97,0.2); }
.switch-label { font-family: 'Courier New', monospace; font-size: 8px; letter-spacing: 1px; opacity: 0.7; }

.comments-area {
  background: rgba(0,0,0,0.3);
  border: 1px solid rgba(201,169,97,0.15);
  border-radius: 8px;
  padding: 8px 12px;
  flex: 1;
  overflow-y: auto;
  min-height: 0;
}
.comments-area::-webkit-scrollbar { display: none; }
.comment-item {
  display: flex; gap: 10px;
  padding: 10px 0;
  border-bottom: 1px dashed rgba(201,169,97,0.1);
  position: relative;
}
.comment-item:last-child { border-bottom: none; }
.comment-avatar {
  width: 32px; height: 32px;
  border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  font-size: 12px; font-weight: 700;
  color: #fff; flex-shrink: 0;
}
.avatar-f { background: linear-gradient(135deg, #c9a961, #a08a4a); }
.avatar-nf { background: linear-gradient(135deg, #d4734a, #b8593a); }
.comment-content { flex: 1; min-width: 0; padding-right: 50px; }
.comment-name { font-size: 11px; color: #c9a961; margin-bottom: 4px; display: flex; align-items: center; gap: 6px; }
.comment-time { font-size: 9px; color: rgba(201,169,97,0.5); font-family: 'Courier New', monospace; }
.comment-text { font-size: 13px; line-height: 1.6; color: rgba(245,240,232,0.9); }
.comment-like-btn {
  position: absolute; bottom: 10px; right: 0;
  display: flex; flex-direction: column; align-items: center; gap: 2px;
  cursor: pointer; padding: 4px 6px; border-radius: 6px;
  transition: all 0.2s; background: transparent; border: none; font-family: inherit;
}
.comment-like-btn:active { transform: scale(0.9); }
.comment-like-icon {
  font-size: 16px; color: rgba(201,169,97,0.6);
  transition: all 0.3s; line-height: 1;
}
.comment-like-btn.liked .comment-like-icon {
  color: #d4734a; transform: scale(1.15);
  text-shadow: 0 0 8px rgba(212,115,74,0.6);
}
.comment-like-count { font-size: 10px; color: rgba(201,169,97,0.7); font-family: 'Courier New', monospace; font-weight: 600; }
.comment-like-btn.liked .comment-like-count { color: #d4734a; }

.comment-input-bar {
  display: flex; gap: 8px;
  padding: 10px 18px;
  background: rgba(13,13,18,0.95);
  border-top: 1px solid rgba(201,169,97,0.15);
  position: relative; z-index: 2;
  flex-shrink: 0;
}
.comment-input-bar input {
  flex: 1; padding: 10px 14px;
  background: rgba(0,0,0,0.4);
  border: 1px solid rgba(201,169,97,0.2);
  border-radius: 20px;
  color: #f5f0e8; font-size: 12px;
  font-family: inherit; outline: none;
}
.comment-input-bar input:focus { border-color: rgba(212,115,74,0.5); }
.comment-input-bar input::placeholder { color: rgba(245,240,232,0.4); }
.comment-input-bar button {
  padding: 10px 18px;
  background: linear-gradient(135deg, #d4734a, #b8593a);
  border: none; border-radius: 20px;
  color: #fff; font-size: 12px;
  font-weight: 600; cursor: pointer;
  font-family: inherit; transition: all 0.2s;
}
.comment-input-bar button:active { transform: scale(0.95); }

/* 卡片4 */
.cinema-map-box {
  width: 100%; aspect-ratio: 16/9;
  background: linear-gradient(135deg, #1a1015, #2a1a20);
  border: 1px solid rgba(201,169,97,0.2);
  border-radius: 8px; position: relative;
  display: flex; align-items: center; justify-content: center;
  margin-bottom: 14px; overflow: hidden;
}
.cinema-map-box img{
  position: absolute; inset: 0;
  width: 100%; height: 100%;
  object-fit: cover;
  display: block;
}
.cinema-map-grid {
  position: absolute; inset: 0;
  background-image:
    linear-gradient(rgba(201,169,97,0.08) 1px, transparent 1px),
    linear-gradient(90deg, rgba(201,169,97,0.08) 1px, transparent 1px);
  background-size: 30px 30px;
}
.cinema-pin {
  position: absolute; width: 10px; height: 10px; border-radius: 50%;
  background: #d4734a;
  box-shadow: 0 0 12px rgba(212,115,74,0.8);
  animation: pinPulse 2s infinite;
}
.cinema-pin.p1 { top: 30%; left: 25%; }
.cinema-pin.p2 { top: 50%; left: 60%; }
.cinema-pin.p3 { top: 70%; left: 40%; }
.cinema-pin.you {
  background: #c9a961; width: 14px; height: 14px;
  top: 50%; left: 50%; transform: translate(-50%, -50%);
}
.cinema-pin.you::after {
  content: ''; position: absolute; inset: -8px;
  border: 1px dashed rgba(201,169,97,0.5); border-radius: 50%;
  animation: pinExpand 2s infinite;
}
@keyframes pinPulse { 0%, 100% { transform: scale(1); opacity: 1; } 50% { transform: scale(1.3); opacity: 0.7; } }
@keyframes pinExpand { 0% { transform: scale(1); opacity: 0.8; } 100% { transform: scale(2.5); opacity: 0; } }
.cinema-map-label {
  position: absolute; top: 8px; left: 8px;
  font-family: 'Courier New', monospace;
  font-size: 9px; color: rgba(201,169,97,0.7);
  letter-spacing: 2px; z-index: 2;
}
.cinema-movie-info {
  display: flex; gap: 12px;
  margin-bottom: 14px; padding: 10px;
  background: rgba(201,169,97,0.04);
  border-radius: 8px;
}
.cinema-movie-poster {
  width: 60px; height: 84px;
  background: linear-gradient(135deg, #1a1015, #2a1a20);
  border: 1px solid rgba(201,169,97,0.2);
  border-radius: 4px; flex-shrink: 0;
  display: flex; align-items: center; justify-content: center;
  font-family: 'Courier New', monospace;
  font-size: 8px; color: rgba(201,169,97,0.4);
  overflow: hidden;
}
.cinema-movie-poster img { width: 100%; height: 100%; object-fit: cover; display: block; }
.cinema-movie-text { flex: 1; display: flex; flex-direction: column; justify-content: center; gap: 4px; }
.cinema-movie-title { font-size: 16px; font-weight: 700; color: #f5f0e8; }
.cinema-movie-meta { font-size: 10px; color: #c9a961; font-family: 'Courier New', monospace; }
.cinema-rating { font-size: 12px; color: #d4734a; font-weight: 600; }
.showtime-list { display: flex; flex-direction: column; gap: 8px; }
.showtime {
  display: flex; justify-content: space-between; align-items: center;
  padding: 10px 12px;
  background: rgba(255,255,255,0.03);
  border: 1px solid rgba(201,169,97,0.15);
  border-radius: 8px;
  cursor: pointer; transition: all 0.2s;
}
.showtime:active { transform: scale(0.98); background: rgba(212,115,74,0.1); }
.st-l { display: flex; flex-direction: column; gap: 3px; }
.st-cinema-name { font-size: 13px; font-weight: 600; color: #f5f0e8; }
.st-info { font-size: 10px; color: rgba(201,169,97,0.7); font-family: 'Courier New', monospace; letter-spacing: 1px; }
.st-r { text-align: right; display: flex; flex-direction: column; gap: 3px; }
.st-time-label { font-size: 13px; font-weight: 700; color: #d4734a; font-family: 'Courier New', monospace; }
.st-price-label { font-size: 11px; color: #c9a961; }
.st-tag {
  display: inline-block; font-size: 9px; padding: 1px 4px;
  background: rgba(212,115,74,0.2); color: #d4734a; border-radius: 2px;
  font-family: 'Courier New', monospace;
}
.tuangou-hint {
  margin-top: 12px; padding: 10px;
  background: linear-gradient(135deg, rgba(212,115,74,0.1), rgba(201,169,97,0.05));
  border: 1px dashed rgba(212,115,74,0.3);
  border-radius: 6px; text-align: center;
  font-size: 11px; color: #d4734a;
  font-family: 'Courier New', monospace; letter-spacing: 1px;
}

/* 卡片5 */
.recommend-section { margin-bottom: 16px; }
.recommend-title {
  font-family: 'Courier New', monospace;
  font-size: 11px; letter-spacing: 3px;
  color: #c9a961; margin-bottom: 10px;
  display: flex; align-items: center; gap: 8px;
  padding-bottom: 6px;
  border-bottom: 1px solid rgba(201,169,97,0.2);
}
/* 卡片5标题：加亮加粗 */
.recommend-title{
  font-size: 12px;
  font-weight: 800;
  color: #ffd88a;
  text-shadow: 0 0 12px rgba(255,216,138,0.35);
  border-bottom-color: rgba(255,216,138,0.35);
}
.recommend-title::before { content: '◇'; color: #d4734a; }
.recommend-list { display: flex; flex-direction: column; gap: 12px; }
.recommend-item {
  display: flex; gap: 12px;
  padding: 12px;
  background: rgba(255,255,255,0.03);
  border: 1px solid rgba(201,169,97,0.15);
  border-radius: 10px;
  cursor: pointer; transition: all 0.2s;
  position: relative; overflow: hidden;
}
.recommend-item:active { transform: scale(0.98); background: rgba(201,169,97,0.08); }
.recommend-poster {
  width: 70px; height: 100px;
  background: linear-gradient(135deg, #1a1015, #2a1a20);
  border: 1px solid rgba(201,169,97,0.2);
  border-radius: 4px; flex-shrink: 0;
  display: flex; align-items: center; justify-content: center;
  font-family: 'Courier New', monospace;
  font-size: 8px; color: rgba(201,169,97,0.4);
  overflow: hidden;
}
.recommend-poster img { width: 100%; height: 100%; object-fit: cover; display: block; }
.recommend-info { flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 4px; }
.recommend-top { display: flex; justify-content: space-between; align-items: flex-start; }
.recommend-name { font-size: 14px; font-weight: 700; color: #f5f0e8; }
.recommend-match { font-family: 'Courier New', monospace; font-size: 10px; color: #d4734a; font-weight: 700; white-space: nowrap; }
.recommend-meta { font-size: 10px; color: rgba(201,169,97,0.7); font-family: 'Courier New', monospace; }
.recommend-rating { font-size: 11px; color: #c9a961; font-weight: 600; }
.match-bar {
  height: 4px; background: rgba(201,169,97,0.15);
  border-radius: 2px; overflow: hidden; margin-top: 4px;
}
.match-bar-fill {
  height: 100%;
  background: linear-gradient(90deg, #d4734a, #c9a961);
  border-radius: 2px;
  box-shadow: 0 0 6px rgba(212,115,74,0.5);
}
.recommend-reason {
  font-size: 11px; color: rgba(245,240,232,0.8);
  line-height: 1.5; font-style: italic;
  padding: 6px 8px;
  background: rgba(212,115,74,0.06);
  border-left: 2px solid rgba(212,115,74,0.4);
  border-radius: 3px; margin-top: 4px;
}
.recommend-reason::before { content: '◈ '; color: #d4734a; font-style: normal; }

/* 导航 */
.swipe-indicator {
  position: absolute; bottom: 20px; left: 50%;
  transform: translateX(-50%);
  display: flex; gap: 6px; z-index: 20;
  background: rgba(0,0,0,0.5);
  padding: 6px 12px; border-radius: 20px;
  backdrop-filter: blur(10px);
  border: 1px solid rgba(201,169,97,0.2);
}
.swipe-dot { width: 6px; height: 6px; border-radius: 50%; background: rgba(201,169,97,0.3); transition: all 0.3s; }
.swipe-dot.active { background: #d4734a; width: 18px; border-radius: 3px; }
.nav-arrow {
  position: absolute; top: 50%; transform: translateY(-50%);
  width: 36px; height: 36px; border-radius: 50%;
  background: rgba(0,0,0,0.6);
  border: 1px solid rgba(201,169,97,0.3);
  color: #c9a961;
  display: flex; align-items: center; justify-content: center;
  font-size: 18px; cursor: pointer;
  z-index: 15; backdrop-filter: blur(8px);
  opacity: 0.7; transition: all 0.2s;
}
.nav-arrow:hover { opacity: 1; }
.nav-arrow:active { transform: translateY(-50%) scale(0.9); }
.nav-arrow.left { left: 20px; }
.nav-arrow.right { right: 20px; }
.nav-arrow.disabled { opacity: 0.2; pointer-events: none; }

/* Toast & Modal */
.toast {
  position: fixed; top: 50%; left: 50%;
  transform: translate(-50%, -50%) scale(0.8);
  background: rgba(13,13,18,0.95); color: #f5f0e8;
  padding: 14px 24px; border-radius: 10px;
  font-size: 13px; font-weight: 500;
  opacity: 0; pointer-events: none;
  z-index: 200; transition: all 0.3s;
  border: 1px solid rgba(201,169,97,0.4);
  max-width: 80%; text-align: center;
  box-shadow: 0 10px 40px rgba(0,0,0,0.5);
}
.toast.show { opacity: 1; transform: translate(-50%, -50%) scale(1); }
.modal {
  position: fixed; inset: 0;
  background: rgba(0,0,0,0.85);
  z-index: 250; display: none;
  justify-content: center; align-items: center;
  padding: 30px; backdrop-filter: blur(8px);
}
.modal.active { display: flex; }
.modal-card {
  width: 100%; max-width: 340px;
  background: linear-gradient(180deg, #1a1015, #0d0d12);
  border: 1px solid rgba(212,115,74,0.4);
  border-radius: 16px;
  padding: 24px 20px;
  text-align: center;
  animation: modalIn 0.3s;
  box-shadow: 0 20px 60px rgba(0,0,0,0.8);
}
@keyframes modalIn { from { opacity: 0; transform: scale(0.9); } to { opacity: 1; transform: scale(1); } }
.modal-icon { font-size: 36px; margin-bottom: 12px; }
.modal-title { font-size: 16px; font-weight: 700; color: #f5f0e8; margin-bottom: 10px; }
.modal-desc { font-size: 12px; color: rgba(245,240,232,0.8); line-height: 1.7; margin-bottom: 20px; }
.modal-tip {
  font-size: 11px; color: #c9a961;
  background: rgba(201,169,97,0.08);
  padding: 8px 12px; border-radius: 6px;
  margin-bottom: 20px; border: 1px dashed rgba(201,169,97,0.3);
}
.modal-actions { display: flex; gap: 8px; }
.modal-btn { flex: 1; padding: 12px; border: none; border-radius: 8px; font-size: 12px; font-weight: 600; cursor: pointer; font-family: inherit; }
.modal-btn.primary { background: linear-gradient(135deg, #d4734a, #b8593a); color: #fff; }
.modal-btn.secondary { background: rgba(201,169,97,0.15); color: #c9a961; border: 1px solid rgba(201,169,97,0.3); }

/* 调试 */
.debug-switch { position: fixed; top: 20px; left: 20px; z-index: 999; display: flex; flex-direction: column; gap: 6px; }
.debug-btn {
  padding: 6px 10px;
  background: rgba(13,13,18,0.9);
  color: #c9a961;
  border: 1px solid rgba(201,169,97,0.4);
  border-radius: 6px;
  font-size: 10px; cursor: pointer;
  font-family: 'Courier New', monospace; letter-spacing: 1px;
}
.debug-btn:hover { background: rgba(212,115,74,0.3); }
.debug-btn.active { background: rgba(212,115,74,0.5); border-color: #d4734a; }
</style>
</head>
<body>

<div class="debug-switch">
  <button class="debug-btn active" onclick="goToCard(1)">CARD 1</button>
  <button class="debug-btn" onclick="goToCard(2)">CARD 2</button>
  <button class="debug-btn" onclick="goToCard(3)">CARD 3</button>
  <button class="debug-btn" onclick="goToCard('3-f')">3-该留</button>
  <button class="debug-btn" onclick="goToCard('3-nf')">3-该走</button>
  <button class="debug-btn" onclick="goToCard(4)">CARD 4</button>
  <button class="debug-btn" onclick="goToCard(5)">CARD 5</button>
</div>

<div class="phone">
  
  <div class="tiktok-feed">
    <div class="tiktok-video">
      <!-- 刷入/刷出视频层：自动播放两条刷入视频，结束后弹出卡片；关闭卡片后播放刷出视频 -->
      <video class="tiktok-feed-video" id="feedVideo" muted playsinline preload="metadata"></video>
    </div>
    <div class="tiktok-info">
      <div class="tiktok-username">@悬疑电影社</div>
      <div class="tiktok-caption">
        《消失的爱人》Amy 那段独白把我看傻了 😨<br>
        <span class="tiktok-tag">#消失的爱人 #GoneGirl</span>
      </div>
    </div>
    <div class="tiktok-side">
      <div class="tiktok-side-btn"><div class="tiktok-side-icon">❤️</div>82.4w</div>
      <div class="tiktok-side-btn"><div class="tiktok-side-icon">💬</div>5.6w</div>
      <div class="tiktok-side-btn"><div class="tiktok-side-icon">⭐</div>收藏</div>
      <div class="tiktok-side-btn"><div class="tiktok-side-icon">↗</div>分享</div>
    </div>
  </div>

  <div class="filmask-container">
    
    <!-- ============ 卡片1 ============ -->
    <div class="filmask-card active" id="card1">
      <div class="card-header">
        <div class="logo-wrap">
          <span class="logo-icon">◈</span>
          <span class="logo">FilMask</span>
          <span class="logo-tag">CINEMA</span>
        </div>
        <div class="card-progress">
          <div class="progress-dot active"></div>
          <div class="progress-dot"></div>
          <div class="progress-dot"></div>
          <div class="progress-dot"></div>
          <div class="progress-dot"></div>
        </div>
      </div>

      <div class="card-body">
        <div class="section-label">CHARACTER MASK · 直接代入</div>
        
        <div class="hook-title">这场失踪，是她写给老公的"情书"</div>
        
        <div class="character-image-box">
          <div class="character-image-corner tl"></div>
          <div class="character-image-corner tr"></div>
          <div class="character-image-corner bl"></div>
          <div class="character-image-corner br"></div>
          <img class="character-image" src="assets/img/amy.jpg" alt="Amy Dunne 角色图">
        </div>

        <div class="character-monologue">
          <div class="monologue-mark">"</div>
          <div class="monologue-text">
            我是 Amy Dunne。完美的妻子、完美的女儿、完美的「Amazing Amy」。直到那天清晨我消失了——警察以为我死了，邻居以为他杀了我，全美国都在为我哭泣。但你知道吗，亲爱的——这一切，都是我亲手写好的剧本。
          </div>
        </div>
        
        <div class="character-source">艾米·邓恩 · 出自《<strong>消失的爱人</strong>》(2014)</div>

        <div class="guess-row">
          <div class="guess-question">这部电影你看过吗？</div>
          <div class="guess-hint">YES · 看过 / NO · 没看过</div>
        </div>
      </div>

      <div class="card-footer">
        <button class="btn btn-no" onclick="answerCard1('no')">NO · 没看过</button>
        <button class="btn btn-yes" onclick="answerCard1('yes')">YES · 看过</button>
      </div>
    </div>

    <!-- ============ 卡片2 ============ -->
    <div class="filmask-card" id="card2">
      <div class="card-header">
        <div class="logo-wrap">
          <span class="logo-icon">◈</span>
          <span class="logo">FilMask</span>
          <span class="logo-tag">CINEMA</span>
        </div>
        <div class="card-progress">
          <div class="progress-dot"></div>
          <div class="progress-dot active"></div>
          <div class="progress-dot"></div>
          <div class="progress-dot"></div>
          <div class="progress-dot"></div>
        </div>
      </div>

      <div class="card-body">
        <div class="section-label">SYNOPSIS · 一分钟入戏</div>
        
        <div class="story-section">
          <div class="story-poster">
            <img src="assets/img/gone-girl-2.jpg" alt="消失的爱人 海报">
          </div>
          <div class="story-text">
            <div class="story-title">消失的爱人</div>
            <div class="story-meta">GONE GIRL · 2014</div>
            <div class="story-summary">
              结婚 5 周年纪念日清晨，Amy 突然失踪。客厅有打斗痕迹，丈夫 Nick 成为头号嫌犯，被全国媒体围剿。但随着调查深入，每一个"真相"背后，都藏着另一个更可怕的真相。
            </div>
          </div>
        </div>

        <div class="divider"></div>

        <div class="trailer-label">
          <span>OFFICIAL TRAILER · 官方宣传片</span>
          <span>02:30</span>
        </div>

        <div class="trailer-video-box" id="trailerBox" onclick="playTrailer(event)">
          <!-- 把你的宣传片视频放到：filmask/assets/video/trailer.mp4 -->
          <video class="trailer-video-el" id="trailerVideo" muted playsinline preload="metadata">
            <source src="assets/video/trailer.mp4" type="video/mp4">
          </video>
          <div class="trailer-corner tl"></div>
          <div class="trailer-corner tr"></div>
          <div class="trailer-corner bl"></div>
          <div class="trailer-corner br"></div>
          <div class="trailer-play">▶</div>
          <div class="trailer-duration">02:30</div>
        </div>

        <div class="trailer-cta">
          ▸ 看完宣传片，决定要不要走进影院
        </div>

        <button class="theater-btn" onclick="openTheaterModal()">
          <div class="theater-btn-left">
            <div class="theater-icon">🎬</div>
            <div class="theater-text">
              <div class="theater-name">抖音放映厅</div>
              <div class="theater-desc">▸ 在线观看完整版</div>
            </div>
          </div>
          <div class="theater-arrow">→</div>
        </button>
      </div>

      <div class="card-footer">
        <button class="btn btn-no" onclick="goToCard(1)">← 返回</button>
        <button class="btn btn-yes" onclick="goToCard(3)">下一页 →</button>
      </div>
    </div>

    <!-- ============ 卡片3 ============ -->
    <div class="filmask-card" id="card3">
      <div class="card-header">
        <div class="logo-wrap">
          <span class="logo-icon">◈</span>
          <span class="logo">FilMask</span>
          <span class="logo-tag">CINEMA</span>
        </div>
        <div class="card-progress">
          <div class="progress-dot"></div>
          <div class="progress-dot"></div>
          <div class="progress-dot active"></div>
          <div class="progress-dot"></div>
          <div class="progress-dot"></div>
        </div>
      </div>

      <div class="card-body">
        <div class="section-label">RELATED · 不好了 知识进脑子了</div>
        
        <div class="derivative-grid">
          <div class="derivative-item" onclick="showToast('▶ 进入「Amy 独白」频道')">
            <video class="derivative-video-el" muted autoplay loop playsinline preload="metadata">
              <source src="assets/video/derivative-1.mp4" type="video/mp4">
            </video>
            <div class="derivative-overlay"></div>
            <div class="derivative-tag">名场面</div>
            <div class="derivative-title">"Cool Girl" 独白完整解析</div>
            <div class="derivative-views">▸ 488w</div>
          </div>
          <div class="derivative-item" onclick="showToast('▶ 进入「叙事拆解」频道')">
            <video class="derivative-video-el" muted autoplay loop playsinline preload="metadata">
              <source src="assets/video/derivative-2.mp4" type="video/mp4">
            </video>
            <div class="derivative-overlay"></div>
            <div class="derivative-tag">叙事</div>
            <div class="derivative-title">芬奇导演如何用日记反转全片</div>
            <div class="derivative-views">▸ 267w</div>
          </div>
          <div class="derivative-item" onclick="showToast('▶ 进入「人物分析」频道')">
            <video class="derivative-video-el" muted autoplay loop playsinline preload="metadata">
              <source src="assets/video/derivative-3.mp4" type="video/mp4">
            </video>
            <div class="derivative-overlay"></div>
            <div class="derivative-tag">心理</div>
            <div class="derivative-title">Amy 到底是受害者还是反派</div>
            <div class="derivative-views">▸ 356w</div>
          </div>
          <div class="derivative-item" onclick="showToast('▶ 进入「原著对比」频道')">
            <video class="derivative-video-el" muted autoplay loop playsinline preload="metadata">
              <source src="assets/video/derivative-4.mp4" type="video/mp4">
            </video>
            <div class="derivative-overlay"></div>
            <div class="derivative-tag">原著</div>
            <div class="derivative-title">小说和电影的 7 处关键不同</div>
            <div class="derivative-views">▸ 142w</div>
          </div>
        </div>

        <div class="section-label">VOTE · 这局怎么破</div>

        <div class="review-prompt">
          <div class="review-question">
            如果你是 Nick，<strong>该走 还是 该留？</strong>
          </div>
          <div class="review-buttons">
            <button class="review-btn forgive" onclick="goToCard('3-f')">→ 该留</button>
            <button class="review-btn no-forgive" onclick="goToCard('3-nf')">→ 该走</button>
          </div>
          <div class="review-stats">
            <span>该留派 · 27%</span>
            <span>该走派 · 73%</span>
          </div>
        </div>

        <!-- ★ 新增：投票下方全网提示 ★ -->
        <div class="vote-hint">全网都在等你的选择！</div>
      </div>

      <div class="card-footer">
        <button class="btn btn-no" onclick="goToCard(2)">← 返回</button>
        <button class="btn btn-yes" onclick="goToCard(4)">跳过 · 看院线 →</button>
      </div>
    </div>

    <!-- ============ 卡片3-该留派 ============ -->
    <div class="filmask-card" id="card3-f">
      <div class="card-header">
        <div class="logo-wrap">
          <span class="logo-icon">◈</span>
          <span class="logo">FilMask</span>
          <span class="logo-tag">CINEMA</span>
        </div>
        <div class="card-progress">
          <div class="progress-dot"></div>
          <div class="progress-dot"></div>
          <div class="progress-dot active"></div>
          <div class="progress-dot"></div>
          <div class="progress-dot"></div>
        </div>
      </div>

      <div class="card-body">
        <div class="camp-header">
          <div class="camp-info">
            <div class="camp-label">YOU JOINED</div>
            <div class="camp-name">→ 该留派</div>
            <div class="camp-count">▸ 共 3,247 人在这里</div>
          </div>
          <button class="camp-switch-btn" onclick="goToCard('3-nf')">
            <span>看看对面 →</span>
            <span class="switch-label">SWITCH</span>
          </button>
        </div>

        <div class="comments-area">
          <div class="comment-item">
            <div class="comment-avatar avatar-f">D</div>
            <div class="comment-content">
              <div class="comment-name">@Dark_Mirror <span class="comment-time">2 分钟前</span></div>
              <div class="comment-text">这才是芬奇最狠的地方——他们就是天生一对的怪物。Nick 离开 Amy 后会发现自己再也找不到这种"完美的对手"了。</div>
            </div>
            <button class="comment-like-btn" onclick="toggleLike(this)">
              <span class="comment-like-icon">♥</span>
              <span class="comment-like-count">2847</span>
            </button>
          </div>
          <div class="comment-item">
            <div class="comment-avatar avatar-f">A</div>
            <div class="comment-content">
              <div class="comment-name">@AmazingAmy <span class="comment-time">5 分钟前</span></div>
              <div class="comment-text">他们的婚姻就是一面镜子，Nick 离开 Amy 就是承认自己也是个 loser。他离不开的不是 Amy，是那个被她"塑造"出来的自己。</div>
            </div>
            <button class="comment-like-btn" onclick="toggleLike(this)">
              <span class="comment-like-icon">♥</span>
              <span class="comment-like-count">1592</span>
            </button>
          </div>
          <div class="comment-item">
            <div class="comment-avatar avatar-f">N</div>
            <div class="comment-content">
              <div class="comment-name">@NickFincher <span class="comment-time">12 分钟前</span></div>
              <div class="comment-text">为了孩子也得留下。而且说真的，外面的世界看到了 Amy 的"演技"，Nick 走了反而失去所有筹码。</div>
            </div>
            <button class="comment-like-btn" onclick="toggleLike(this)">
              <span class="comment-like-icon">♥</span>
              <span class="comment-like-count">967</span>
            </button>
          </div>
          <div class="comment-item">
            <div class="comment-avatar avatar-f">P</div>
            <div class="comment-content">
              <div class="comment-name">@PerfectMatch <span class="comment-time">18 分钟前</span></div>
              <div class="comment-text">他们俩是真的"灵魂伴侣"——只是这个灵魂是阴暗的。这就是芬奇想说的：有些人就是注定要互相折磨一辈子。</div>
            </div>
            <button class="comment-like-btn" onclick="toggleLike(this)">
              <span class="comment-like-icon">♥</span>
              <span class="comment-like-count">734</span>
            </button>
          </div>
          <div class="comment-item">
            <div class="comment-avatar avatar-f">C</div>
            <div class="comment-content">
              <div class="comment-name">@CoolGirlClub <span class="comment-time">25 分钟前</span></div>
              <div class="comment-text">最后那个镜头 Nick 摸 Amy 头的瞬间——既厌恶又依恋，这才是芬奇电影最高级的部分。</div>
            </div>
            <button class="comment-like-btn" onclick="toggleLike(this)">
              <span class="comment-like-icon">♥</span>
              <span class="comment-like-count">512</span>
            </button>
          </div>
          <div class="comment-item">
            <div class="comment-avatar avatar-f">S</div>
            <div class="comment-content">
              <div class="comment-name">@StayForever <span class="comment-time">31 分钟前</span></div>
              <div class="comment-text">所有婚姻都是地狱，只不过他们俩的地狱更精彩一点。走了去哪儿呢，外面是另一个地狱。</div>
            </div>
            <button class="comment-like-btn" onclick="toggleLike(this)">
              <span class="comment-like-icon">♥</span>
              <span class="comment-like-count">389</span>
            </button>
          </div>
        </div>
      </div>

      <div class="comment-input-bar">
        <input type="text" placeholder="说说你为什么觉得该留...">
        <button onclick="showToast('✓ 已发表到「该留派」')">发送</button>
      </div>

      <div class="card-footer">
        <button class="btn btn-no" onclick="goToCard(3)">← 返回投票</button>
        <button class="btn btn-yes" onclick="goToCard(4)">下一页 →</button>
      </div>
    </div>

    <!-- ============ 卡片3-该走派 ============ -->
    <div class="filmask-card" id="card3-nf">
      <div class="card-header">
        <div class="logo-wrap">
          <span class="logo-icon">◈</span>
          <span class="logo">FilMask</span>
          <span class="logo-tag">CINEMA</span>
        </div>
        <div class="card-progress">
          <div class="progress-dot"></div>
          <div class="progress-dot"></div>
          <div class="progress-dot active"></div>
          <div class="progress-dot"></div>
          <div class="progress-dot"></div>
        </div>
      </div>

      <div class="card-body">
        <div class="camp-header">
          <div class="camp-info">
            <div class="camp-label">YOU JOINED</div>
            <div class="camp-name">→ 该走派</div>
            <div class="camp-count">▸ 共 8,927 人在这里</div>
          </div>
          <button class="camp-switch-btn" onclick="goToCard('3-f')">
            <span>看看对面 →</span>
            <span class="switch-label">SWITCH</span>
          </button>
        </div>

        <div class="comments-area">
          <div class="comment-item">
            <div class="comment-avatar avatar-nf">R</div>
            <div class="comment-content">
              <div class="comment-name">@RunNick <span class="comment-time">2 分钟前</span></div>
              <div class="comment-text">那个女人杀了三个人！为了控制你能编出一个孩子！跑！立刻跑！连夜跑！再不跑等着上头条吧 Nick！</div>
            </div>
            <button class="comment-like-btn" onclick="toggleLike(this)">
              <span class="comment-like-icon">♥</span>
              <span class="comment-like-count">5234</span>
            </button>
          </div>
          <div class="comment-item">
            <div class="comment-avatar avatar-nf">G</div>
            <div class="comment-content">
              <div class="comment-name">@GoneGirlSurvivor <span class="comment-time">5 分钟前</span></div>
              <div class="comment-text">没有任何关系比生命更重要。她下次心情不好就会再来一次"消失"——只不过这次轮到你"被"消失。</div>
            </div>
            <button class="comment-like-btn" onclick="toggleLike(this)">
              <span class="comment-like-icon">♥</span>
              <span class="comment-like-count">3127</span>
            </button>
          </div>
          <div class="comment-item">
            <div class="comment-avatar avatar-nf">W</div>
            <div class="comment-content">
              <div class="comment-name">@WakeUpNick <span class="comment-time">12 分钟前</span></div>
              <div class="comment-text">芬奇的结局之所以可怕，正是因为它真实——但作为观众我希望 Nick 有勇气逃。否则这就是一个无止境的噩梦。</div>
            </div>
            <button class="comment-like-btn" onclick="toggleLike(this)">
              <span class="comment-like-icon">♥</span>
              <span class="comment-like-count">1893</span>
            </button>
          </div>
          <div class="comment-item">
            <div class="comment-avatar avatar-nf">F</div>
            <div class="comment-content">
              <div class="comment-name">@FreedomFirst <span class="comment-time">18 分钟前</span></div>
              <div class="comment-text">为了"孩子"留下来的人，都是在用孩子绑架自己。这个孩子长大会变成第二个 Amy。</div>
            </div>
            <button class="comment-like-btn" onclick="toggleLike(this)">
              <span class="comment-like-icon">♥</span>
              <span class="comment-like-count">1456</span>
            </button>
          </div>
          <div class="comment-item">
            <div class="comment-avatar avatar-nf">B</div>
            <div class="comment-content">
              <div class="comment-name">@BreakTheCycle <span class="comment-time">25 分钟前</span></div>
              <div class="comment-text">所谓"互相折磨的灵魂伴侣"是一种病态浪漫化。Nick 留下来不是因为爱，是因为被驯化了。</div>
            </div>
            <button class="comment-like-btn" onclick="toggleLike(this)">
              <span class="comment-like-icon">♥</span>
              <span class="comment-like-count">892</span>
            </button>
          </div>
          <div class="comment-item">
            <div class="comment-avatar avatar-nf">E</div>
            <div class="comment-content">
              <div class="comment-name">@ExitDoor <span class="comment-time">35 分钟前</span></div>
              <div class="comment-text">坐牢都比和 Amy 一起生活强。至少坐牢有出狱的一天，跟 Amy 一辈子都不会有 ending。</div>
            </div>
            <button class="comment-like-btn" onclick="toggleLike(this)">
              <span class="comment-like-icon">♥</span>
              <span class="comment-like-count">623</span>
            </button>
          </div>
        </div>
      </div>

      <div class="comment-input-bar">
        <input type="text" placeholder="说说你为什么觉得该走...">
        <button onclick="showToast('✓ 已发表到「该走派」')">发送</button>
      </div>

      <div class="card-footer">
        <button class="btn btn-no" onclick="goToCard(3)">← 返回投票</button>
        <button class="btn btn-yes" onclick="goToCard(4)">下一页 →</button>
      </div>
    </div>

    <!-- ============ 卡片4 ============ -->
    <div class="filmask-card" id="card4">
      <div class="card-header">
        <div class="logo-wrap">
          <span class="logo-icon">◈</span>
          <span class="logo">FilMask</span>
          <span class="logo-tag">CINEMA</span>
        </div>
        <div class="card-progress">
          <div class="progress-dot"></div>
          <div class="progress-dot"></div>
          <div class="progress-dot"></div>
          <div class="progress-dot active"></div>
          <div class="progress-dot"></div>
        </div>
      </div>

      <div class="card-body">
        <div class="section-label">CINEMA · 别刷了，真的值得去看</div>
        
        <div class="cinema-map-box">
          <img src="assets/img/map.jpg" alt="附近影院地图">
        </div>

        <div class="cinema-movie-info">
          <div class="cinema-movie-poster">
            <img src="assets/img/gone-girl-2.jpg" alt="消失的爱人 海报">
          </div>
          <div class="cinema-movie-text">
            <div class="cinema-movie-title">消失的爱人</div>
            <div class="cinema-movie-meta">2014 · 10周年特别重映</div>
            <div class="cinema-rating">★ 豆瓣 8.7</div>
          </div>
        </div>

        <div class="section-label">SHOWTIMES · 今晚排片</div>

        <div class="showtime-list">
          <div class="showtime" onclick="showToast('已跳转抖音团购 · 出票')">
            <div class="st-l">
              <div class="st-cinema-name">胡桥影剧院</div>
              <div class="st-info">▸ 杜比影院 · 1.2km</div>
              <span class="st-tag">推荐</span>
            </div>
            <div class="st-r">
              <div class="st-time-label">19:30</div>
              <div class="st-price-label">¥88</div>
            </div>
          </div>
          <div class="showtime" onclick="showToast('已跳转抖音团购 · 出票')">
            <div class="st-l">
              <div class="st-cinema-name">SFC上影竞衡八八影城（金山店）</div>
              <div class="st-info">▸ IMAX · 2.8km</div>
            </div>
            <div class="st-r">
              <div class="st-time-label">20:15</div>
              <div class="st-price-label">¥118</div>
            </div>
          </div>
          <div class="showtime" onclick="showToast('已跳转抖音团购 · 出票')">
            <div class="st-l">
              <div class="st-cinema-name">UVC影城金山店</div>
              <div class="st-info">▸ 普通厅 · 3.5km</div>
            </div>
            <div class="st-r">
              <div class="st-time-label">21:00</div>
              <div class="st-price-label">¥68</div>
            </div>
          </div>
        </div>

        <div class="tuangou-hint">
          ◈ 点击场次直接进入抖音团购出票
        </div>
      </div>

      <div class="card-footer">
        <button class="btn btn-no" onclick="goToCard(3)">← 返回</button>
        <button class="btn btn-yes" onclick="goToCard(5)">猜你喜欢 →</button>
      </div>
    </div>

    <!-- ============ 卡片5 ============ -->
    <div class="filmask-card" id="card5">
      <div class="card-header">
        <div class="logo-wrap">
          <span class="logo-icon">◈</span>
          <span class="logo">FilMask</span>
          <span class="logo-tag">CINEMA</span>
        </div>
        <div class="card-progress">
          <div class="progress-dot"></div>
          <div class="progress-dot"></div>
          <div class="progress-dot"></div>
          <div class="progress-dot"></div>
          <div class="progress-dot active"></div>
        </div>
      </div>

      <div class="card-body">
        <div class="section-label">LIKE · 专属你的电影指南</div>
        
        <div class="recommend-section">
          <div class="recommend-title">SAME GENRE · 同类型</div>
          <div class="recommend-list">
            <div class="recommend-item" onclick="showToast('已加载《看不见的客人》详情')">
              <div class="recommend-poster">
                <img src="assets/img/invisible-guest.jpg" alt="看不见的客人 海报">
              </div>
              <div class="recommend-info">
                <div class="recommend-top">
                  <div class="recommend-name">看不见的客人</div>
                  <div class="recommend-match">94% 匹配</div>
                </div>
                <div class="recommend-meta">2016 · 西班牙 · 奥里奥尔·保罗</div>
                <div class="recommend-rating">★ 豆瓣 8.8</div>
                <div class="match-bar"><div class="match-bar-fill" style="width: 94%"></div></div>
                <div class="recommend-reason">同样是层层反转的悬疑神作，"每一句话都可能是谎言"的极致演绎</div>
              </div>
            </div>
            <div class="recommend-item" onclick="showToast('已加载《控方证人》详情')">
              <div class="recommend-poster">
                <img src="assets/img/witness.jpg" alt="控方证人 海报">
              </div>
              <div class="recommend-info">
                <div class="recommend-top">
                  <div class="recommend-name">控方证人</div>
                  <div class="recommend-match">89% 匹配</div>
                </div>
                <div class="recommend-meta">1957 · 美国 · 比利·怀尔德</div>
                <div class="recommend-rating">★ 豆瓣 9.6</div>
                <div class="match-bar"><div class="match-bar-fill" style="width: 89%"></div></div>
                <div class="recommend-reason">"妻子"的伪证传统由此片开创，Amy 的精神祖母</div>
              </div>
            </div>
          </div>
        </div>

        <div class="recommend-section">
          <div class="recommend-title">SAME DIRECTOR · 同导演</div>
          <div class="recommend-list">
            <div class="recommend-item" onclick="showToast('已加载《七宗罪》详情')">
              <div class="recommend-poster">
                <img src="assets/img/se7en.jpg" alt="七宗罪 海报">
              </div>
              <div class="recommend-info">
                <div class="recommend-top">
                  <div class="recommend-name">七宗罪</div>
                  <div class="recommend-match">96% 匹配</div>
                </div>
                <div class="recommend-meta">1995 · 大卫·芬奇</div>
                <div class="recommend-rating">★ 豆瓣 8.8</div>
                <div class="match-bar"><div class="match-bar-fill" style="width: 96%"></div></div>
                <div class="recommend-reason">芬奇的暗黑美学起点，结尾那个盒子永远忘不掉</div>
              </div>
            </div>
            <div class="recommend-item" onclick="showToast('已加载《搏击俱乐部》详情')">
              <div class="recommend-poster">
                <img src="assets/img/fight-club.jpg" alt="搏击俱乐部 海报">
              </div>
              <div class="recommend-info">
                <div class="recommend-top">
                  <div class="recommend-name">搏击俱乐部</div>
                  <div class="recommend-match">91% 匹配</div>
                </div>
                <div class="recommend-meta">1999 · 大卫·芬奇</div>
                <div class="recommend-rating">★ 豆瓣 9.0</div>
                <div class="match-bar"><div class="match-bar-fill" style="width: 91%"></div></div>
                <div class="recommend-reason">关于现代人精神分裂的最佳寓言，叙事诡计的祖师爷</div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="card-footer">
        <button class="btn btn-no" onclick="goToCard(4)">← 返回院线</button>
        <button class="btn btn-yes" onclick="closeFilmask()">完成探索</button>
      </div>
    </div>

  </div>

  <button class="nav-arrow left" id="navLeft" onclick="prevCard()">‹</button>
  <button class="nav-arrow right" id="navRight" onclick="nextCard()">›</button>

  <div class="swipe-indicator" id="swipeIndicator">
    <div class="swipe-dot active" data-card="1"></div>
    <div class="swipe-dot" data-card="2"></div>
    <div class="swipe-dot" data-card="3"></div>
    <div class="swipe-dot" data-card="4"></div>
    <div class="swipe-dot" data-card="5"></div>
  </div>

</div>

<div class="modal" id="theaterModal">
  <div class="modal-card">
    <div class="modal-icon">🎬</div>
    <div class="modal-title">即将进入抖音放映厅</div>
    <div class="modal-desc">你将跳转至《消失的爱人》在线观看页面</div>
    <div class="modal-tip">
      💡 如需获得更好的观影体验<br>
      建议转移至<strong style="color:#d4734a">抖音 PC 端</strong>观看
    </div>
    <div class="modal-actions">
      <button class="modal-btn secondary" onclick="closeTheaterModal()">取消</button>
      <button class="modal-btn primary" onclick="confirmTheater()">继续在手机观看</button>
    </div>
  </div>
</div>

<div class="toast" id="toast"></div>

<script>
let currentCard = 1;

function goToCard(num) {
  const oldCard = document.querySelector('.filmask-card.active');
  const newCard = document.getElementById('card' + num);
  if (!newCard || oldCard === newCard) return;
  
  if (oldCard) {
    const oldIdx = getCardIndex(oldCard.id.replace('card', ''));
    const newIdx = getCardIndex(num);
    if (newIdx > oldIdx) oldCard.classList.add('exit-left');
    else oldCard.classList.add('exit-right');
    setTimeout(() => oldCard.classList.remove('active', 'exit-left', 'exit-right'), 300);
  }
  
  setTimeout(() => {
    newCard.classList.add('active');
    currentCard = num;
    updateUI();
  }, 200);
}

function getCardIndex(num) {
  const str = String(num);
  if (str === '1') return 1;
  if (str === '2') return 2;
  if (str === '3' || str === '3-f' || str === '3-nf') return 3;
  if (str === '4') return 4;
  if (str === '5') return 5;
  return 0;
}

function updateUI() {
  const idx = getCardIndex(currentCard);
  document.querySelectorAll('.swipe-dot').forEach((dot, i) => {
    dot.classList.toggle('active', i + 1 === idx);
  });
  document.querySelectorAll('.debug-btn').forEach(btn => btn.classList.remove('active'));
  const btns = document.querySelectorAll('.debug-btn');
  if (currentCard === 1) btns[0].classList.add('active');
  else if (currentCard === 2) btns[1].classList.add('active');
  else if (currentCard === 3) btns[2].classList.add('active');
  else if (currentCard === '3-f') btns[3].classList.add('active');
  else if (currentCard === '3-nf') btns[4].classList.add('active');
  else if (currentCard === 4) btns[5].classList.add('active');
  else if (currentCard === 5) btns[6].classList.add('active');
  
  document.getElementById('navLeft').classList.toggle('disabled', idx === 1);
  document.getElementById('navRight').classList.toggle('disabled', idx === 5);
}

function nextCard() { const idx = getCardIndex(currentCard); if (idx < 5) goToCard(idx + 1); }
function prevCard() { const idx = getCardIndex(currentCard); if (idx > 1) goToCard(idx - 1); }

function answerCard1(answer) {
  if (answer === 'yes') {
    showToast('✓ 看过了 · 跳转到衍生与讨论');
    setTimeout(() => goToCard(3), 600);
  } else {
    showToast('▸ 先看故事梗概 + 宣传片');
    setTimeout(() => goToCard(2), 600);
  }
}

function toggleLike(btn) {
  btn.classList.toggle('liked');
  const countSpan = btn.querySelector('.comment-like-count');
  const currentCount = parseInt(countSpan.textContent);
  if (btn.classList.contains('liked')) countSpan.textContent = currentCount + 1;
  else countSpan.textContent = currentCount - 1;
}

function openTheaterModal() { document.getElementById('theaterModal').classList.add('active'); }
function closeTheaterModal() { document.getElementById('theaterModal').classList.remove('active'); }
function confirmTheater() { closeTheaterModal(); showToast('🎬 已跳转至抖音放映厅'); }

function closeFilmask() {
  showToast('◈ FilMask 已收起 · 继续刷视频');
  setTimeout(() => {
    const container = document.querySelector('.filmask-container');
    if (container) container.classList.remove('shown');
    playOutroVideo();
  }, 800);
}

// ===== 刷入/刷出视频：用户上下滑切换；刷入两条后上滑弹出卡片；关闭卡片 → 刷出 =====
const INTRO_VIDEOS = ['assets/video/intro-1.mp4', 'assets/video/intro-2.mp4'];
const OUTRO_VIDEO = 'assets/video/outro.mp4';

let feedMode = 'intro'; // intro | idle | outro
let introIndex = 0;     // 0/1

function showCards() {
  const container = document.querySelector('.filmask-container');
  if (container) container.classList.add('shown');
}

function hideFeedVideo() {
  const v = document.getElementById('feedVideo');
  if (!v) return;
  v.pause();
  v.style.opacity = '0';
  // 等过渡结束再隐藏，避免闪烁
  setTimeout(() => { v.style.display = 'none'; }, 360);
}

function playFeedVideo(src) {
  const v = document.getElementById('feedVideo');
  if (!v) return;
  v.style.display = 'block';
  // 先置0再到1，保证每次切片都有过渡
  v.style.opacity = '0';
  // intro 循环播放；outro 不循环，播完自动收起
  v.loop = (feedMode !== 'outro');
  v.src = src;
  v.load();
  const p = v.play();
  if (p && p.catch) p.catch(() => {});
  requestAnimationFrame(() => { v.style.opacity = '1'; });
}

function startIntroSequence() {
  // 进入页面先隐藏卡片，先刷两条视频
  const container = document.querySelector('.filmask-container');
  if (container) container.classList.remove('shown');

  feedMode = 'intro';
  introIndex = 0;
  playFeedVideo(INTRO_VIDEOS[introIndex]);
}

function playOutroVideo() {
  feedMode = 'outro';
  playFeedVideo(OUTRO_VIDEO);
}

const feedVideo = document.getElementById('feedVideo');
if (feedVideo) {
  feedVideo.addEventListener('ended', () => {
    if (feedMode === 'outro') {
      // 刷出播完后回到黑底
      feedMode = 'idle';
      hideFeedVideo();
    }
  });
}

function feedNext() {
  // 仅在刷入阶段响应上滑
  if (feedMode !== 'intro') return;
  if (introIndex < INTRO_VIDEOS.length - 1) {
    introIndex += 1;
    playFeedVideo(INTRO_VIDEOS[introIndex]);
  } else {
    // 第二条刷入视频上滑 → 弹出卡片
    feedMode = 'idle';
    hideFeedVideo();
    showCards();
  }
}

function feedPrev() {
  // 仅在刷入阶段响应下滑
  if (feedMode !== 'intro') return;
  if (introIndex > 0) {
    introIndex -= 1;
    playFeedVideo(INTRO_VIDEOS[introIndex]);
  }
}

function playTrailer(e) {
  const box = document.getElementById('trailerBox');
  const v = document.getElementById('trailerVideo');
  if (!box || !v) return;

  if (v.paused) {
    const p = v.play();
    if (p && p.catch) {
      p.then(() => box.classList.add('playing'))
       .catch(() => showToast('⚠️ 未找到宣传片：请放入 assets/video/trailer.mp4'));
    } else {
      box.classList.add('playing');
    }
  } else {
    v.pause();
    box.classList.remove('playing');
  }
}

function showToast(msg) {
  const t = document.getElementById('toast');
  t.innerHTML = msg;
  t.classList.add('show');
  setTimeout(() => t.classList.remove('show'), 2200);
}

let touchStartX = 0;
let touchStartY = 0;
const phone = document.querySelector('.phone');
phone.addEventListener('touchstart', e => touchStartX = e.changedTouches[0].screenX);
phone.addEventListener('touchstart', e => touchStartY = e.changedTouches[0].screenY);
phone.addEventListener('touchend', e => {
  const endX = e.changedTouches[0].screenX;
  const endY = e.changedTouches[0].screenY;
  const diffX = touchStartX - endX;
  const diffY = touchStartY - endY; // >0 上滑

  const container = document.querySelector('.filmask-container');
  const cardsShown = container && container.classList.contains('shown');

  if (cardsShown) {
    // 卡片内：左右滑切页
    if (Math.abs(diffX) < 50 || Math.abs(diffX) < Math.abs(diffY)) return;
    if (diffX > 0) nextCard(); else prevCard();
  } else {
    // 视频刷入：上下滑切换
    if (Math.abs(diffY) < 60 || Math.abs(diffY) < Math.abs(diffX)) return;
    if (diffY > 0) feedNext(); else feedPrev();
  }
});

let mouseStartX = 0, isMouseDown = false;
phone.addEventListener('mousedown', e => { mouseStartX = e.screenX; isMouseDown = true; });
phone.addEventListener('mouseup', e => {
  if (!isMouseDown) return;
  isMouseDown = false;
  const diff = mouseStartX - e.screenX;
  if (Math.abs(diff) < 50) return;
  if (diff > 0) nextCard(); else prevCard();
});

// 桌面端：滚轮模拟上下滑（未弹出卡片时）
phone.addEventListener('wheel', e => {
  const container = document.querySelector('.filmask-container');
  const cardsShown = container && container.classList.contains('shown');
  if (cardsShown) return;
  if (Math.abs(e.deltaY) < 20) return;
  if (e.deltaY > 0) feedNext();
  else feedPrev();
}, { passive: true });

const trailerVideo = document.getElementById('trailerVideo');
if (trailerVideo) {
  trailerVideo.addEventListener('ended', () => {
    const box = document.getElementById('trailerBox');
    if (box) box.classList.remove('playing');
  });
}

document.addEventListener('keydown', e => {
  if (e.key === 'ArrowLeft') prevCard();
  if (e.key === 'ArrowRight') nextCard();
});

updateUI();
startIntroSequence();
</script>
</body>
</html>
