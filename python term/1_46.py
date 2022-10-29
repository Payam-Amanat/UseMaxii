# num = [1,2,3,4]
# for i in num:
#     print(i)


# name = "payam"
# for i in name:
#     print(i)

# for i in range(1,10):
#     if i%2 == 1 :
#         for m in range(1,6):
#             print(m*"*")
#     else:
#         for c in range(5,0,-1):
#             print(c*"*")
# a=0
# while a<=10:
#     print(a)
#     a +=1

# password = input("enter your password : ")
# real_passwrod = "1234"
# while password != real_passwrod:
#     print("wrong password entered")
#     password = input("enter your passwrd : ")
#     if password == real_passwrod:
#         print("password is correct")



# a = "python"
# b = "HTML"
# c = "CSS"

# programs = [a,b,c]
# print(programs)
# print(len(programs))
# print(len(range(1,10)))
# print(programs[len(programs)-1])

# print("CSS" in programs)
# print("C#" in programs)
#-------------------------------------------------------------22

# color=["red","green","blue"]

# for i in color:
#     print(i)


# i=0
# while len(color)>i:
#     print(color[i])
#     i+=1

#---
# color=["red","green","blue",20]

# for i in color:
#     if type(i)==int:
#         break
#     else:
#         print(i)


# index = 0
# while index<len(color):
#     if type(color[index])==int:
#         break
#     else:
#         print(color[index])
#         index +=1

#---------------------------------------------------------------------23


# names = ["ali","reza","hassan"]

# names.append("sara")  #names.append("sara","baran") = error  just single item can be placed

# names.pop() # last item will be deleted

# names.extend(["sara","baran"]) #several items will be added

# names.insert(1,"shaghayegh") #first item for index number and second for name : names.insert(-1,"hasty")


# b = ['one','two','three']
# names.append(b)
# print(names) #len(names) == 4

#--------------------------------------------------------------------------24

# new = ["one","two","three"]
# # new.clear() #all members will be deleted remains just empty bracket

# new.remove("two") #two will be found and deleted


#---------------------------------------------------------------------------25

# name = ['one',"two","three",20]
# print(name.index("three")) #three's index will be peresented






# name = ['one',"two","three",20,"three",30,40,"three"]
# print(name.index("three",5)) # second place is used for giving the starter place it means
#it wont get started form first place it will be started from fifth place(index) threfore index
#number 7 will be shown due to having three in place number 7 after 5

# print(name.index("three",2,5))#last item is used for saying that till where must be calculated(till index 5)


# print(name.count("three")) # count is used to say the number of the given string



# name.reverse()# it reverses the values in the list(consider that you must write it in specific code line )
# # and than you can print it otherwise an error will be given
# print(name)



# numbers = [3,1,4]
# numbers.sort() # sorting the values(if we do it for a list which has string values,it will be sorted by alphabetical
# order)
# print(numbers)


# numbers = ['a','b']
# p="1".join(numbers)
# print(p)


#---------------------------------------------------------------------------------------------------------26
#list slicing
#[start : end : step]


# values = ["one","two","three","four","five","six","seven","eight","nine","ten"]

# n=values[1:7:2]

# m[:]# all of them

#m[1:]form index number one till end 

#m[-3:] from index third item from the last to end

#m[:9] from 0 till 9

#m[: : 2] all of them by two step step


#m[: : -1] it reverses without using reverse function

# n == m True 
# n is m False


# m = "payam amanat"
# # print(m[: : -1])


# print(m[5: : -1])

#----------------------------------------------------------------------------------------27
# list comprention



# a=[1,2,3,4,5]
# b=[]
# # for i in a:
# #     b.append(i**2)
# # print(b)

# b1 =[i**2 for i in a] # wxactly the last codes but in one line is called list comprention


# name = "payam"
# capitalname=[char for char in name]
# print(capitalname)



# namecapital = [char.upper() for char in name]
# print(namecapital)


# numbers = [1,2,3,4,5,6,7,8,9,10]


