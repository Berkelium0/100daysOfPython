from bs4 import BeautifulSoup
import requests

response = requests.get(
    "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/").text

soup = BeautifulSoup(response, "html.parser")

movie_list = [title.get_text() for title in soup.find_all("h3")]
movies = movie_list[::-1]

#  movie_list.insert(0, .encode("ascii", "xmlcharrefreplace"))

with open("movies.txt", "w") as f:
    for item in movies:
        f.write(f"{item.encode('ascii', 'replace').decode('ascii')}\n")

# Get daily highest voted story from ycombinator
# response = requests.get("https://news.ycombinator.com/news")
# yc_web_page = response.text
#
# soup = BeautifulSoup(yc_web_page, "html.parser")
#
# article_tag = soup.find_all("span", class_="titleline")
# article_texts = []
# article_links = []
# for article in article_tag:
#     a = article.find("a")
#     article_texts.append(a.getText())
#     article_links.append(a.get("href"))
#
# article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all("span", class_="score")]
# max_index = article_upvotes.index(max(article_upvotes))
# print(article_texts[max_index], "\n", article_links[max_index], "\n", article_upvotes[max_index])
