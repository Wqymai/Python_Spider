from bs4 import BeautifulSoup


html ="""<html><head><title>The Dormouse's story</title></head><body><a class='myclass'/><p>hello
world

</p></body></html>"""
soup = BeautifulSoup(html,'html5lib')

print soup.a
print type(soup.a)
print soup.name
print soup.a.name
print soup.a.attrs
print  soup.a['class']

print  soup.title
print  soup.title.string
print type(soup.title.string)
print "======.contents======="
print soup.head.contents
print  soup.html.contents[0]

print "========.children======="
print soup.head.children
for child in soup.html.children:
    print child

print "========.descendants========="
for child in soup.html.descendants:
    print  child

print  "======.strings===="
for str in soup.strings:
    print repr(str)

print "===.stripped_strings======"
for str in soup.stripped_strings:
    print  repr(str)

print "===.parent====="
p=soup.a
print p.parent.name







