setwd("C:\\Users\\POOVAYUVA\\Desktop\\POOVANAN Assignment")
library(rvest)
library(XML)
library(magrittr)

# imdb Reviews #############################
aurl <-"https://www.imdb.com/title/tt11138290/?ref_=fn_al_tt_1" 
imdb_reviews <- NULL
for (i in 1:10){
  murl <- read_html(as.character(paste(aurl,i,sep="=")))
  rev <- murl %>%
    html_nodes(".review-text") %>%
    html_text()
  imdb_reviews <- c(imdb_reviews,rev)
}
write.table(imdb_reviews,"movie.txt",row.names = F)

getwd()
