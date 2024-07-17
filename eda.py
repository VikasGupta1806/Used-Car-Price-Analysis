# -*- coding: utf-8 -*-
"""eda.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-xVyNRHFKD5sMMl_9FSj5yycS6-nlbSl
"""

import pandas as pd
import numpy as np

df = pd.read_csv("car_prices_cleaned.csv")

print(df.info())
print(df.describe())

from datetime import datetime
import pandas as pd

df['saledate'] = pd.to_datetime(df['saledate'], utc=True)

current_year = datetime.now().year
df['car_age'] = current_year - df['year']

df['sale_month'] = df['saledate'].dt.month
df['sale_year'] = df['saledate'].dt.year

import matplotlib.pyplot as plt
import seaborn as sns

numerical_features = ['sellingprice', 'car_age', 'odometer', 'mmr']
df[numerical_features].hist(bins=30, figsize=(15, 10))
plt.show()

plt.figure(figsize=(15, 10))
for i, feature in enumerate(numerical_features):
    plt.subplot(2, 2, i+1)
    sns.boxplot(x=df[feature])
    plt.title(f'Box Plot of {feature}')
plt.tight_layout()
plt.show()

categorical_features = ['make', 'model', 'body', 'transmission', 'color', 'condition', 'seller', 'state']
for feature in categorical_features:
    plt.figure(figsize=(10, 5))
    df[feature].value_counts().plot(kind='bar')
    plt.title(f'Distribution of {feature}')
    plt.xlabel(feature)
    plt.ylabel('Count')
    plt.show()

plt.figure(figsize=(15, 10))
for i, feature in enumerate(numerical_features):
    plt.subplot(2, 2, i+1)
    sns.scatterplot(x=df[feature], y=df['sellingprice'])
    plt.title(f'Scatter Plot of Selling Price vs {feature}')
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 8))
correlation_matrix = df[numerical_features].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

for feature in categorical_features:
    plt.figure(figsize=(15, 5))
    sns.boxplot(x=df[feature], y=df['sellingprice'])
    plt.title(f'Box Plot of Selling Price by {feature}')
    plt.xticks(rotation=90)
    plt.show()

for feature in categorical_features:
    grouped_df = df.groupby(feature)['sellingprice'].agg(['mean', 'median', 'count']).reset_index()
    print(f'Group-wise Analysis for {feature}')
    print(grouped_df.head())

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

X = df.drop(columns=['sellingprice', 'vin', 'saledate'])
X = pd.get_dummies(X, drop_first=True)
y = df['sellingprice']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
rf_importance = pd.DataFrame(rf.feature_importances_, index=X_train.columns, columns=['Importance'])
rf_importance = rf_importance.sort_values(by='Importance', ascending=False)
print('Random Forest Feature Importance:')
print(rf_importance.head(10))