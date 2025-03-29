setwd("c:/Users/Admin/PycharmProjects/RandomProjects/Random_projects/reaserchMethods/Assignment3")

income.data <- read.table("Income.txt", header = TRUE, sep = "\t")

income <- data.frame(income.data)

# Develop confirmatory regression models to predict income from the other variables.

# 1. Fit a regression model with all the variables.
model1 <- lm(RINCOME ~ ., data = income)
summary(model1)
cat("Model equation: RINCOME =", round(coef(model1)[1], 2), "+", 
    round(coef(model1)[2], 2), "* AGE +",
    round(coef(model1)[3], 2), "* EDUC +",
    round(coef(model1)[4], 2), "* HRS1 +",
    round(coef(model1)[5], 2), "* WRKSLF\n")

# regression equation RINCOME = 503.2*Age + 8071.8*EDUC + 749.6*HRS1 + 12281.1*WRKSLF


# Develop stepwise regression models to predict income from the other variables.

# 2. Fit a stepwise regression model
model2 <- step(model1, direction = "both", trace = 0)
summary(model2)
cat("Model equation: RINCOME =", round(coef(model2)[1], 2), "+", 
    round(coef(model2)[2], 2), "* AGE +",
    round(coef(model2)[3], 2), "* EDUC +",
    round(coef(model2)[4], 2), "* HRS1 +",
    round(coef(model2)[5], 2), "* WRKSLF\n")