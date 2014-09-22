#HW2
#Andrew Koh
#https://github.com/kohak/CMDA

getwd()
setwd("C:\\Users\\kohza_000\\Desktop\\CMDA\\CMDA")

load('phsample.rdata')

summary(dhus)
summary(dpus)
#2
#dhus and dpus are large data sets with similar variables 
#The data sample is a list of all the PUMS data of a single
#person/household with lots of information for each unit
#including occupation, level of education, personal income, etc.

#3
psub = subset(dpus,with(dpus,(PINCP>1000)&(ESR==1)&
                          (PINCP<=250000)&(PERNP>1000)&(PERNP<=250000)&
                          (WKHP>=40)&(AGEP>=20)&(AGEP<=50)&
                          (PWGTP1>0)&(COW %in% (1:7))&(SCHL %in% (1:24))))  #Subset of data matching metrics for employment conditions

psub$SEX = as.factor(ifelse(psub$SEX==1,'M','F'))  #sets gender info into a readable form and more levels
psub$SEX = relevel(psub$SEX,'M')                   #makes it so M and F are encoded differently in the model
cowmap <- c("Employee of a private for-profit",   #sets working class info into
            "Private not-for-profit employee",    #a readable form and more levels
            "Local government employee",
            "State government employee",
            "Federal government employee",
            "Self-employed not incorporated",
            "Self-employed incorporated")
psub$COW = as.factor(cowmap[psub$COW])
psub$COW = relevel(psub$COW,cowmap[1])
schlmap = c(                                 
  rep("no high school diploma",15),   #sets education info into
  "Regular high school diploma",      #a readable form and more levels
  "GED or alternative credential",
  "some college credit, no degree",
  "some college credit, no degree",
  "Associate's degree",
  "Bachelor's degree",
  "Master's degree",
  "Professional degree",
  "Doctorate degree")
psub$SCHL = as.factor(schlmap[psub$SCHL])
psub$SCHL = relevel(psub$SCHL,schlmap[1])
dtrain = subset(psub,ORIGRANDGROUP >= 500) #Subset of data rows for model training
dtest = subset(psub,ORIGRANDGROUP < 500)  #Subset of data rows for model testing

summary(dtrain$COW) #Gives a summary of the COW column of the dtrain data


#We picked a dataset called cars93 containing 93 entries with 28 different variables for
#each car
carsData <- read.csv("cars93.csv")

#The data was retrieved from http://vincentarelbundock.github.io/Rdatasets/datasets.html
#The data is Data from 93 Cars on Sale in the USA in 1993 
#All of the data is information about each model of the car that people would like to know
#before buying the car such as price, MPG, cyllinders, etc.  Each one has a name
#and a manufacturer that helps identify the car type.  
