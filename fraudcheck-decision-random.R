library(readr)
fraud <- read.csv(file.choose())
View(fraud)

fraud$Taxable.Income <- ifelse(fraud$Taxable.Income >= 30000,"good","risky")

fraud$Taxable.Income <- as.factor(fraud$Taxable.Income)

library(caTools)
fraudsplit <- sample.split(fraud$Undergrad, SplitRatio = 500/600)

train <- subset(fraud,fraudsplit=="TRUE")
test <- subset(fraud,fraudsplit=="FALSE")

#---DECISION_TREE---

library(C50)

model <- C5.0(Taxable.Income~., data = train)
plot(model)
View(model)

final <- C5.0(Taxable.Income~., data = test)
plot(final)

predvalues <- predict(model, newdata = test)
table <- table(test$Taxable.Income,predvalues)
accuracy <- sum(diag(table))/sum(table)
accuracy  #80percent

#--RANDOM_FOREST---

library(randomForest)
model2 <- randomForest(Taxable.Income~., data = train)
plot(model2)

final2 <- randomForest(Taxable.Income~., data = test)
plot(final2)

predvalues2 <- predict(model2, newdata = test)
table2 <- table(test$Taxable.Income,predvalues2)
accuracy2 <- sum(diag(table2))/sum(table2)
accuracy2  #78percent
