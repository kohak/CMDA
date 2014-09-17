#Andrew Koh
#CS 3654
#9/1/2014
#HW1

#https://github.com/kohak

#1
?read.table
getwd()
setwd("C:\\Users\\kohza_000\\Desktop\\CMDA\\CMDA\\R")
read.table("Data Sets\\prices.txt", col.names=c("Col 1", "Col 2", "Col 3", "Col 4"))
#row.names is just like col.names; it labels each of the rows with a name.  
read.csv("Data Sets\\prices.csv") #Did read.table as well as read.csv
myTable <- read.table("Data Sets\\Hw1.txt", col.names=c("a", "b", "c"))
myTable
a <- myTable$a
a
b <- myTable$b
b
c <- myTable$c
c



#2
?cbind
MAT1 <- cbind(1, c(1,1,3,4), c(3, 4, 1, 6), c(1, 1, 12, 1))
#?matrix
#MAT1 <- matrix(1, nrow=4, ncol=4)
MAT1[4, 4]
t(MAT1) #transpose
solve(MAT1) #inverse



#3
fpe <- read.table("http://data.princeton.edu/wws509/datasets/effort.dat")
fpe

colnames(fpe)
rownames(fpe)
?head
head(fpe, 12)
#prints out the first n rows of table x in function head(x, n)
write.table(fpe, "mydata.txt", sep="\t") 
write.table(fpe, "mydata.csv", sep=",") 

