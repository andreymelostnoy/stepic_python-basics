import requests
import re


url1, url2 = (input() for _ in range(2))
pattern = r'href=\"(.*)\"'
url1_links = re.findall(pattern, requests.get(url1).text)
deep_url_links = []
for url in url1_links:
    deep_url_links.append(re.findall(pattern, requests.get(url).text))

result = False

for lst in deep_url_links:
    for url in lst:
        if url2 in url:
            result = True
            break

if result:
    print("Yes")
else:
    print("No")