# odd =[i for i in numbers if i%2==1]
# even = [n for n in numbers if n%2==0]
# print(f"odd is {odd}")
# print(f"even is {even}")



# test = [x**2 if x%2==0 else x**3 for x in numbers]
# print(test)
#---------------------------------------------------------------------------------------------------28
# a=[[1,2,3],[4,5]]
# print(a[0]) #1,2,3
# print(a[0][1]) # 2

# simple = [i for i in a]
# print(simple)


# for i in a:
#     for m in i:
#         print(m)

# test = [[x for x in i]for i in a]
# print(test)


# nm = [n for n in range(1,4)]
# print(nm)

# test =[[p for p in range(1,4)]for i in range(1,4)] #review again
# print(test)

# test =[["X" if num%2==0 else "O" for num in range(1,4)]for n in range(1,4) ] review again
# print(test)

#----------------------------------------------------------------------------------------------29
#dict
# info ={"name":"ali","age":20,2:"pass"} # first way creating list 
# print(info)

# info2 = dict(name="payam",age=20) #secodn way
# print(info2)


# print(info["name"]) getting name value
# print(info["age"]) getting age value
# print(info[2]) calling 2 value


# for i in info.values(): getting all values by using for loop
#     print(i)


# for i in info.keys(): getting keys 
#     print(i)


# for i,j in info.items(): getting both values and keys all together by calling item function
#     print(f"{i} :  {j}")


# for i in info.items(): it shows but in tuple method
#     print(i)
    
#--------------------------------------------------------------------------------------------30


# info = {"name":"payam","family":"amanat","age":21}

# print("name" in info)

# print("payam" in info.values())

# if "email" in info: checking and taking values if exist
#     print(info["email"])
# else:
#     print("there is not")


# info.clear()
# print(info)


# check = info.copy() #it copies a dict from check
# print(check)

# print(check == info) 
# print(check is info)


# c1={}.fromkeys("name","unknown")
# print(c1)

# c2={}.fromkeys(["name"],"unknown")
# print(c2)

# c3 = {}.fromkeys(["name","family"],"unknown")
# print(c3)

# v = {}.fromkeys("1234","unknown") # extra sample for the first sample
# print(v)


# print(info.get("name")) # the same as the next one but there is only a difference that
# when name object doesnt exist , in get returns None but in typical method returns an error
# print(info["name"])

# print(info.get("city"))
# print(info["city"])

#------------------------------------------------------------------------------------------31

# course ={

#     "title" : "python",
#     "master" : "payam amanat",
#     "video time" : 18,
#     "video count" : 40,
#     "course tags" : ["c",'c#',"c++"],
#     "related course": [{

#               "title" : "HTML",
#               "master" : "rezaii fard",
#               "video time" : 20,
#               "video count" : 50,
#               "course tags" : ["python",'c',"css"]},

#               { 
#               "title" : "c#",
#               "master" : "masomi",
#               "video time" : 10,
#               "video count" : 20,
#               "course tags" : ["c",'python',"java"],
#               }
#    ]}

# # for i in course["related course"]:
# #     print(i["title"])

# # for i in course["related course"]:
# #     print(i["master"])

#------------------------------------------------------------------------------------------------33

# a = dict(item1 = 10 , item2 = 20 , item3 = 30)
# c={key : value for key,value in a.items()} #copy of a like list slicing
# print(c)

# v={key:value**2 for key,value in a.items()}
# print(v)


# l ={n:n for n in [1,2,3,4]} it doesnt need to have a dict before it(just for test)
# print(l)

# n = {i : ("even" if i%2==0 else "odd")for i in [1,2,3,4]}
# # print(n)

#---------------------------------------------------------------------------------------------------34
#tuple 


# a=(1,2,3,4) # the difference between tuple and list is that : the items from tuple can not be changed
# and there arent none of expend , pop , append and ... methods in tuple function.
# if we try to change or replace items from a tuple variable , it will be given an error 

#why do we use tuple?
# its faster , takes less space

# b=tuple([1,2,3,4]) #another wey for writing a tuple

