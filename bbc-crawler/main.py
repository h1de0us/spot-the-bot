from utils import *


def test_case_1():
    url = 'https://www.bbc.com/pidgin/sport-61457814'
    txt = get_text_from_link(url)
    print(txt)


def test_case_2():
    url = 'https://www.bbc.com/pidgin'
    links = get_links_from_webpage(url)
    for link in links:
        print(link)


def test_case_3():
    get_links()
    print(len(used))


def test_case_4():
    export_text_from_links("links.txt", "corpus.txt")
