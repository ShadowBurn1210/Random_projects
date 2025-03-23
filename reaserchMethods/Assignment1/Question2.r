setwd("c:/Users/Admin/PycharmProjects/RandomProjects/Random_projects/reaserchMethods/Assignment1")
library(MASS)

apartment.data <- read.table("Apartments.txt", header = TRUE)
# Read the file using the tab delimiter
apartment <- data.frame(apartment.data)

# step.reg.data <- step(lm(SalePrice ~ Number+Age+LotSize, data = apartment), direction = "both")

# summary(step.reg.data)
reg.data <- lm(SalePrice ~ Number+Age+LotSize, data = apartment)

summary(reg.data)
