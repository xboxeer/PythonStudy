count=1
while count<=5:
    print(count)
    count+=1
while True:
    value = input("type in the number:")
    if value=='q':
        break
    number=int(value)
    if number%2==0:
        print("even number")
    else:
        print("you did not type in correct number")


