test1="this is a test of emergency text system"
with open('test','wt') as fout:
    fout.write(test1)
with open('test','rt') as fin:
    test2=fin.read()
    print(test2)