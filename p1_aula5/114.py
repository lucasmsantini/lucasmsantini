import urllib.request

try:
    site = 'https://www.allyourmusic.com'
    response = urllib.request.urlopen("http://pudim.com.br")
except urllib.error.URLError:  # ou só o except
    print("site inexistente")
else:
    print("site ok!!")
    print(site.title())
