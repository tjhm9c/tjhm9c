import requests
from bs4 import BeautifulSoup

def trace(link, follows=[]):
    r = requests.get(link)
    soup = BeautifulSoup(r.text, "html.parser")
    body = soup.find("div", {"id": "mw-content-text"})
    follow_link = None
    for p in body.find_all("p"):
        for link in p.find_all("a"):
            href = link.get("href")
            if href is not None:
                if "/wiki/" == href[0:6] and ":" not in href and "#" not in href and "(" not in href:
                    new_link = "https://en.wikipedia.org" + href
                    new_text = link.get_text()
                    if new_link not in follows and follow_link is None:
                        follows.append(new_link)
                        follow_link = new_link
                        if new_text.lower() == "philosophy":
                            follows.append(new_link)
                            return follows
    return trace(follow_link, follows)

# links = trace("https://en.wikipedia.org/wiki/Hello")
#
# for link in links:
#     webbrowser.open_new(link)