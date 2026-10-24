# l1=[2,3,4,7,8,10]
# l2=[1,2,5,6,7,9]
# l3=[]
# # for i in range (len(l1)):
# #     print(f"at index {i}, {i}th value lf l1 is {l1[i]} and {i}th valuse of l2 is {l2[i]}")
# #     if l1[i]<l2[i]:
# #         l3.append(l1[i])
# #         l3.append(l2[i])
# #     else:
# #         l3.append(l2[i])
# #         l3.append(l1[i])
# #     print(l3)

# # print("\n\n Enter l4:  \n")
# # user_input=input()
# # l4 = [int(x.strip()) for x in user_input.split(',')]
# # print(l4)
# # print(type(l4))

# # print("\n \n Enter l5:  \n")
# # user_input1=input()
# # l5 = [int(x.strip()) for x in user_input1.split(',')]
# # print(l5)
# # print(type(l5))

# temp=input("enter list:  ")
# for i in temp.split(','):
#     l9=i.strip()
# print(l9)
# print(type(l9))


def zata(str1):
    lst=[]
    sol=""
    cnt=0
    for i in str1:
        if i in lst:
            cnt+=1
        else:
            lst.append(i)
            if cnt >=1:
                sol=sol+str(cnt)
            sol=sol+str(i)
            cnt = 1
    sol=sol+str(cnt)
    print(sol)
    print(type(sol))
zata("aaabbc")


# str1=""
# print(str1)
# str2="bb"
# print(str2)
# str1=str1+str2
# print(str1)
# str3=3
# str1=str1+str(str3)
# print(str1)

# echo "# python-100-codes" >> README.md
# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/salgarhariom/python-100-codes.git
# git push -u origin main