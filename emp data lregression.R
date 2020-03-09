library(readr)
emp_data <- read_csv("C:/Users/POOVAYUVA/Desktop/EXCELR ASSIGN/SIMPLE LINEAR/emp_data.csv")
View(emp_data)

#NORMAL TRANSFORMATION

emp <- lm(emp_data$Churn_out_rate~emp_data$Salary_hike,data =emp_data)
summary(emp) #0.8101


#logrithmic transformation
attach(emp_data)

empl <- lm(Churn_out_rate~log(Salary_hike),data=emp_data)
summary(empl) #0.8297

#exponential transformation

empe <- lm(log(Churn_out_rate)~Salary_hike,data=emp_data)
summary(empe)  #0.8577


#quadratic transformation

empq <- lm(log(Churn_out_rate)~Salary_hike+I(Salary_hike^2),data=emp_data)
summary(empq) #0.9789

#since quadratic transformation gives the better Adjusted R-squared value=0.9789
#hence empq will be the better model.
 
