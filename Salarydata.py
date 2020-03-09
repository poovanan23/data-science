import pandas as pd
import numpy as np
salary=pd.read_csv("C://Users//POOVAYUVA//Desktop//EXCELR ASSIGN//SIMPLE LINEAR//Salary_Data.csv")
sal=salary.describe()


salary.columns

salary.plot.box()

salary.plot.hist()

salarycorr=salary.corr()

salarycorr

import statsmodels.formula.api as sm


model=sm.ols("Salary~Experience",data=salary).fit()

model.summary()

Predicted=model.predict()

salary["log_Experience"] = np.log(salary.Experience)

salary.head()

model2=sm.ols("Salary~log_Experience",data=salary).fit()

model2.summary()

predict2=model2.predict()

salary["log_Salary"] = np.log(salary.Salary)

salary.head()

model3=sm.ols("log_Salary~Experience",data=salary).fit()

model3.summary()

predict3=model3.predict()

model4=sm.ols("log_Salary~log_Experience",data=salary).fit()

model4.summary()

predict4=model4.predict()

salary["x2"] = salary.Experience ** 2

salary.head()

model5=sm.ols("log_Salary~Experience + x2",data=salary).fit()

model5.summary()

predict5=model5.predict()

def RMSE(Pred, Act):

    sq_error=(Pred-Act)**2
    mean_sqerror=np.mean(sq_error)
    root_mean_sqerror=np.sqrt(mean_sqerror)
    return(root_mean_sqerror)
print(RMSE(Predicted,salary.Salary))

print(RMSE(predict2,salary.Salary))

print(RMSE(np.exp(predict3),salary.Salary))
print(RMSE(np.exp(predict4),salary.Salary))


print(RMSE(np.exp(predict5),salary.Salary))

np.mean(Predicted-salary.Salary)

np.mean(predict2-salary.Salary)


