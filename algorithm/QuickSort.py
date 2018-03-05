def quickSort(input,i,j):
    if(i>=j):
        return
    anchorI=i
    anchorJ=j
    anchor=input[i]
    while i<j:
        while j>i and input[j]>=anchor:
            j=j-1
        while i<j and input[i]<=anchor:
            i=i+1
        if(i<=j):
            input[i],input[j]=input[j],input[i]
    if(j>=i):
        input[anchorI],input[j]=input[j],input[anchorI]
        quickSort(input,anchorI,j)
        quickSort(input,j+1,anchorJ)
    

#list=[20,3,5,32,6,7,2,4,13,43,54,23,233,543,12]
list=[9,8,7,6,5,4,3,2,1,0]
quickSort(list,0,len(list)-1)
print(list)
