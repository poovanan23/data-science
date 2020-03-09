library(readr)
Salary_Data <- read_csv("C:/Users/POOVAYUVA/Desktop/EXCELR ASSIGN/SIMPLE LINEAR/Salary_Data.csv")
View(Salary_Data)

#normal transformation
attach(Salary_Data)

sdn<- lm(Salary~YearsExperience,data =Salary_Data)
summary(sdn)  #0.9554


#logrithmic transformation

sdl<- lm(Salary~log(YearsExperience),data=Salary_Data)
summary(sdl) #0.8487

#exponential transformation

sde <- lm(log(Salary)~YearsExperience,data=Salary_Data)
summary(sde)  #0.9295


#quadratic transformation

sdq <- lm(log(Salary)~YearsExperience+I(YearsExperience^2),data=Salary_Data)
summary(sdq) #0.9448

#since normal transformation gives the better Adjusted R-squared value=0.9554
#hence sdn will be the better model.

