list = [1,2,3,4,5,6,7,8,9,10]

print("original list",list)

n = len(list)//2

newlist = []

for i in range(n):
    newlist.append(list[i])

print("Extracted first five element is: ",newlist)

newlist.reverse()

print("Reversed extracted elements: ",newlist)