# a={
#     (22,33) : "shiraz",
#     (60,70) : "tehran"
# }
# print(a[(22,33)])


# p =(1,2,3,4,5,6)
# i=0

# while i <= len(a):
#     print(p[i])
#     i +=1


# for i in p:
#     print(i)


# test = (1,2,3,4,5,6,6,"one","one","one","two","two","two")
# print(test.count("one"))
# print(test.index("one"))
# print(test[2:7])

#------------------------------------------------------------------------------------------------35
# a={1,2,3,4,2,3,3,3,4,4,6} # set like the same in math
#repetitive numbers wont be printed

# print(a[0])# an error will be ocurred you cant access to the indexes


# print(4 in a) # true

# b={3,2,1,7,0}
# print(b) #it will be managed 


# for i in a:    # repetitive numbers wont be shown even in if loop
#     print(i)


# c=["a","b",2]
# b=set(c)
# print(c)
# print(b)


# p={'a',1,3,4}
# print(p)


# a.add(1) # adding value but repetitive values wont be added

# a.remove(9) #deleting  from the set but if it doesnt exist it will give you a warning

#for avoiding error we can use of method discard

# a.discard(9)


# a.copy

# a.clear()


# r={x**2 for x in range(10)}
# print(r)


# name = {char for char in 'payam'}
# print(name)
#---------------------------------------------------------------------------------------------------------36 function
# # creating function
# def name():
#     command
#-----------------------------------------------------------------------------------------------37

# def one():
#     return 2*3

# print(one())


# def one():
#     a=3
#     b=4
#     c=a * b
#     return c

# print(one())

#---------------------------------------------------------------------------------------------------38
# def new(x):
#     return x+10

# print(new(1))


# def take(x,y):
#     return x+y

# print(take(10,20))


# def name (firstname,familyname):
#     return firstname +" "+familyname

# print(name("payam","amanat"))


# information = {"name":"payam","family":"amanat"}
# def name (firstname,familyname):
#     return firstname +" "+familyname

# print(name(information["name"],information["family"]))



# number = list(range(9))
# def showname(num):
#     test = 0
#     sum=[]
#     for i in num:
#         if i % 2 == 0:
#             sum.append(i)
#             test +=i
#     print(sum)
#     print(test)


# showname(number)

#-------------------------------------------------------------------------------------------39
# def exponent(power , num):
#     return power * num

# print(exponent(10,2))



# def exponent(power , num=2):
#     return power * num

# print(exponent(10))



# def name(firstname,lastname):
#     return firstname + " " + lastname

# print(name(lastname='amanat',firstname="payam"))

#------------------------------------------------------------------------------------------------40
# def test(*num):
#     total = 0
#     for n in num:
#         total +=n
#     print(total)


# test(1,2,3,4,5) #= *[1,2,3,4,5]



# def test2(name,*number):
#     print(name)
#     total = 0
#     for i in number:
#         total += i
#     print(total)


# test2("payam",1,2,3,4,5)
# we use * when we dont know how many variables we have
#if we write a set of numbers in list we should write a star before it to exteract the numbers from the list
#  *[1,2,3,4,5,6]




# def information(**info):
#     print(info)

# information(name="payam",family="amanat",age=21)

# we use ** when we dont know how many variables will be inputed by user




# def information(**info):
#    for n,m in info.items():
#        print(f"{n} : {m}")

# information(name="payam",family="amanat",age=21)
# we can use for loop due to we have variables and scales





# orders for writing a function
#parametr,*args,defualt parameters,**keyward

# def display(a,b,*args,defpara="defualt",**keyward):
#     return [a,b,*args,defpara,keyward]

# print(display(1,2,6,6,7,8,9,10,defpara="haha",firstname="payam",lastname="amanat"))




# informetion = {"name":"payam","family":"amanat"}
# def namefamily(name,family):
#     return f"name is {name}\nfamily is {family}"

# print(namefamily(**informetion))

#--------------------------------------------------------------------------------------------------41 lambdaa
# lambda 

#a function in a line it can be interpreted in just one line not more

# if we want to convert lambda to function we need to press alt+contrl+f

