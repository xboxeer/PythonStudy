fin=open("relativity","r")
poem=fin.read()
fin.close()
print(poem)

poem=""
offset=0
chunk=100
fin=open("relativity","r")
while True:
    piece=fin.read(chunk)
    if not piece:
        break
    poem+=piece
    print(poem)
    print(len(poem))
fin.close()
print(poem)
print(len(poem))