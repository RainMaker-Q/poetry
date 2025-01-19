import json
import requests

# 1. 从文件中导入数据
with open("data.json", "r", encoding="utf-8") as file:
  data = json.load(file)  # 将 JSON 文件内容解析为 Python 对象（列表）

# 2. 遍历数组子项，发起请求
url = "http://localhost:3000/poetry"  # 替换为你的目标 API 地址

step = 0
for item in data:
  # 构造 POST 请求的参数
  step = step + 1
  payload = {
    "title": item["title"],
    "note": item["note"],
    "contentZh": item["content_zh"],
    "contentEn": item["content_en"],
    "number": step
  }
  
  # 发起 POST 请求
  try:
    response = requests.post(url, json=payload)
    response.raise_for_status()  # 检查请求是否成功
    print(f"Sent: {payload}")
    print(f"Response: {response.json()}")
  except requests.exceptions.RequestException as e:
    print(f"Error occurred for {payload}: {e}")
