library(readr)
my_movies <- read_csv("C:/Users/POOVAYUVA/Desktop/EXCELR ASSIGN/ARM/my_movies.csv")
View(my_movies)

str(my_movies)

my_movies[] <- lapply(my_movies,as.character)
View(my_movies)

library(arules)


ar <- apriori(my_movies,parameter = list(supp=0.003,confidence=0.7))

inspect(ar[1:10])

itemFrequencyPlot(my_movies,topN=20)

library(arulesViz)

plot(ar[1:20],method="graph")


