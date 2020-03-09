library(readr)
Zoo <- read_csv("C:/Users/POOVAYUVA/Desktop/EXCELR ASSIGN/knn/Zoo.csv")
View(Zoo)
normal <- function(x){
  return((x-min(x))/(max(x)-min(x)))
}
knn <-lapply(Zoo[,c(-1,-18)], normal)
View(knn)
normknn <- as.data.frame(knn)
View(normknn)
trainingdatazoo <- normknn[1:75,]
testdatazoo <- normknn[76:101,]
traininglabel <- Zoo[1:75,18]
View(traininglabel)
testlabel <- Zoo[76:101,18]
View(testlabel)
library(class)
accuracy=NULL
for(i in 1:74){
  finalknn <- knn(train=trainingdatazoo,test=testdatazoo,cl=traininglabel$type,k=i)
  table <-table(finalknn,testlabel$type)
  accuracy[i] <- sum(diag(table))/sum(table)
}
accuracy
max(accuracy)
plot(accuracy)
