import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
cal=pd.read_csv("C://Users//POOVAYUVA//Desktop//EXCELR ASSIGN//SIMPLE LINEAR//calories_consumed.csv")
cal.columns
plt.hist(cal.Calories)
plt.boxplot(cal.Calories,0,"rs",0)

plt.hist(cal.Weight)
plt.boxplot(cal.Weight)
plt.plot(cal.Calories,cal.Weight,"bo");plt.xlabel("Cal consumed");plt.ylabel("Wt gained")
cal.Weight.corr(cal.Calories)
np.corrcoef(cal.Weight,cal.Calories)
import statsmodels.formula.api as smf
model=smf.ols("Weight~Calories",data=cal).fit()
model.params
model.summary()
model.conf_int(0.05)
pred=model.predict(cal.iloc[:,1])

plt.scatter(x=cal['Calories'],y=cal['Weight'],color='red');plt.plot(cal['Calories'],pred,color='black');plt.xlabel('CAL');plt.ylabel('WT')

pred.corr(cal.Weight) 

# Transforming variables for accuracy
model2 = smf.ols('Weight~np.log(Calories)',data=cal).fit()
model2.params
model2.summary()
print(model2.conf_int(0.01)) # 99% confidence level
pred2 = model2.predict(pd.DataFrame(cal['Calories']))
pred2.corr(cal.Weight)
# pred2 = model2.predict(wcat.iloc[:,0])
pred2
plt.scatter(x=cal['Calories'],y=cal['Weight'],color='green');plt.plot(cal['Calories'],pred2,color='blue');plt.xlabel('CAL');plt.ylabel('WT')

# Exponential transformation
model3 = smf.ols('np.log(Weight)~Calories',data=cal).fit()
model3.params
model3.summary()
print(model3.conf_int(0.01)) # 99% confidence level
pred_log = model3.predict(pd.DataFrame(cal['Calories']))
pred_log
pred3=np.exp(pred_log)  # as we have used log(AT) in preparing model so we need to convert it back
pred3
pred3.corr(cal.Weight)
plt.scatter(x=cal['Calories'],y=cal['Weight'],color='green');plt.plot(cal.Calories,np.exp(pred_log),color='blue');plt.xlabel('CAL');plt.ylabel('WT')
resid_3 = pred3-cal.Weight
student_resid = model3.resid_pearson 
student_resid
plt.plot(model3.resid_pearson,'o');plt.axhline(y=0,color='green');plt.xlabel("Observation Number");plt.ylabel("Standardized Residual")

# Predicted vs actual values
plt.scatter(x=pred3,y=cal.Weight);plt.xlabel("Predicted");plt.ylabel("Actual")

# Quadratic model
cal["Calories_Sq"] = cal.Calories*cal.Calories
model_quad = smf.ols("Weight~Calories+Calories_Sq",data=cal).fit()
model_quad.params
model_quad.summary()
pred_quad= model_quad.predict(cal.Calories)

model_quad.conf_int(0.05) # 
plt.scatter(cal.Calories,cal.Weight,c="b");plt.plot(cal.Calories,pred_quad,"r")

plt.scatter(np.arange(109),model_quad.resid_pearson);plt.axhline(y=0,color='red');plt.xlabel("Observation Number");plt.ylabel("Standardized Residual")

plt.hist(model_quad.resid_pearson) # histogram for residual values 

