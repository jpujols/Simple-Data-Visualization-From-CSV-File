import pandas as pd
import matplotlib.pyplot as plt
csv_file='healthcare-dataset-stroke-data.csv'
data = pd.read_csv(csv_file)

#Extract two columns from dataset
age = data["age"]
bmi = data["bmi"]

#Store columns in 2 lists
x=[]
y=[]

#Convert dataset to list
x=list(age)
y=list(bmi)

#To draw a scatter plot, we write
#pie chart
#plt.plt.pie(x,labels=y,autopct='%.2f%%')

#bar
#plt.bar(x,y)

#scatter
plt.bar(x,y)
plt.xlabel('Age->')
plt.ylabel('BMI->')
plt.title('HealthCare Dataset Stroke Data')
plt.show()
plt.savefig('chart.png')