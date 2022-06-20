#!/bin/sh -v
# first arg == id e.g. ITP1_1_A
# second arg == task_name
i=$1
task_name=$2
url="https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=${i}"
out="./out/IntroductionToProgramming1/${i}_${task_name}.pdf"
mkdir "./out"
mkdir "./out/IntroductionToProgramming1"
docker run --rm -v $(pwd):/converted/ arachnysdocker/athenapdf athenapdf $url $out



