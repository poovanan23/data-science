library(readr)
sms <- read_csv("C:/Users/POOVAYUVA/Desktop/EXCELR ASSIGN/NAIVE/sms_raw_NB.csv")
View(sms)

trainsms <- sms[1:4000,]
View(trainsms)

trainsms$type <- as.factor(trainsms$type)
str(trainsms)

testsms <- sms[4001:5559,]
View(testsms)

testsms$type <- as.factor(testsms$type)
str(testsms)

library(e1071)
modelsms <-naiveBayes(type~.,data=trainsms)
View(modelsms)
prediction <- predict(modelsms,newdata = testsms)
View(prediction)

library(caret)
cfm <- confusionMatrix(prediction,testsms$type)
View(cfm)
