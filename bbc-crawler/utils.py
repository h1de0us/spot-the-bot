import requests
from bs4 import BeautifulSoup
import queue

used = set()
q = queue.Queue()


def export_text_from_links(in_file, out_file):
    fin = open(in_file, "r")
    links = fin.readlines()
    fin.close()
    fout = open(out_file, "w")
    for i, link in enumerate(links):
        text = get_text_from_link(link.strip())
        # if i % 10 == 0:
        #     print("iteration {0}".format(i // 10))
        fout.write(text + '\n')
    fout.close()


def get_links(n_links=100, filename="links.txt"):
    # base url
    url = "https://www.bbc.com/pidgin/"
    f = open(filename, "w")
    q.put(url)
    counter = 0
    while not q.empty():
        counter += 1
        if counter == n_links:
            break
        cur = q.get()
        f.write(cur + '\n')
        used.add(cur)
        links = get_links_from_webpage(cur)
        for link in links:
            if link not in used:
                q.put(link)
    f.close()


def get_links_from_webpage(url) -> list:
    links = set()
    r = requests.get(url)
    contents = r.text
    soup = BeautifulSoup(contents, 'lxml')
    for tag in soup.find_all("a"):
        # либо ссылка начинается с https://www.bbc.com/pidgin/
        link = tag.get("href")
        if link is None:
            continue
        if link.startswith("https://www.bbc.com/pidgin/") or link.startswith("http://www.bbc.com/pidgin/"):
            link = link.replace('http:', 'https:')
            links.add(link)
        elif link.startswith("/pidgin/"):
            links.add("https://www.bbc.com" + link)
    return list(links)


# считаем, что текст статьи лежит внутри div
def get_text_from_link(link):
    text = ""
    r = requests.get(link)
    if r.status_code != requests.codes.ok:
        return text
    contents = r.text
    soup = BeautifulSoup(contents, 'lxml')
    for child in soup.recursiveChildGenerator():
        if child.name == "div":
            for grandchild in child.descendants:
                if grandchild.name == "p":
                    text += grandchild.text
                    text += "\n"
    # print(text)
    return text
