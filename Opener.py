import urllib.request
from urllib.request import Request,urlopen
def UrlToOpen(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    Page = urlopen(req).read()
    return Page
class myUrlOpener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"


