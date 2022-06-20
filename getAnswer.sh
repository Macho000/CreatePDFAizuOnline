#!/bin/sh -v
# first arg == contest_name e.g. 255, 254,...
# second arg == task_name e.g. a, b, c
# third arg == answer url e.g. https://atcoder.jp/contests/abc254/editorial/4064
i=$1
j=$2
answer_url=$3
url="https://atcoder.jp${answer_url}"
out="./out/${i}/${j}_Answer.pdf"
mkdir "./out/${i}"
docker run --rm -v $(pwd):/converted/ arachnysdocker/athenapdf athenapdf $url $out



