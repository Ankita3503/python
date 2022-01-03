# l1=[1,2,3,2,3,5,4,1]
# l2=[]
# for i in l1:
#     if i not in l2:
#         l2.append(i)
# print('''After the Removing the duplicate element's List will be a =>''',l2)
# #l2.short()
# print(l2.short())
l=['yash',120,'hi',30,10]
su=0
for i in l:
    if type(i)== int:
        su+=i
print(su)