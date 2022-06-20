# coding: UTF-8
import sys
import requests
import os
from bs4 import BeautifulSoup    # importする


def createPdf(contest: int):
  answer_url = f"https://atcoder.jp/contests/abc{contest}/editorial"
  html = requests.get(answer_url)
  soup = BeautifulSoup(html.content, "html.parser")    # HTMLを解析する
  for task in ["a", "b", "c", "d", "e", "f", 'g', 'h']:
    element = soup.find(href=f"/contests/abc{contest}/tasks/abc{contest}_{task}")
    if element is None:
      break
    element = element.findNext('ul')
    a = element.find('a', href=True)
    get_problem_command = f"bash getProblem.sh {contest} {task}"
    os.system(get_problem_command)
    get_answer_command = f"bash getAnswer.sh {contest} {task} {a['href']}"
    os.system(get_answer_command)

if __name__=='__main__':
  for contest in range(207,199, -1):
    createPdf(contest)
