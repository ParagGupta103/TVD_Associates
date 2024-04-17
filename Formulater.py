import pandas as pd
from sklearn.preprocessing import StandardScaler
import os

#Seeting Up Path
file_path = '/Users/paraggupta/Desktop/Externship/data/Dataset_1_Full.xlsx'
data = pd.read_excel(file_path)

#Data cleaining
data.columns = data.iloc[0]
data = data[1:]
threshold = len(data) * 0.9
data = data.dropna(thresh=threshold, axis=1)

#Defining Numeric Columns 
numeric_cols = ['Amount Paid', 'Balance']
data[numeric_cols] = data[numeric_cols].apply(pd.to_numeric, errors='coerce')

#defining Categorical Columns

#For the Title column, Maybe we can assingn 1 to anyone who has director in their Title and give extra points for that ?
categorical_cols = ['[Member Status]','[Memeber Type]', '[Address | Main | Country',]
for col in categorical_cols:
    data[col].fillna(data[col].mode()[0], inplace=True)
data['Date Registered'] = pd.to_datetime(data['Date Registered'], errors='coerce')

#Scaling Every Numeric Column to standard distribution ( mean = 0, sd = 1)
scaler = StandardScaler()
data[numeric_cols] = scaler.fit_transform(data[numeric_cols])

#Create Two new Cols for Registration Year and Registration Month
data['Year Registered'] = data['Date Registered'].dt.year
data['Month Registered'] = data['Date Registered'].dt.month

#data.dropna(inplace=True)
#data.reset_index(drop=True, inplace=True)

#Save the New Data to a new file
new_file_path = '/Users/paraggupta/Desktop/Externship/data/Cleaned_Dataset_Full.csv'
data.to_excel(new_file_path, index=False)
