import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.metrics import r2_score


df = pd.read_excel('Dataset\pokemon.xlsx')

# Handle missing values
df.dropna(subset=['sp_attack', 'sp_defense', 'speed'], inplace=True)

# convert attack, defense, sp_attack, sp_defense, speed to float
df['attack'] = df['attack'].astype(float)
df['defense'] = df['defense'].astype(float)
df['sp_attack'] = df['sp_attack'].astype(float)
df['sp_defense'] = df['sp_defense'].astype(float)
df['speed'] = df['speed'].astype(float)

# Create a new column called total_stats
df['total_stats'] = df['attack'] + df['defense'] + df['sp_attack'] + df['sp_defense'] + df['speed']

# create bins for each individual stat to make a scatter plot and if the pokemon is legendary change its color
bins = [0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800]
df['attack_bins'] = pd.cut(df['attack'], bins)
df['defense_bins'] = pd.cut(df['defense'], bins)
df['sp_attack_bins'] = pd.cut(df['sp_attack'], bins)
df['sp_defense_bins'] = pd.cut(df['sp_defense'], bins)
df['speed_bins'] = pd.cut(df['speed'], bins)

# Create a scatter plot for each individual stat
plt.figure(figsize=(20, 20))
plt.subplot(3, 2, 1)
plt.scatter(df['attack'], df['total_stats'], c=df['is_legendary'])
plt.xlabel('Attack')
plt.ylabel('Total Stats')
plt.title('Attack vs Total Stats')

plt.subplot(3, 2, 2)
plt.scatter(df['defense'], df['total_stats'], c=df['is_legendary'])
plt.xlabel('Defense')
plt.ylabel('Total Stats')
plt.title('Defense vs Total Stats')

plt.subplot(3, 2, 3)
plt.scatter(df['sp_attack'], df['total_stats'], c=df['is_legendary'])
plt.xlabel('Special Attack')
plt.ylabel('Total Stats')
plt.title('Special Attack vs Total Stats')

plt.subplot(3, 2, 4)
plt.scatter(df['sp_defense'], df['total_stats'], c=df['is_legendary'])
plt.xlabel('Special Defense')
plt.ylabel('Total Stats')
plt.title('Special Defense vs Total Stats')

plt.subplot(3, 2, 5)
plt.scatter(df['speed'], df['total_stats'], c=df['is_legendary'])
plt.xlabel('Speed')
plt.ylabel('Total Stats')
plt.title('Speed vs Total Stats')

plt.show()

X = df[['attack']].values
y = df['total_stats'].values

# perform linear regression on each individual stat
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)
r2_score(y, y_pred)

sorted_indices = np.argsort(X.flatten())
X_sorted = X[sorted_indices]
y_pred_sorted = y_pred[sorted_indices]

# plot the linear regression line
plt.figure(figsize=(10, 10))
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X_sorted, y_pred_sorted, color='red', label='Linear Regression')
plt.xlabel('Attack')
plt.ylabel('Total Stats')
plt.title('Attack vs Total Stats')
plt.legend()
plt.text(X_sorted[0], y_pred_sorted[0], 'R^2 = ' + str(r2_score(y, y_pred)))
plt.grid(True)
plt.savefig('Attack_vs_Total_Stats.png')
plt.show()

X = df[['defense']].values
y = df['total_stats'].values

model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)
r2_score(y, y_pred)

sorted_indices = np.argsort(X.flatten())
X_sorted = X[sorted_indices]
y_pred_sorted = y_pred[sorted_indices]

plt.figure(figsize=(10, 10))
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X_sorted, y_pred_sorted, color='red', label='Linear Regression')
plt.xlabel('Defense')
plt.ylabel('Total Stats')
plt.title('Defense vs Total Stats')
plt.legend()
plt.text(X_sorted[0], y_pred_sorted[0], 'R^2 = ' + str(r2_score(y, y_pred)))
plt.grid(True)
plt.savefig('Defense_vs_Total_Stats.png')
plt.show()

X = df[['sp_attack']].values
y = df['total_stats'].values

model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)
r2_score(y, y_pred)

sorted_indices = np.argsort(X.flatten())
X_sorted = X[sorted_indices]
y_pred_sorted = y_pred[sorted_indices]

plt.figure(figsize=(10, 10))
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X_sorted, y_pred_sorted, color='red', label='Linear Regression')
plt.xlabel('Special Attack')

plt.ylabel('Total Stats')
plt.title('Special Attack vs Total Stats')
plt.legend()

plt.text(X_sorted[0], y_pred_sorted[0], 'R^2 = ' + str(r2_score(y, y_pred)))
plt.grid(True)
plt.savefig('Special_Attack_vs_Total_Stats.png')
plt.show()

X = df[['sp_defense']].values
y = df['total_stats'].values

model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)
r2_score(y, y_pred)

sorted_indices = np.argsort(X.flatten())
X_sorted = X[sorted_indices]
y_pred_sorted = y_pred[sorted_indices]

plt.figure(figsize=(10, 10))
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X_sorted, y_pred_sorted, color='red', label='Linear Regression')
plt.xlabel('Special Defense')
plt.ylabel('Total Stats')
plt.title('Special Defense vs Total Stats')
plt.legend()
plt.text(X_sorted[0], y_pred_sorted[0], 'R^2 = ' + str(r2_score(y, y_pred)))
plt.grid(True)
plt.savefig('Special_Defense_vs_Total_Stats.png')
plt.show()

X = df[['speed']].values
y = df['total_stats'].values

model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)
r2_score(y, y_pred)

sorted_indices = np.argsort(X.flatten())
X_sorted = X[sorted_indices]
y_pred_sorted = y_pred[sorted_indices]

plt.figure(figsize=(10, 10))
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X_sorted, y_pred_sorted, color='red', label='Linear Regression')
plt.xlabel('Speed')
plt.ylabel('Total Stats')
plt.title('Speed vs Total Stats')
plt.legend()
plt.text(X_sorted[0], y_pred_sorted[0], 'R^2 = ' + str(r2_score(y, y_pred)))
plt.grid(True)
plt.savefig('Speed_vs_Total_Stats.png')
plt.show()

# perform linear regression on all stats