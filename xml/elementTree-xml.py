import xml.etree.ElementTree as ET

xmlFile = "xml_files/example.xml"

tree = ET.parse(xmlFile)
root = tree.getroot()

# ET.dump(tree)

# for elm in root.findall("./book[@id='bk102']/"):
#     print(elm.tag)
# Output--->
# author
# title
# genre
# price
# publish_date
# description

# for elm in root.findall("./book[@id='bk102']"):
#     print(elm.attrib)
# Output--->
#{'id': 'bk102'}

# for elm in root.findall("./book[@id='bk102']/author"):
#     print(elm.text)
# Output--->
#Ralls, Kim


# This code changes the value of author for book with ID bk102
# for elm in root.findall("./book[@id='bk102']/author"):
#     elm.text = "Dall, E"
#     print(elm.text)
#     tree.write('xml_files/example.xml')

titles=[]
for title in root.findall("./book/title"):
    titles.append(title.text)

print(titles)