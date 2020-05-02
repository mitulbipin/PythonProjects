from bs4 import BeautifulSoup
import requests

file1 = open("proxies.txt", "w")


def crawl_proxy():
    proxies = []
    link = "https://www.sslproxies.org"

    r = requests.get(link)
    s = BeautifulSoup(r.text, "html.parser")
    for i in s.find_all("tr"):
        try:
            data = i.find_all("td")
            address = data[0].text
            port = data[1].text
            string = address + ":" + port
            file1.write(string + "\n")
            proxies.append({"https": string})

        except:
            pass
    return proxies


proxy = crawl_proxy()
print(proxy)

file1.close()
