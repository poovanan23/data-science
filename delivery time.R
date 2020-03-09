library(readr)
delivery_time <- read_csv("C:/Users/POOVAYUVA/Desktop/EXCELR ASSIGN/SIMPLE LINEAR/delivery_time.csv")
View(delivery_time)

attach(delivery_time)

plot(delivery_time$`Delivery Time`,delivery_time$`Sorting Time`)

cor.test(delivery_time$`Delivery Time`,delivery_time$`Sorting Time`) #0.82

dt <- lm(delivery_time$`Delivery Time`~delivery_time$`Sorting Time`,data =delivery_time)
summary(dt) #0.6655

error=(delivery_time$`Delivery Time`- dt$fitted.values)
rmsen=sqrt(mean(error^2))


#logrithmic transformation

attach(delivery_time)
plot(log(`Sorting Time`),`Delivery Time`)
cor.test(log(`Sorting Time`),`Delivery Time`) #0.83 
dtl <- lm(`Delivery Time`~log(`Sorting Time`),data=delivery_time)
summary(dtl)  #0.6794
error=(`Delivery Time`- dtl$fitted.values)
rmsel=sqrt(mean(error^2))


#exponential
attach(delivery_time)

cor.test(`Sorting Time`,log(`Delivery Time`)) #0.8431
dte <- lm(log(`Delivery Time`)~`Sorting Time`,data=delivery_time)
summary(dte) #0.6957
exp(dte$fitted.values)
exerroe <-`Delivery Time`-exp(dte$fitted.values)
rmsee <- sqrt(mean(exerroe^2))


#quadratic equation
plot(`Sorting Time`,`Delivery Time`)
plot(`Sorting Time`^2,`Delivery Time`)
plot (`Sorting Time`^2,log(`Delivery Time`)
cor.test(`Sorting Time`^2,log(`Delivery Time`)) #0.7882452
qddt <- lm(log(`Delivery Time`)~`Sorting Time`+I(`Sorting Time`^2),data=delivery_time)
summary (qddt) #0.7387

exp(qddt$fitted.values)
errorq <- `Delivery Time`-exp(qddt$fitted.values)
rmseq <- sqrt(mean(errorq^2)) #2.799

#since quadratic transformation gives the better Adjusted R-squared value=0.7387
#hence qddt will be the better model.

