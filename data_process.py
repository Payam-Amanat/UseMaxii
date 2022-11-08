import pandas as pd
import matplotlib.pyplot as plt


#reading data file 
data = pd.read_csv('./new data')



#removing first column
data.drop(['nan'],axis=1,inplace=True)


#removing first row
data.drop([0],axis=0,inplace=True)


#finding the number of missing values
missing_values_numbers = data.isnull().sum()


#replacing missing values with 0 (each column)
data.fillna(0,inplace=True)



#finding values such as : mean,max,std,etc with(describe function)
data.describe()


#now,we choose 2 random columns
first_item  = data['44056'] 
second_item = data['18794'] 

#drawing scatter plot
plt.scatter(first_item,second_item)
plt.show()

#drawing line plot
plt.plot(first_item,second_item)
plt.show()

#end of process



