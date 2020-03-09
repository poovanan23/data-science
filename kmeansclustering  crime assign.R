library(readr)
crime_data <- read_csv("C:/Users/POOVAYUVA/Desktop/EXCELR ASSIGN/CLUSTERING/crime_data.csv")
View(crime_data)

crimrem <- scale(crime_data[,-1])

d <- dist(crimrem,method = "euclidean")

km <- kmeans(d,4)

str(km)

library(animation)

km1 <- kmeans.ani(d,4)

#hclust

modelhc<-hclust(d,method ="complete")

plot(modelhc,hang=-1)

?rect.hclust()

rect.hclust(modelhc,k=4)

