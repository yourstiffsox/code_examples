from matplotlib import pyplot as plt
import pandas as pd
import statsmodels.api as sm
import numpy as np


# create dataframe
diabetes = pd.read_csv('/Users/ryanw/OneDrive/Desktop/diabetes.csv')
diabetes.replace('O', '0', inplace=True)
print(diabetes.Outcome)
# create two new dataframes without the null values
diabetes_bp = diabetes.BloodPressure[diabetes.BloodPressure > 0]
diabetes_bp = diabetes_bp.reset_index()
diabetes_bmi = diabetes.BMI[diabetes.BMI > 0]
diabetes_bmi = diabetes_bmi.reset_index()
# preform an inner merge to keep only the rows in common
diabetes_bp_bmi = pd.merge(diabetes_bp, diabetes_bmi)
# fit a model based on the new dataframe
model = sm.OLS.from_formula('BloodPressure ~ BMI', data=diabetes_bp_bmi)
results = model.fit()
# plot blood pressure against bmi
x = diabetes_bp_bmi.BMI
y = diabetes_bp_bmi.BloodPressure
plt.figure(figsize=(12, 12))
ax1 = plt.subplot(1, 1, 1)
ax1.scatter(x, y)
ax1.set_ylabel('Blood Pressure')
ax1.set_xlabel('BMI')
# plot a least squares line through the scatter plot
line = ax1.plot(x, results.params[1] * x + results.params[0], color='red')
plt.ylim(40, 100)
plt.xlim(20, 50)
plt.legend((line), ('OLS line',), loc=1, prop={'size': 20})
plt.show()
# compare mean of the predictions to the mean of the actual data
print(np.mean(results.predict()))
print(np.mean(diabetes_bp_bmi.BloodPressure))


plt.show()
