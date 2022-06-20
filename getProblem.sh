#!/bin/sh -v
# first arg == contest_name e.g. 255, 254,...
# second arg == task_name e.g. a, b, c
i=$1
j=$2
url="https://atcoder.jp/contests/abc${i}/tasks/abc${i}_${j}"
out="./out/${i}/${j}.pdf"
mkdir "./out/${i}"
docker run --rm -v $(pwd):/converted/ arachnysdocker/athenapdf athenapdf $url $out



