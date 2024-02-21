import xml.dom.minidom as dom

domTree = dom.parse("xml_files/example.xml")
group = domTree.documentElement
books = group.getElementsByTagName("book")

for book in books:
    author = book.getElementsByTagName("author")[0].childNodes[0].nodeValue
    title = book.getElementsByTagName("title")[0].childNodes[0].nodeValue
    genre = book.getElementsByTagName("genre")[0].childNodes[0].nodeValue
    price = book.getElementsByTagName("price")[0].childNodes[0].nodeValue
    publish_date = book.getElementsByTagName("publish_date")[0].childNodes[0].nodeValue

    # to fetch surname details within author tag
    author_element = book.getElementsByTagName("author")[0]
    author_name = ""
    surname_element = author_element.getElementsByTagName("surname")
    if surname_element:
        surname = surname_element[0].childNodes[0].nodeValue
    else:
        surname = ""

    print(f"Author- {author}")
    print(f"Surname- {surname}")
    # print(f"Title- {title}")
    # print(f"Genre- {genre}")
    # print(f"Price- {price}")
    # print(f"Publishing Date- {publish_date}")


# Adding new node to the xml file
new_book = domTree.createElement("book")
new_book.setAttribute("id", "bk113")

author = domTree.createElement("author")
author.appendChild(domTree.createTextNode("APJ Abdul Kalam"))

title = domTree.createElement("title")
title.appendChild(domTree.createTextNode("Wings of Fire"))

genre = domTree.createElement("genre")
genre.appendChild(domTree.createTextNode("Life"))

price = domTree.createElement("price")
price.appendChild(domTree.createTextNode("89.23"))

publish_date = domTree.createElement("publish_date")
publish_date.appendChild(domTree.createTextNode("2002-12-14"))

new_book.appendChild(author)
new_book.appendChild(title)
new_book.appendChild(genre)
new_book.appendChild(price)
new_book.appendChild(publish_date)

group.appendChild(new_book)

domTree.writexml(open("example.xml", "w"))
