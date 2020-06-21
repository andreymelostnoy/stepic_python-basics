# import requests
# import re
#
#
# # url = input().strip()
# # r = requests.get(url).text
# r = """
# <a href="http://stepic.org/courses">;
# <a class = "hello" href= "http://ftepic.org/courses"; id="dfdf">
# <p class = "hello" href= "http://dtepic.org/courses">;
# <a class = "hello" href = "http://a.b.vc.ttepic.org/courses">;
# <a href='https://stepic.org'>;
# <a href='http://neerc.ifmo.ru:1345'>;
# <a href = "ftp://mail.ru/distib" >
# <a href= "ya.ru">
# <a href ="www.ya.ru">;
# <a href="../skip_relative_links">
# <link rel="image_src" href="https://examaple.org/files/6a2/72d/e09/6a272de0944f447fb5972c44cc02f795.png"; />
# """
#
# p1 = r'<a.+href=[\'\"]([^./][^\'\"]*)[\'\"]'
# links = re.findall(p1, r)
# print(links)
# p2 = r"(.*://)*"
# links_p2 = []
# for link in links:
#     links_p2.append(re.sub(p2, "", link))
# print(links_p2)
# p3 = r"/\w+"
# links_p3 = []
# for link in links_p2:
#     links_p3.append(re.sub(p3, "", link))
# print(links_p3)
# p4 = r"\:\d*"
# links_p4 = []
# for link in links_p3:
#     links_p4.append(re.sub(p4, "", link))
# print(links_p4)
# p5 = r"(\?.*)|(\/.*)"
# links_p5 = []
# for link in links_p4:
#     links_p5.append(re.sub(p5, "", link))
# print(links_p5)
# result = list(set(links_p5))
# result.sort()
# print(result)
# # for url in result:
# #     print(url)

import re
import urllib.request
from urllib.parse import urlparse

url = input()


def get_links():
    try:
        fp = urllib.request.urlopen(url)
        mybytes = fp.read()
        mystr = mybytes.decode("utf8")
        fp.close()
        links = re.findall(r'<a.+href=[\'"]([^./][^\'"]*)[\'"]', mystr)
    except:
        return []
    else:
        return links


def parse_link(link):
    parsed_uri = urlparse(link)
    res = parsed_uri.netloc
    try:
        return res[:res.index(':')]
    except:
        return res
    else:
        return res[:res.index(':')]


links = get_links()

unsorted = list(map(parse_link, links))

for link in sorted(list(set(unsorted))):
    print(link)
