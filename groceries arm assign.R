library(readr)
groceries <- read_csv("C:/Users/POOVAYUVA/Desktop/EXCELR ASSIGN/ARM/groceries.csv")
View(groceries)

summary(groceries)

library(arules)

ar <- apriori(groceries,parameter = list(supp=0.002,confidence=0.5))

inspect(ar[1:10])

itemFrequencyPlot(groceries,topN=10)

library(arulesViz)

plot(ar[1:10],method="graph")

