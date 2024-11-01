from selenium import webdriver
import requests

res = requests
url = "https://news.yahoo.co.jp"
res.get(url)

# 試しに取得したいページの一部を取得
result = res.get(url).text[:500]

print(result)
