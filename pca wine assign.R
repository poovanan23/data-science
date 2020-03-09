library(readr)
wine <- read_csv("C:/Users/POOVAYUVA/Desktop/EXCELR ASSIGN/pca/wine.csv")
View(wine)

w <- wine[,-1]

pca <- prcomp(w,scale. = TRUE)

names(pca)

variance <- sqrt(pca$sdev)

proportion <- variance/sum(variance)

plot(proportion,type = "b")

plot(cumsum(proportion),type = "b")

pxfinal <- pca$x

finalpca <- pxfinal[,1:3]


y <- wine[,1]

finalset <- cbind(y,finalpca)


d <- dist(finalset,method = "maximum")



modelhc<-hclust(d,method ="complete")

plot(modelhc,hang=-1)

?rect.hclust()

rect.hclust(modelhc,k=5)

?cutree

ct <- cutree(modelhc,k=5)

as.data.frame(ct)

final <-cbind(wine,ct)

write.csv(final,file = "winecls.csv")


#kmeans clustering

km <- kmeans(d,4)

str(km)

library(animation)

km1 <- kmeans.ani(d,4)

