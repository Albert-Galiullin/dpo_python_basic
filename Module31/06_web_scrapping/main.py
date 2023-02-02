import requests
import re

def get_content(pattern: str, html: str) -> None:
    p = re.compile(pattern, re.IGNORECASE)
    res = re.findall(p, html)
    for e in res:
        print(e)


# if __name__ == "__main__":
pattern = r'<h3.*>(.+?)</h3>'
url = 'http://www.columbia.edu/~fdc/sample.html'
html = requests.get(url).text
get_content(pattern, html)
