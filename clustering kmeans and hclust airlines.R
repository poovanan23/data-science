library(readxl)
EastWestAirlines <- read_excel("C:/Users/POOVAYUVA/Desktop/EXCELR ASSIGN/CLUSTERING/EastWestAirlines.xlsx")
View(EastWestAirlines)

airl <-scale(EastWestAirlines[,-1])

#hierarichal clustering


d <- dist(airl,method = "maximum")



modelhc<-hclust(d,method ="complete")

plot(modelhc,hang=-1)

?rect.hclust()

rect.hclust(modelhc,k=4)

?cutree

ct <- cutree(modelhc,k=4)

as.data.frame(ct)

final <-cbind(EastWestAirlines,ct)

write.csv(final,file = "airlines1.csv")


#kmeans clustering

km <- kmeans(d,4)

str(km)

library(animation)

km1 <- kmeans.ani(d,4)
