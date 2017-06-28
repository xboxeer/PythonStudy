poem="there was a young lady named Bright"+\
    "whose speed was far faster then the light"+\
    "she started one day"+\
    "in a relative way,"+\
    "and returned on the previous night"
print(len(poem))
fout=open("relativity","w")
offset=0
chunk=100
while True:
    if(offset>len(poem)):
        break
    print(fout.write(poem[offset:offset+chunk]))
    offset+=chunk
fout.close()
