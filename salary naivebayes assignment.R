library(readr)
SalaryData_Train <- read_csv("C:/Users/POOVAYUVA/Desktop/EXCELR ASSIGN/NAIVE/SalaryData_Train.csv")
View(SalaryData_Train)

library(readr)
SalaryData_Test <- read_csv("C:/Users/POOVAYUVA/Desktop/EXCELR ASSIGN/NAIVE/SalaryData_Test.csv")
View(SalaryData_Test)

SalaryData_Train$Salary <- as.factor(SalaryData_Train$Salary)
str(SalaryData_Train)

SalaryData_Test$Salary <- as.factor(SalaryData_Test$Salary)
str(SalaryData_Test)

library(e1071)
modelsalary <-naiveBayes(Salary~.,data=SalaryData_Train)
View(modelsalary)
prediction <- predict(modelsalary,newdata = SalaryData_Test)
View(prediction)

library(caret)
cfm <- confusionMatrix(prediction,SalaryData_Test$Salary)
View(cfm)
