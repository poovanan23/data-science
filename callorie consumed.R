library(readr)
csd <- read_csv("C:/Users/POOVAYUVA/Desktop/EXCELR ASSIGN/SIMPLE LINEAR/calories_consumed.csv")
View(csd)

summary(csd)

#normal transformation
attach(csd)
plot(csd$`Calories Consumed`,csd$`Weight gained (grams)`)
cor.test(csd$`Calories Consumed`,csd$`Weight gained (grams)`) 
caln <- lm(csd$`Weight gained (grams)`~csd$`Calories Consumed`,data =csd)
summary(caln) #0.8882 
error=(csd$`Weight gained (grams)`- caln$fitted.values)
rmse=sqrt(mean(error^2))


#logrithmic transformation

attach(csd)
plot(log(`Calories Consumed`),`Weight gained (grams)`)
cor.test(log(`Calories Consumed`),`Weight gained (grams)`) 
call <- lm(`Weight gained (grams)`~log(`Calories Consumed`),data=csd)
summary(call) #0.7917
error=(csd$`Weight gained (grams)`- call$fitted.values)
rmse=sqrt(mean(error^2))


#exponential transformation

plot(`Calories Consumed`,log(`Weight gained (grams)`))
cor.test(`Calories Consumed`,log(`Weight gained (grams)`))#strong corellation
cale <- lm(log(`Weight gained (grams)`)~`Calories Consumed`,data=csd)
summary(cale) #0.8674
exp(cale$fitted.values)
exerroe <-`Weight gained (grams)`-exp(cale$fitted.values) 
rmse <- sqrt(mean(exerroe^2))


#quadratic equation
plot(`Calories Consumed`,`Weight gained (grams)`)
plot(`Calories Consumed`^2,`Weight gained (grams)`)
plot(`Calories Consumed`^2,log(`Weight gained (grams)`))
cor.test(`Calories Consumed`^2,log(`Weight gained (grams)`))
qd <- lm(log(`Weight gained (grams)`)~`Calories Consumed`+I(`Calories Consumed`^2),data=csd)
summary(qd) #0.8553
exp(qd$fitted.values)
errorq <- `Weight gained (grams)`-exp(qd$fitted.values)
rmseq <- sqrt(mean(errorq^2))


#since normal transformation gives the better Adjusted R-squared value=0.8882
#hence caln will be the better model.
