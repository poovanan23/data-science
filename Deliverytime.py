import pandas as pd
import numpy as np
delivery=pd.read_csv("C://Users//POOVAYUVA//Desktop//EXCELR ASSIGN//SIMPLE LINEAR//delivery_time.csv")
delivery.plot.box()


delivery.plot.hist()

deliverycorr=delivery.corr()

deliverycorr

import statsmodels.formula.api as sm

model=sm.ols("Delivery~Sorting",data=delivery).fit()

model.summary()

Predicted=model.predict()

delivery["log_Sorting"] = np.log(delivery.Sorting)

delivery.head()

model2=sm.ols("Delivery~log_Sorting",data=delivery).fit()

model2.summary()

predict2=model2.predict()

delivery["log_Delivery"] = np.log(delivery.Delivery)

delivery.head()

model3=sm.ols("log_Delivery~Sorting",data=delivery).fit()

model3.summary()

predict3=model3.predict()

model4=sm.ols("log_Delivery~log_Sorting",data=delivery).fit()

model4.summary()

predict4=model4.predict()

delivery["x2"] = delivery.Sorting ** 2

delivery.head()

model5=sm.ols("log_Delivery~Sorting + x2",data=delivery).fit()

model5.summary()

predict5=model5.predict()

def RMSE(Pred, Act):

    sq_error=(Pred-Act)**2

    mean_sqerror=np.mean(sq_error)
    root_mean_sqerror=np.sqrt(mean_sqerror)
    return(root_mean_sqerror)
print(RMSE(Predicted,delivery.Delivery))

print(RMSE(predict2,delivery.Delivery))

print(RMSE(np.exp(predict3),delivery.Delivery))

print(RMSE(np.exp(predict4),delivery.Delivery))

print(RMSE(np.exp(predict5),delivery.Delivery))

np.mean(Predicted-delivery.Delivery)

np.mean(predict2-delivery.Delivery)
