library(readr)
glass <- read_csv("C:/Users/POOVAYUVA/Desktop/EXCELR ASSIGN/knn/glass.csv")
View(glass)


class1 <- glass[glass$Type=="1",]
View(class1)
class2 <- glass[glass$Type=="2",]
View(class2)
class3 <- glass[glass$Type=="3",]
View(class3)
class4<- glass[glass$Type=="4",]
View(class4)
class5 <- glass[glass$Type=="5",]
View(class5)
class6 <- glass[glass$Type=="6",]
View(class6)
#
trainclass1 <-class1[1:40,]
View(trainclass1)
testclass1 <- class1[41:70,]
View(testclass1)
#
trainclass2 <- class2[1:40,]
View(trainclass2)
testclass2 <- class2[41:76,]
View(testclass2)
#
trainclass3 <- class3[1:10,]
View(trainclass3)
testclass3 <- class3[11:17,]
View(testclass3)
#
trainclass5 <- class5[1:8,]
View(trainclass5)
testclass5 <- class5[9:13,]
View(testclass5)
#
trainclass6 <- class6[1:6,]
View(trainclass6)
testclass6 <- class6[7:9,]
View(testclass6)
trainfinal <- rbind(trainclass1,trainclass2,trainclass3,trainclass5,trainclass6)
View(trainfinal)
testfinal <- rbind(testclass1,testclass2,testclass3,testclass5,testclass6)
View(testfinal)
normal <- function(x){
  return((x-min(x))/(max(x)-min(x)))
}
knn <-lapply(trainfinal[,-10], normal)
View(knn)

#label
trainlabel <- trainfinal[,10]
View(trainlabel)
testlabel <- testfinal[,10]
View(testlabel)

normknn <- as.data.frame(knn)
View(normknn)

knn1 <- lapply(testfinal[,-10], normal)
View(knn1)

normknnt <- as.data.frame(knn1)
View(normknnt)
accuracy <- NULL
for(i in 1:103){
  finalknn <- knn(train=normknn,test=normknnt,cl=trainlabel$Type,k=i)
  table <-table(finalknn,testlabel$Type)
  accuracy[i] <- sum(diag(table))/sum(table)
}
accuracy
max(accuracy)

