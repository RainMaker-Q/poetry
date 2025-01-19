import requests
import urllib.parse
import time
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import markdown

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

def getAllPageUrls():
  # 发送 http 请求
  originUrl = 'https://web.archive.org/web/20140320160414/http://shashibiya.org/sonnet-no-1/'
  endUrl = 'https://web.archive.org/web/20140320160414/http://en.wordpress.com/about-these-ads/'
  url = getProxyUrl(originUrl)
  response = requests.get(url, headers=headers, timeout=10)

  if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    links = soup.find_all('a', href=True)
    res = []
    flag = False
    for link in links:
      # 获取相对链接并转换为绝对链接
      fullUrl = urljoin(url, link['href'])
      if fullUrl == originUrl:
        flag = True;
      elif fullUrl == endUrl:
        flag = False
      if(flag):
        res.append(fullUrl)
      print(fullUrl)
    print(f"[getAllPageUrls] res: {res}")
    return res
  else:
      print(f"Failed to receive the page.")

def fetchPageContent(url):
  # 发送 http 请求
  response = requests.get(url, headers=headers, timeout=10)

  if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.title.string
    res = {"title": title, "content_zh":"", "note":"","content_en": ""}

    paragraphs = soup.find_all('p')
    for i, paragraph in enumerate(paragraphs, start=1):
      if i==1:
        res['content_zh'] = paragraph.get_text()
      elif i==3:
        res['note'] = paragraph.get_text()
      elif i==6:
        res['content_en'] = paragraph.get_text()
    print(f"fetchPageContent res: {res}")
    return res
  else:
      print(f"Failed to receive the page.")

def getProxyUrl(url):
  proxyUrl = urllib.parse.quote_plus(url)
  fullUrl = 'https://dev.snow-cleaner.top?proxyUrl=' + proxyUrl
  return fullUrl

def getAllContent(links):
  res = []
  # 遍历数组中的每个链接
  for link in links:
    try:
      proxyUrl = getProxyUrl(link)
      content = fetchPageContent(proxyUrl)
      res.append(content)
      # 等待1秒再进行下一个请求
      time.sleep(1)
    except Exception as e:
      print(f"Error fetching {link}: {e}")
  print(f"[getAllContent] res: {res}")
  return res


allUrls = getAllPageUrls()
testUrls = allUrls[:50]

allContent = getAllContent(allUrls)

with open('poetryObj.md', 'a') as file:
  file.write(f"{allContent}")

# 转换为 Markdown
def generate_markdown(data):
  markdown_content = []
  for item in data:
    markdown_content.append(f"# {item['title']}\n")
    markdown_content.append(f"## 中文内容\n{item['content_zh']}\n")
    markdown_content.append(f"## 注释\n{item['note']}\n")
    markdown_content.append(f"## 英文内容\n{item['content_en']}\n")
  return '\n'.join(markdown_content)

# 执行转换
markdown_result = generate_markdown(allContent)

# 将结果保存为 Markdown 文件
with open('output1.md', 'w', encoding='utf-8') as file:
  file.write(markdown_result)
