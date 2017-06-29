import xml.etree.ElementTree as et
tree=et.ElementTree(file="menu.xml")
root=tree.getroot()
print(root.tag)
for child in root:
    print("child tag=",child.tag,"child attribute",child.attrib)
