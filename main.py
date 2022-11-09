from bs4 import BeautifulSoup
# import lxml

# ------------------------------------------------------------------------------------------
# Using BeautifulSoup from the live website on Internet
import requests
response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.select(".title .titleline a")
article_texts = [article_tag.getText() for article_tag in articles]
article_links = [article_tag.get("href") for article_tag in articles]
article_upvotes = [int(score.getText().split()[0])
                   for score in soup.select(".subline .score")]

max_upvote = max(article_upvotes)
index_max_upvote = article_upvotes.index(max_upvote)

print(article_texts[index_max_upvote])
print(article_links[index_max_upvote])

# ------------------------------------------------------------------------------------------
# Using BeautifulSoup Locally
# 🫳🫳
# with open("website.html", encoding="utf8") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.prettify())
# # print(soup.title.string)
# # all_anchor_tags = soup.findAll(name="a")
# # for tag in all_anchor_tags:
# #     print(tag.getText())
# #     print(tag.get("href"))

# section_heading = soup.find(name="h3", class_="heading")
# # print(section_heading)

# name = soup.select(selector="p")
# print(name)
