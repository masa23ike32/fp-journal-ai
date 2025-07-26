import openai
import os
from datetime import datetime

openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_text(text):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "あなたは税制改正の要約アシスタントです。FP向けに簡潔かつ正確に要約してください。"},
            {"role": "user", "content": f"以下の文章を要約してください：\n{text}"}
        ],
        temperature=0.3
    )
    return response['choices'][0]['message']['content']

def main():
    # 仮の入力（PDF読み込みは別途追加可能）
    input_text = "令和7年度税制改正では、住宅ローン控除の対象拡大、iDeCo掛金上限の引き上げ..."

    summary = summarize_text(input_text)

    html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <title>税制改正要約</title>
    <style>
        body {{ font-family: sans-serif; padding: 2em; background-color: #f9f9f9; }}
        h1 {{ color: #2c3e50; }}
        p {{ line-height: 1.6; }}
    </style>
</head>
<body>
    <h1>📘 税制改正要約（{datetime.today().strftime('%Y/%m/%d')}）</h1>
    <p>{summary}</p>
</body>
</html>"""

    with open("summary.html", "w", encoding="utf-8") as f:
        f.write(html)

if __name__ == "__main__":
    main()