# one = lambda num : num**2
# print(one(4))


# cal = lambda first,second : first*second
# print(cal(10,20))

# def one():
#     print("hello")

# print(one.__name__)
#__name__ returns functions's name 

#-------------------------------------------------------------------------------------------------------42 map

# num = [1,2,3,4,5]
# # test = map(lambda x:x*2,num) # remember you have to covert map to list always 
# # print(num)
# # print(list(test))
# # print(list(test)) # if we print towice , it will be printed empty list



# name = ["ali","mohamad","sara"]
# check = map(lambda x : x.upper(),name)
# print(list(check))


# info = [{"name":"payam" , "family":"amanat"},{"name":"mohsen" , "family":"gholami"}]
# getting_name = map(lambda x : x["family"],info)
# print(list(getting_name))




# info = [{"name":"payam" , "family":"amanat"},{"name":"mohsen" , "family":"gholami"}]
# mlist = []
# for i in info:
#     mlist.append(i["family"].upper())

# print(mlist)
#---------------------------------------------------------------------------------------------43 filter,all,any
# number = [1,2,3,4,5,6]
# even = filter(lambda x : x%2 == 0 , number)
# print(list(even))

# odd= list(filter(lambda x : x%2==1,number))
# print(f"odd numbers are : {odd}")



# namess = [{"name":"payam","type":["python","js"]},
#         {"name":"sara","type":[]},
#         {"name":"payam","type":[]}
#         ]


# c = filter(lambda x : len(x["type"])==0,namess)#those which are empty
# # print(list(c))




# d=filter(lambda x : not len(x["type"])==0,namess) the item which has type value
# print(list(d))



# f=list(filter(lambda  x : len(x["type"]),namess))
# print(f)




# for i in namess:
#         if len(i["type"]) ==0:
#            print(i)



# h=[x for x in namess if len(x["type"])==0]
# print(h)



#all() it returns true or false => if all values be True will return true but if just one item be 
#false it return false


# number = [1,2,3,4,5] #True
# print(all(number))



# number = [0,1,2,3,4,5]
# print(all(number))


# name = '' #true
# print(all(name))


# a=[2,3,4,6]
# print(all(num %2 == 0 for num in a ))


# any() => if there is only one item true it return true
# a=[1,2,3,5,7]
# print(any(x%2==0 for x in a))
#-----------------------------------------------------------------------------------------------44 sort,max



# numbers = [4,1,3,2,5]
# b=sorted(numbers)
# print(b)

# c=sorted(numbers,reverse=True) it return its reveres
# print(c)


# example = [{"name":'payam',"age":21},{"name":"ali","age":30},{"name":"rezaaa","age":10}]
# b=sorted(example) #error
# print(sorted(example,key=lambda x :x["age"])) ok
# print(sorted(example,key=lambda i : i["age"],reverse=True)) it takes reverse argoman



# numbers = [8,5,2,10,9,3]
# # print(max(numbers)) max  numbers

# char = ["c",'a','z']  max character
# print(max(char))

# names = ["ali","mohsena","payam"] # it return payam why? bcz the first char of name payam is bigger
# print(max(names))

# test =[len(x) for x in names]
# print(test)

# print(max(names,key=lambda x : len(x))) # now it returns mohsena

#-----------------------------------------------------------------------------------------------45 abs,sum,round
# a=[1,2,3,4,5]

# print(len(a))
# print(a.__len__()) both are correct


# b={1,2,3,4,5}
# print(len(b))
# print(b.__len__()) both are correct

#abs
# print(abs(-10)) #it returns posetive form of the given number


# print(sum([1,2,3,4,5,5]))

# a=[1,2,3,4,5]
# print(sum(a))

# c=(1,2,3,4,5)
# print(sum(c))

# a=1.2
# print(round(a)) if the given number be upper than half, it returns to upper number 2

# b=1.7
# print(round(b)) it returns 2

# v=1.23872368
# print(round(v,2)) # it returns 2 number of decimal 

#-----------------------------------------------------------------------------------------------46