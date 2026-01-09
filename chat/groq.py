from dotenv import load_dotenv
from groq import Groq
import os

load_dotenv() # 載入環境變數

model_name = "openai/gpt-oss-20b"

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

# 初始化對話歷史
messages = [
    {
        "role": "system",
        "content": "使用繁體中文回答問題"
    }
]

while True:

    # 獲取用戶輸入
    user_input = input("你：")

    # 將用戶輸入加到對話歷史
    messages.append({"role": "user", "content": user_input})

    # 如果用戶輸入 '再見'，結束對話
    if user_input.lower() == '再見':
        print("AI：再見！很高興與你交談。")
        break
    
    # 發送請求給 OpenAI API
    completion = client.chat.completions.create(
        model=model_name,
        messages=messages
    )
    
    # 獲取 AI 的回應
    ai_response = completion.choices[0].message.content
    
    # 將 AI 的回應添加到對話歷史
    messages.append({"role": "assistant", "content": ai_response})
    
    # 印出 AI 的回應
    print(f"AI：{ai_response}")