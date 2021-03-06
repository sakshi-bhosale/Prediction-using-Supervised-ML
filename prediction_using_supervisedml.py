# -*- coding: utf-8 -*-
"""Prediction_Using_SupervisedML.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LNHyiyF3RUMDvBCqdfYmsaY0rfQlekXP

# **Task 1- Prediction using Supervised Machine Learning**

 **Predict the precentage of a student based on the no. of study hours.**

# Author- Sakshi Bhosale

**Importing Libraries**
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import pylab as pl
import seaborn as sns
import matplotlib.pyplot as plt
# %matplotlib inline

"""**Loading the Dataset and Reading the data**"""

url = "http://bit.ly/w-data"
#Reading the data from remote link

df = pd.read_csv(url)
#loading the dataset

"""**Exploring the data**"""

df.head()
#Display first 5 rows

df.tail()
#Display last 5 rows

df.sample(5)
#Display random 5 rows

"""**Exploring the Details**"""

print(df.shape)
#Dimension of dataset

print(df.describe())
#details on the dataset

"""**Data Visualisation**

Scatter Plot
"""

plt.scatter(df.Hours, df.Scores, color='blue')
plt.xlabel("Hours Studied")
plt.ylabel("Percentage Scored")
plt.show()

"""Line Plot"""

sns.lineplot(data=df)
#line chart showing how marks evolved over time

"""**Since the data is linearly arranged, we use Linear Regressions to make predictions**"""

#importing the regression model
from sklearn.linear_model import LinearRegression

"""**Preparing the data for the ML Algorithm**"""

x = df.iloc[:, :-1].values
y = df.iloc[:, 1].values

"""**Creating Training and Testing sets**"""

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,random_state = 0,test_size=0.2)

"""**Initialising and Training the model**"""

regression = LinearRegression()  
regression.fit(x_train, y_train)

print("Training Finished!")

"""**Plotting the Results**"""

sns.barplot(x=df["Hours"], y=df["Scores"])
# Bar chart showing the scores of students vs hours they put in

plt.xlabel("Scores after Study")
# Add label for vertical axis

plt.ylabel("Hours")
# Add label for vertical axis

"""**Comparing the accuracy of the model with actual values**"""

y_pred=regression.predict(x_test)  
prediction=list(y_pred)
df_compare = pd.DataFrame({ 'Actual':y_test,'Result':prediction})
df_compare

from sklearn import metrics
print("Predicted Accuracy :")
metrics.r2_score(y_test,y_pred)

"""**Predictions**"""

Prediction = regression.predict([[9.25]])
print("Predicted score of a student studying 9.25 hours in a day is",Prediction)

"""# **Conclusion-**

From the above model, we predict that if a student studies for 9.25 hours per day then he/she is likely to score 93.69%.

### Thank You
"""