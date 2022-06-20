# coding: UTF-8
import sys
import requests
import os
from bs4 import BeautifulSoup    # importする
from requests_html import HTMLSession # enable javascript rendering
import pyppeteer
import urllib.request
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains #マウスオーバーするために必要


def createPdf(contest: str, task_name: str):
  answer_url = f"https://judge.u-aizu.ac.jp/onlinejudge/solution.jsp?pid={contest}"
  print("answer_url is :"+answer_url)

  # 各動作間の待ち時間（秒）
  INTERVAL = 3

  # ブラウザ起動
  driver_path = "./chromedriver"
  driver = webdriver.Chrome(executable_path=driver_path)

  # windowサイズをmaxにする
  driver.maximize_window()
  time.sleep(INTERVAL)

  # サイトを開く
  driver.get(answer_url)
  time.sleep(INTERVAL)

  # 検索先のページのHTMLを取得
  html = driver.page_source.encode('utf-8')
  html = BeautifulSoup(html, "html.parser")    # HTMLを解析する
  a = html.find(id="solutionTable").find('a', href=True)
  href = a['href']
  get_problem_command = f"bash getProblem.sh {contest} {task_name}"
  os.system(get_problem_command)
  get_answer_command = f"bash getAnswer.sh {contest} {href} {task_name}"
  os.system(get_answer_command)
   # ブラウザを閉じる
  driver.close()

if __name__=='__main__':

  url = "https://judge.u-aizu.ac.jp/onlinejudge/finder.jsp?course=ITP1"
  # 各動作間の待ち時間（秒）
  INTERVAL = 3

  # ブラウザ起動
  driver_path = "./chromedriver"
  driver = webdriver.Chrome(executable_path=driver_path)

  # windowサイズをmaxにする
  driver.maximize_window()
  time.sleep(INTERVAL)

  # サイトを開く
  driver.get(url)
  time.sleep(INTERVAL)

  # 検索先のページのHTMLを取得
  html = driver.page_source.encode('utf-8')
  html = BeautifulSoup(html, "html.parser")    # HTMLを解析する
  table = html.find(id="rankingBody")
  for elment in table.find_all("tr"):
    task_href = elment.find("a", href=True)
    task_id = task_href["href"].split("=")[-1]
    task_name = task_href.text.replace("&nbsp;", ":").split(":")[-1].strip().replace(" ", "_")
    createPdf(task_id, task_name)
  # ブラウザを閉じる
  driver.close()
