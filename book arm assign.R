library(readr)
book <- read_csv("C:/Users/POOVAYUVA/Desktop/EXCELR ASSIGN/ARM/book.csv")
View(book)

str(book)

book[] <- lapply(book,as.character)
View(book)

library(arules)


ar <- apriori(book,parameter = list(supp=0.001))

inspect(ar[1:10])

itemFrequencyPlot(book,topN=20)

library(arulesViz)

plot(ar[1:20],method="graph")


