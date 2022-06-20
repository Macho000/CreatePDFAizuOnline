#!/bin/sh -v
# first arg == id e.g. ITP1_1_A
# second arg == answer_url e.g. review.jsp?rid=1983386#1
# third arg == task_name
i=$1
answer_url=$2
task_name=$3
url="https://judge.u-aizu.ac.jp/onlinejudge/${answer_url}"
out="./out/IntroductionToProgramming1/${i}_${task_name}_Answer.pdf"
mkdir "./out"
mkdir "./out/IntroductionToProgramming1"
docker run --rm -v $(pwd):/converted/ arachnysdocker/athenapdf athenapdf $url $out



