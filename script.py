from selenium import webdriver
import requests
from bs4 import BeautifulSoup


def fetchData(url):
    """指定したURLからデータを取得する関数"""
    response = requests.get(url)
    return response.text


def extractTags(html, tag):
    """HTMLから特定のタグを抜き出す関数"""
    soup = BeautifulSoup(html, "html.parser")
    return soup.find_all(tag)  # 指定したタグをすべて取得


url = "https://news.yahoo.co.jp"
htmlData = fetchData(url)

# <h1>タグを抜き出す
aTags = extractTags(htmlData, "a")

# 抜き出したタグを表示
for a in aTags:
    print(a.text)  # タグのテキストを表示
