fout=open("binaryWrite","wb")
content=bytes(range(0,256))
print(content)
fout.write(content)
fout.close()