library(readr)
forestfires <- read_csv("C:/Users/POOVAYUVA/Desktop/EXCELR ASSIGN/SVM ASSIGN/forestfires.csv")
View(forestfires)

Y <- forestfires[,31]

FF <- forestfires[,c(-1,-2,-31)]

final <- scale(FF)

combine <- cbind(final,Y)

traindata <- combine[1:300,]

testdata <- combine[301:517,]

testdata$size_category <- as.factor(testdata$size_category)
str(testdata)
 traindata$size_category <- as.factor(traindata$size_category)
 str(traindata)

library(kernlab)
?ksvm


forestmodel <- ksvm(size_category~.,data=traindata,kernel=anovadot())

prediction <- predict(forestmodel,testdata)
View(prediction)

library(caret)

cf <-confusionMatrix(prediction,testdata$size_category) #accuracy=0.8848








