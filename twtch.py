import urllib.request
import webbrowser
headers = {}
headers['User-Agent'] = "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:48.0) Gecko/20100101 Firefox/48.0"

req = urllib.request.Request('https://twitchmaster.ru', headers = headers)
html = urllib.request.urlopen(req).read()
with open('twitch.html','wb') as f:
    f.write(html)

webbrowser.open('https://twitchmaster.ru', new=0)