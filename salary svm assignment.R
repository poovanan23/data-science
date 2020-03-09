library(readr)
SalaryData_Train <- read_csv("C:/Users/POOVAYUVA/Desktop/EXCELR ASSIGN/svm/SalaryData_Train.csv")
View(SalaryData_Train)

library(readr)
SalaryData_Test <- read_csv("C:/Users/POOVAYUVA/Desktop/EXCELR ASSIGN/svm/SalaryData_Test.csv")
View(SalaryData_Test)

sdt <- SalaryData_Train[,c(1,4,10,11,12)]

sdt1 <- SalaryData_Train[,c(2,3,5,6,7,8,9,13,14)]

sdtest <- SalaryData_Test[,c(1,4,10,11,12)]
sdtest2 <- SalaryData_Test[,c(2,3,5,6,7,8,9,13,14)]

scalesdt <- scale(sdt)

finaltrain <- cbind(scalesdt,sdt1)

scalesdtest <- scale(sdtest)

testfinal <- cbind(scalesdtest,sdtest2)

testfinal$Salary <- as.factor(testfinal$Salary)
str(testfinal)

finaltrain$Salary <- as.factor(finaltrain$Salary)
str(finaltrain)

library(kernlab)

salarymodel <- ksvm(Salary~.,data=finaltrain,kernel=rbfdot())

prediction <- predict(salarymodel,testfinal)

View(prediction)

library(caret)

cf <-confusionMatrix(prediction,testfinal$Salary)
