setwd("c:/Users/Admin/PycharmProjects/RandomProjects/Random_projects/reaserchMethods/Assignment3")

customer.data <- read.table("customers.txt", header = TRUE, sep = "\t")

customer <- data.frame(customer.data)

# Develop simple linear regression models based on independent variable Ads

model1 <- lm(Customers ~ Ads, data = customer)
summary(model1)
cat("Model equation: Customers =", round(coef(model1)[1], 2), "+", 
    round(coef(model1)[2], 2), "* Ads\n")

# (c) Create dummy variables to describe the advertising medium
customer.data$I1 <- ifelse(customer.data$Media == 1, 1, 0)
customer.data$I2 <- ifelse(customer.data$Media == 2, 1, 0)


# (d) Conduct a regression analysis with dummy variables
model_multiple <- lm(Customers ~ Ads + I1 + I2, data = customer.data)
summary(model_multiple)

cat("\n--- Multiple Regression Results ---\n")
summary_multiple <- summary(model_multiple)
cat("Model equation: Customers =", 
    round(coef(model_multiple)[1], 2), "+", 
    round(coef(model_multiple)[2], 2), "* Ads +",
    round(coef(model_multiple)[3], 2), "* I1 +",
    round(coef(model_multiple)[4], 2), "* I2\n")

# Create a stepwise regression model
model_stepwise <- step(model_multiple, direction = "both", trace = 0)
summary(model_stepwise)