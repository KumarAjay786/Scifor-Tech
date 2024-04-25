# -*- coding: utf-8 -*-
"""bimal_economic.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vLh8AT_68MyrYlL0NsD0h5a3_KvAChF3
"""

import pandas as pd

import seaborn as sns

import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression

df = pd.read_csv("/content/salesforcourse-4fe2kehu.csv")
df.head()

df.info()

df.tail()

#Removes the row 34866 due to nan values
df = df.drop(34866, axis=0)

#Delete data in last column "Column1"
df = df.drop('Column1', axis=1)

# Convert "Customer Age, Year,and Quantity " column to integer format
df['Customer Age'] = df['Customer Age'].astype(int)
df['Year'] = df['Year'].astype(int)
df['Quantity'] = df['Quantity'].astype(int)

# Convert "Date" column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# extract month and year
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month

df.head(10)

state_revenue = df.groupby('State')['Revenue'].mean()
state_revenue.sort_values(ascending=False).plot.bar()

df['Customer Age'].plot(kind='hist', bins=20, title='Customer Age')
plt.gca().spines[['top', 'right',]].set_visible(False)

# Plot the average sales for each month
df.groupby('Month')['Revenue'].mean().plot(kind='bar')
plt.show()

# Calculate profit for each product
df['profit'] = df['Revenue'] - df['Cost']

df.describe()

# Group data by Revenue and month

Month_Revenue = df.groupby(['Year'])['Revenue'].sum().reset_index()

sns.relplot(data=Month_Revenue, x="Year", y="Revenue", kind="line", height =5)

monthly_cost = df.groupby(['Year'])['Cost'].sum().reset_index()

sns.relplot(data=monthly_cost, x="Year", y="Cost", kind="line", height =5)

grouped = df.groupby(["Year"])[['Cost', 'Revenue', 'profit']].sum().reset_index()
grouped

# prompt: Using dataframe df: use sk learn and do some basic things like linear regression ,give the full code

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df[['Unit Cost', 'Unit Price']], df['profit'], test_size=0.25)

# Create a linear regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions on the testing set
y_pred = model.predict(X_test

# Split the data into training and testing sets
X = df[['Quantity', 'Unit Cost', 'Unit Price']]
y = df['profit']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

# Create a linear regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

print(X_test)

# Make predictions
y_pred = model.predict(X_test)

print(f"Predicted value: {y_pred}")

"""The `y_pred` variable contains an array of predicted values for the profit based on the input features (`Quantity`, `Unit Cost`, and `Unit Price`) in the test set. Each element in the array corresponds to a row in the test set.

The output `Predicted value: [25.69738409 -70.04317325  60.66122807]` indicates that the model predicts the profit for the first 3 rows in the test set to be 25.69738409 ,-70.04317325 , 60.66122807,......... respectively.


"""

# to check the model score
accuracy = model.score(X_test,y_test)
print(f"accuracy of the model is {accuracy*100:.2f}%")

# to create a new column and put all the y_pred value respectively
# and put the rest rows value as 0/


# df['y_pred'] = 0
# df.loc[X_test.index, 'y_pred'] = y_pred