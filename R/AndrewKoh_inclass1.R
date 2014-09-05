getwd()
setwd("C:\\Users\\kohza_000\\Desktop\\Data Analytics\\R")
csvData<- read.csv("cars1.csv")

#dimension
dim(csvData)

#variable at (2,2)
var1<-csvData[2, 2]
var1

#print column names
names(csvData)

#print row 1 and row  2
csvData[1]
csvData[2]

#get row speed
SPEED<-csvData$speed
SPEED

#print row 15
csvData[15,]
