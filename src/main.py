import os
import feedparser
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from email.utils import parsedate_to_datetime

input_dir = os.path.join(os.getcwd(), 'input')
output_dir = os.path.join(os.getcwd(), 'output')

ban_words = ['[인사]', '[부고]']

def manipulating():
  url = "https://www.yna.co.kr/rss/news.xml"
  feed = feedparser.parse(url)

  input_list = os.listdir(input_dir)

  for i, entry in enumerate(feed.entries[:len(input_list)], 0):
    published = parsedate_to_datetime(entry.published)

    if published.strftime('%d') != datetime.now().strftime('%d'): continue

    font_path = os.path.join(os.getcwd(), 'assets', 'font', 'Pretendard-Bold.ttf')
    font = ImageFont.truetype(font_path, 70)

    image = Image.open(os.path.join(input_dir, input_list[i]))
    headline = f"{entry.title}"
    img_size = (1920, 1080)
    
    image = image.resize(img_size)
    draw = ImageDraw.Draw(image)

    left, top, right, bottom = draw.textbbox((0, 900), headline, font=font)
    text_width = right - left

    position = ((img_size[0] - text_width) / 2, 900)

    draw.rectangle((position[0] -20, top -10, position[0] +text_width +20, bottom +10), fill="#000080")
    draw.text(xy=position, text=headline, fill="#ffffff", font=font, align='center')

    image.save(os.path.join(output_dir, f"converted[{i}].png"))

manipulating()

# 내가 뉴스 헤드라인 뽑으려고 네이버 API, 공공데이터포털 OpenAPI, 크롤링 이런 뻘짓 다 했는데 결국에 RSS가 정답이었다 ㅋㅋㅋ ㅅㅂ