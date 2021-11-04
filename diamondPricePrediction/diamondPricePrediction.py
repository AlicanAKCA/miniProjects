# Dataset : https://raw.githubusercontent.com/tidyverse/ggplot2/master/data-raw/diamonds.csv
# Alican AKCA - 20.01.2021

#### Required Libraries

# For Visualization and Calculation
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.pylab as pylab
import seaborn as sns
import numpy as np
import re
import pandas as pd

# For Processing and Prediction Models

from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from xgboost import XGBRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_squared_error
from sklearn import metrics
from sklearn.model_selection import cross_val_score

# Loading Dataset
diamondsData=pd.read_csv('https://raw.githubusercontent.com/tidyverse/ggplot2/master/data-raw/diamonds.csv') # Or you can use csv file directory.

# Encoding Labels, This dataset has a categorical data in columns

encoding_diamondsData = diamondsData.copy()
dataTypesOf_diamondsData = (diamondsData.dtypes =="object")
objectColumns = list(dataTypesOf_diamondsData[dataTypesOf_diamondsData].index)

# Applying label encoder to these columns.

label_encoder = LabelEncoder()
for enc in encoding_diamondsData:
    encoding_diamondsData[enc] = label_encoder.fit_transform(encoding_diamondsData[enc])

# We are preparing data.
X= encoding_diamondsData.drop(["price"],axis =1)
y= encoding_diamondsData["price"]

# We separated the prepared data for testing and training. We can change the separation rate.

x_train, x_test, y_train, y_test = train_test_split(X, y,test_size=0.33, random_state=7)

# Scaling process

sc=StandardScaler()
X_train = sc.fit_transform(x_train)
X_test = sc.transform(x_test)

# We gave our data to our 1st model

lr = LinearRegression()
lr.fit(X_train,y_train)
lr_predictedData = lr.predict(X_test)

# We gave our data to our 2nd model

dtr = DecisionTreeRegressor()
dtr.fit(X_train,y_train)
dtr_predictedData = dtr.predict(X_test)

# We gave our data to our 3th model

rfr = RandomForestRegressor()
rfr.fit(X_train,y_train)
rfr_predictedData = rfr.predict(X_test)

# We gave our data to our 4th model

knn = KNeighborsRegressor()
knn.fit(X_train,y_train)
knn_predictedData = knn.predict(X_test)

# We gave our data to our 5th model

xgb = XGBRegressor()
xgb.fit(X_train,y_train)
xgb_predictedData = xgb.predict(X_test)

# We applied cross-validation process. 
# We will list the results, look at the scores and find the best model.

cv_scores = []
cv_scores.append(cross_val_score(lr,X_train,y_train,scoring="neg_root_mean_squared_error", cv=10))
cv_scores.append(cross_val_score(dtr,X_train,y_train,scoring="neg_root_mean_squared_error", cv=10))
cv_scores.append(cross_val_score(rfr,X_train,y_train,scoring="neg_root_mean_squared_error", cv=10))
cv_scores.append(cross_val_score(knn,X_train,y_train,scoring="neg_root_mean_squared_error", cv=10))
cv_scores.append(cross_val_score(xgb,X_train,y_train,scoring="neg_root_mean_squared_error", cv=10))

for i in cv_scores:
    print(i)
    
# The result is usually not surprising,
# Let's do the guesswork on the XGBoost model

pred = xgb.predict(X_test)

# Let's also use the R-Squared method for verification

print("R^2:",metrics.r2_score(y_test, pred))
print("Adjusted R^2:",1 - (1-metrics.r2_score(y_test, pred))*(len(y_test)-1)/(len(y_test)-X_test.shape[1]-1))

# Visualization 

plt.figure(figsize=(15,10))
plt.title('Model Evaluation')
plt.scatter(range(0,len(X_test)),y_test,label='True',s=3, color = "blue")
plt.scatter(range(0,len(X_test)),pred,label='Predicted',s=3, color = "orange")
plt.xlabel('Index')
plt.ylabel('Price')
plt.legend()
plt.show()