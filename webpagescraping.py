import requests
from bs4 import BeautifulSoup

# exercise 17
url = "https://www.nytimes.com"

r = requests.get(url)
r_html = r.text
soup = BeautifulSoup(r_html)

# Does not work
for story_heading in soup.find_all(class_="balancedHeadline"):
    if story_heading.a:
        print(story_heading.a.text.replace("\n", " ").strip())
    else:
        print(story_heading.contents[0].strip())
