"""list study-2"""
small_bird=["hummingBird","finch"]
extinct_bird=["dodo","passener pigeon","Norwegain Blue"]
all_bird=[small_bird,extinct_bird]
print(all_bird[0][0])
all_bird[0][0]="some small bird"
print(all_bird[0][0])
print(all_bird[1][1:4])
small_bird.append("another bird")
small_bird.append("another bird")
print(small_bird)
small_bird.extend(extinct_bird)
print(small_bird)
small_bird.insert(0,"ma que")
print(small_bird)
del small_bird[0]
print(small_bird)
small_bird.remove("another bird")
print(small_bird)
top=small_bird.pop()
print(top)
print(small_bird)
print("finch" in small_bird)
print(",".join(small_bird))
small_bird.sort()
print(small_bird)

