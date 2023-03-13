import io
from bs4 import BeautifulSoup
#install lxml,beautifulsoup4
path="index.html"
with io.open(path, encoding='utf-8') as f:
    contents = f.read()
    soup = BeautifulSoup(contents, 'lxml')
    print(soup.head.title.text)
    for tag in soup.find_all(["p", "h1", "h2", "h3", "h4", "h5", "h6"]):
        print("{0}: {1}".format(tag.name, tag.text))