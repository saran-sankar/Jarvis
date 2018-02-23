import urllib.request
keyword='hey'
page = urllib.request.urlopen('https://www.facebook.com/saransankar.ep/friends?lst=100001818993231%3A100001818993231%3A1514789161&source_ref=pb_friends_tl')
string = page.read().decode('utf-8')
print(string)
