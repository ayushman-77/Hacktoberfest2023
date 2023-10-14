def binary_search(list, search):
    x=sorted(list)
    first=0
    last=len(x)-1
    while first<=last:
        mid = (first + last)//2
        if x[mid] < search:
            first = mid + 1
 
        elif x[mid] > search:
            last = mid - 1
 
        else:
            return mid
    return -1

while True:
    li=eval(input("Enter list of ascending integer elements : "))
    k=0
    for i in li:
        if not isinstance(i, int):
            k=1
            break
    if k==1:
        print("Elements should be integers only! Try again")
        print()
        continue
    search=input("Enter element to be searched : ")
    if not search.isdigit():
        print("Search element should be an integer! Try again")
        print()
        continue
    else:
        search=int(search)
    output=binary_search(li,search)
    if output==-1:
        print("Element was not found")
        break
    else:
        print(f"Element found at position {output} of sorted list")
        break
