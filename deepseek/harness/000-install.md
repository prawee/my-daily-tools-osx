# Install and Use DeepSeek Harness (dsh)
# ติดตั้งและใช้งาน DeepSeek Harness (dsh)

> `@deepseek-ai/dsh` 0.2.2-rc.1 (developer preview, อาจมี breaking changes) · ยังไม่ได้ทดสอบรันจริงบนเครื่องนี้

Agent harness แบบ open-source จาก DeepSeek AI (สถาปัตยกรรม plugin)
Repo: https://github.com/deepseek-ai/deepseek-harness · Docs: https://deepseek-harness.github.io/deepseek-harness/

> อ่าน [SAFETY.md](https://github.com/deepseek-ai/deepseek-harness/blob/main/SAFETY.md) ก่อนใช้งาน

## 1. Requirements / สิ่งที่ต้องมี
- Node.js >= 24.9.0 (`node -v`)
- DeepSeek API key (https://platform.deepseek.com)

## 2. Run from npm / รันผ่าน npm (เร็วสุด)
```bash
npx @deepseek-ai/dsh web
```
- เปิด Web UI ที่ `http://127.0.0.1:3080` และเปิด browser ให้อัตโนมัติ
- ผ่าน SSH จะแค่แสดง URL (ต้อง forward port เอง)
- `--no-open` = รัน server โดยไม่เปิด browser

## 3. Install globally / ติดตั้งแบบ global (ไม่บังคับ)
```bash
npm i -g @deepseek-ai/dsh
dsh web
```

## 4. Run from source / รันจาก source
```bash
git clone https://github.com/deepseek-ai/deepseek-harness.git
cd deepseek-harness
pnpm install
pnpm run build
pnpm dsh web
```
`pnpm dsh web` ใช้ไฟล์ที่ build แล้ว ไม่ build ซ้ำ

## 5. Use it / วิธีใช้
1. เปิด `http://127.0.0.1:3080`
2. เลือก workspace (โฟลเดอร์โปรเจกต์)
3. ตั้งค่า DeepSeek provider และ API key ใน UI
4. คุยกับ agent ใน workspace นั้น

## 6. CLI commands / คำสั่ง CLI
```bash
dsh web                # start Web UI / เปิด Web UI
dsh plugin add <pkg>   # install plugin / ติดตั้ง plugin
dsh --help             # ดูคำสั่งทั้งหมด
```

## Python alternative / ทางเลือก Python (บุคคลที่สาม)
โปรเจกต์อิสระของ HenryZ838978 ไม่ใช่ตัวทางการ:
```bash
pip install deepseek-harness        # client library
pip install deepseek-harness-cli    # `dsh doctor --node`
export DEEPSEEK_API_KEY=sk-...
```
```python
from deepseek_harness import DeepSeekHarness

c = DeepSeekHarness(disable_thinking_by_default=True)
out = c.chat(
    model="deepseek-v4-pro",
    messages=[{"role": "user", "content": "Hello"}],
    max_tokens=4096,
)
print(out["message"]["content"])
```
> แพ็กเกจ npm ชื่อ `deepseek-harness` (ไม่มี scope) เป็นแค่ชื่อที่จองไว้ ใช้ `@deepseek-ai/dsh` แทน
