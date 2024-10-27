import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(color_codes=True)

df=pd.read_csv("D:\Datascience\dataset\socialmedia.csv")
pd.set_option("display.max_columns",20)

# df.info()

df.drop({"UserID",'OS',"Frequency","ConnectionType",'Video ID',"Debt","Video Category","Video Length"},inplace=True,axis=1)

df.columns=df.columns.str.replace(" ","_")
df.columns=df.columns.str.replace("Location","Country")
df.columns=df.columns.str.replace("Total_Time_Spent","Time_Spend")
print(df.isnull().sum())
print(df.describe())
print(df.head(10))


print(df['Gender'].value_counts())

print(df['DeviceType'].value_counts())

print(df['Platform'].value_counts())

print(df['Country'].value_counts())

print(df['Age'].value_counts().mean())

print(df['Addiction_Level'].value_counts())

print(df['Profession'].value_counts())

print(df['CurrentActivity'].value_counts())

print(df['Platform'].value_counts().mean())


sns.countplot(x=df['Platform'],palette="mako")
plt.show()

sns.countplot(x=df['DeviceType'])
plt.show()

sns.histplot(x=df['Country'],palette="Reds")
plt.xticks(rotation=45)
plt.show()

sns.countplot(x=df['Profession'])
plt.xticks(rotation=45)
plt.show()


data=df.groupby('Gender').groups
sizes=[len(data[key]) for key in data]
labels=["Female","Male","Other"]
plt.figure(figsize=(8, 8))
plt.pie(sizes,labels=labels,autopct='%1.1f%%',colors=["Pink","lightblue","Red"], startangle=140)
plt.title('Distribution by Gender')
plt.axis('equal')  
plt.legend()
plt.show()




data=df.groupby('Watch_Reason').groups
sizes=[len(data[key]) for key in data]
labels=["Habit","Boredom","Entertainment","Procastination"]
plt.figure(figsize=(8, 8))
plt.pie(sizes,labels=labels,autopct='%1.1f%%',colors=["Blue","Green","Yellow","Violet"], startangle=140)
plt.title('Distribution by Gender')
plt.axis('equal')  
plt.legend()
plt.show()

