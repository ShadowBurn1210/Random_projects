setwd("c:/Users/Admin/PycharmProjects/RandomProjects/Random_projects/reaserchMethods/Assignment1")

# Read the file using the tab delimiter
furn.data <- read.table("Furniture.txt", header = TRUE, sep = "\t")

# Create a data frame
data <- data.frame(furn.data)

# (a) Find the sample linear regression line
# Fixed regression model - now Customers is predicted by Ads
reg.data <- lm(data$Customers ~ data$Ads)
# summary(reg.data)

# # Create a scatter plot with regression line
# plot(data$Ads, data$Customers, main = "Scatter plot of Ads and Customers", 
#      xlab = "Ads", ylab = "Customers")
# abline(reg.data, col = "red")

# # (c) Determine the coefficient of determination (R-squared)
# r_squared <- summary(reg.data)$r.squared
# cat("R-squared:", r_squared, "\n")

# # (b) Interpret the coefficients
# coefficients <- coef(reg.data)
# cat("Intercept:", coefficients[1], "- Expected customers when no ads are placed\n")
# cat("Slope:", coefficients[2], "- Expected increase in customers for each additional ad\n")

# # (d) Determine whether there is evidence to infer a linear relationship
# f_stat <- summary(reg.data)$fstatistic
# p_value <- pf(f_stat[1], f_stat[2], f_stat[3], lower.tail = FALSE)
# cat("F-statistic:", f_stat[1], "with p-value:", p_value, "\n")
# cat("Is there evidence of a linear relationship?", ifelse(p_value < 0.05, "Yes", "No"), "\n")

# # (e) Determine the residuals and standardized residuals
# residuals <- residuals(reg.data)
# standardized_residuals <- rstandard(reg.data)
# plot(data$Ads, residuals, main = "Residuals vs Ads", xlab = "Ads", ylab = "Residuals", pch = 16)
# # Create a data frame with both types of residuals
# residual_data <- data.frame(
#   # Observation = 1:length(residuals),
#   # Ads = data$Ads,
#   # Customers = data$Customers,
#   # Fitted = fitted(reg.data),
#   Residuals = residuals,
#   Standardized_Residuals = standardized_residuals
# )
# head(residual_data)

# # (f) Histogram of residuals and normality test
# par(mfrow = c(1, 2))
# hist(residuals, main = "Histogram of Residuals", 
#      xlab = "Residuals", col = "skyblue", border = "black")

# # QQ plot for visual assessment of normality
# qqnorm(residuals)
# qqline(residuals)
# par(mfrow = c(1, 1))

# # Shapiro-Wilk test for normality
# shapiro_test <- shapiro.test(residuals)
# print(shapiro_test)
# cat("Do residuals appear normally distributed?", 
#     ifelse(shapiro_test$p.value > 0.05, "Yes", "No"), "\n")

# # (g) Construct a 95% prediction interval and plot with scatterplot and regression line
# new_data <- data.frame(Customers = seq(min(data$Customers), max(data$Customers), by = 10))

# predictions <- predict(reg.data, newdata = new_data, interval = "predict", level = 0.95)

# # Plot with prediction intervals
# plot(data$Ads, data$Customers, main = "Regression with 95% Prediction Interval",
#      xlab = "Number of Ads", ylab = "Number of Customers", pch = 16)
# abline(reg.data, col = "red")

# # Add prediction interval lines
# lines(new_data, predictions[, 2], col = "blue", lty = 2)
# lines(new_data, predictions[, 3], col = "blue", lty = 2)

# # (i) Check for heteroscedasticity
# # Breusch-Pagan test
# library(lmtest)
# bp_test <- bptest(reg.data)
# print(bp_test)
# cat("Is heteroscedasticity a problem?", 
#     ifelse(bp_test$p.value < 0.05, "Yes", "No"), "\n")

# # Visual check: Plot residuals vs fitted values
# plot(fitted(reg.data), residuals, 
#      main = "Residuals vs Fitted Values",
#      xlab = "Fitted Values", ylab = "Residuals", pch = 16)
# abline(h = 0, lty = 2, col = "red")

# # (j) Comprehensive summary of findings
# cat("\n---- SUMMARY OF FINDINGS ----\n")
# cat("1. The regression equation is: Customers =", round(coefficients[1], 2), "+", 
#     round(coefficients[2], 2), "× Ads\n")
# cat("2. R-squared value is", round(r_squared, 4), "meaning that approximately", 
#     round(r_squared * 100, 2), "% of the variation in customer numbers is explained by the number of ads\n")
# cat("3. F-test p-value is", p_value, "indicating that the relationship is", 
#     ifelse(p_value < 0.05, "statistically significant", "not statistically significant"), "\n")
# cat("4. Normality test p-value is", shapiro_test$p.value, "suggesting residuals are", 
#     ifelse(shapiro_test$p.value > 0.05, "normally distributed", "not normally distributed"), "\n")
# cat("5. Heteroscedasticity test p-value is", bp_test$p.value, "suggesting heteroscedasticity is", 
#     ifelse(bp_test$p.value < 0.05, "a concern", "not a significant concern"), "\n")