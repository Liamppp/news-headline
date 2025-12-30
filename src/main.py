import feedparser
from datetime import datetime
from email.utils import parsedate_to_datetime

url = "https://www.yna.co.kr/rss/news.xml"
feed = feedparser.parse(url)


for i, entry in enumerate(feed.entries[:10], 1):
  published = parsedate_to_datetime(entry.published)

  if published.strftime('%d') != datetime.now().strftime('%d'): continue

  print(f"{i}. [{published.strftime('%H:%M')}] {entry.title}")

# 내가 뉴스 헤드라인 뽑으려고 네이버 API, 공공데이터포털 OpenAPI, 크롤링 이런 뻘짓 다 했는데 결국에 RSS가 정답이었다 ㅋㅋㅋ ㅅㅂ