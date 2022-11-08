
path = pd.read_csv('./file2.csv')
print(path)



first_Tutorial =  pd.DataFrame({"name":["payam","reza","hassan"],"score":[19,17,18],
"family":["amanat","rezaii","ghaderi"]})

second_Tutorial = pd.DataFrame({"name":["payam","reza","hassan"],"score":[20,16,19],
"family":["amanat","rezaii","ghaderi"]}
)

c = first_Tutorial.join(second_Tutorial,lsuffix=" ")

# join => it sticks the second dataset to the first data set lsuffix is necessry

# merge => it blends dependes on our willing(if name,family,etc are the same and we dont want to print again)
#we write on=["name","family",etc]
# how=>left,right,outer , on => bar hasb chizi ke nemikhaim dobare neshan dade shavad


check_city = path.groupby("City") # ایندکس های تکراری را به ما نشان می دهد
print(check_city.groups) 
