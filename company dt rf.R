library(readr)
company <- read.csv(file.choose())
View(company)


?ifelse
company$Sales<- ifelse(company$Sales>10,"HIGH","LOW")
View(company$Sales)

str(trainc)
company$Sales <- as.factor(company$Sales)
traincompany <- company[1:300,]
View(traincompany)
testcompany <-company[301:400,]
View(testcompany)

library(C50)

model <- C5.0(Sales~.,data = traincompany)
View(model)
plot(model)
modeltest<- C5.0(Sales~.,data = testcompany)
View(modeltest)
plot(modeltest)
predvalue <- predict(model,newdata = testcompany)
table <-table(predvalue,testcompany$Sales)
View(table)
accuracy <- sum(diag(table))/sum(table)
accuracy #80%

library(randomForest)
?randomForest
modelrf <- randomForest(Sales~.,data=traincompany)
View(modelrf)
plot(modelrf)
predrf <- predict(modelrf,newdata=testcompany)
tablerf <-table(predrf,testcompany$Sales)
View(tablerf)

accuracy <- sum(diag(tablerf))/sum(tablerf)
accuracy

library(caret)
confusionMatrix(predvalue,testcompany$Sales)
confusionMatrix(predrf,testcompany$Sales)

