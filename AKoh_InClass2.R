#Lecture 7

getwd()
setwd("C:\\Users\\kohza_000\\Desktop\\CMDA\\CMDA")

install.packages("ggplot2")
install.packages("hexbin")
library("ggplot2")
library("hexbin")
#The health insurance customer data
load('exampleData.rData')
#Examine data
names(custdata)
dim(custdata)
class(custdata)

#Summary statistics

summary(custdata) #for the entire data frame

#look at individual variables to spot problems

summary(custdata$is.employed)
summary(custdata$income)
summary(custdata$age)

#Question 1 : custdata

#age maximum is 146.7, which is literally negative so that's an outlier
#isemployed has a lot of NAs, which is weird since people are either employed or not employed
#income minimum is negative

uciCar <- read.table(
  'http://www.win-vector.com/dfiles/car.data.csv',
  sep=',',
  header=T
)

summary(uciCar)
summary(uciCar$buying)
summary(uciCar$maint)
summary(uciCar$doors)
summary(uciCar$persons)
summary(uciCar$lug_boot)
summary(uciCar$safety)
summary(uciCar$rating)

#1
#I notice that for buying, maint, doors, the numbers are all 432.  
#I also notice for persons, lug_boot, and safety, the numbers are all 576
#It is also an issue that the high, medium, and low are all the same number, making
#me think that there is some issue with the data for each column of uciCar besides rating

#2
#I notice that everything except for ratings have the same number for big, med, and small.  
#This makes me believe that there was an error in how the data was collected

#3
#
load('credit.rdata')
summary(d)
summary(d$Personal.status.and.sex)
#Most of the men are signle and most of the women are divorced/seperated/married
#For some reason, the only category females were put in is divorced/seperated/married which makes me think
#this data is somewhat flawed
summary(d$Other.debtors)
#There's a lot of data for Other.debtors/guarantors that have none for this summary.  

#4
#Hexbin is similar to a scatterplot but instead of having exact small points, a hexbin plot
#does a gradient sort of thing showing where there's a high amount of data
#5
#I would do a bar graph for number of vehicles and income because there's a small variance
#of number of vehicles and a high amounts of changing for income so there's 2 variables
counts <- table(custdata$num.vehicles, custdata$income)
barplot(counts, main="Number of vehicles and income",
        xlab="Number of vehicles", col=c("darkblue","red"),
        legend = rownames(counts))
#6
#For income less than 30k and recent move, I would do a 2 variable bar graph
#with recent.move to be the x and whether it's true or false to be income < 30
counts <- table(custdata$recent.move)
barplot(counts, main="Number of vehicles and income",
        xlab="Number of vehicles", col=c("darkblue","red"),
        legend = rownames(counts))
