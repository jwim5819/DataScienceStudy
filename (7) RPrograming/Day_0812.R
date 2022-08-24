# 그래픽 디스플레이 창 생성
windows(width = 7, height = 5)

library(car)
df <- Prestige

hist(df$income, col = 'tomato', breaks = 20)
shapiro.test(df$income)

hist(df$education, col = 'tomato', breaks = 20)
hist(df$women, col = 'tomato', breaks = 20)
hist(df$prestige, col = 'tomato', breaks = 20)
shapiro.test(df$prestige)

plot(df[, -(5:6)], pch = 19, col = 'tomato')

cor(df[, -(5:6)])

model <- lm(income ~ education, df)
summary(model)

plot(income ~ education, df, col = 'steelblue', pch = 19)
abline(model, col = 'tomato', lwd = 3)

model <- lm(income ~ education + women + prestige, df)
summary(model)

model <- lm(income ~ education + women, df)
summary(model)

model <- lm(income ~ women + prestige, df)
summary(model)



library(stargazer)
stargazer(model, type = 'text')

par(mfrow = c(2,2))
plot(model)
par(mfrow = c(1,1))


# 다항 회귀분석
model <- lm(income ~ education + I(education^2), df)
plot(income ~ education, df, col = 'skyblue')

library(tidyverse)
with(df, lines(arrange(data.frame(education, fitted(model)), education), lty = 1,
               lwd = 3, col = 'tomato'))
summary(model)



df <- mtcars
str(df)
df <- mtcars[, 1:6]
str(df)

plot(df, col = 'green', pch = 19)
cor(df)

library(corrgram)
corrgram(df)

model <- lm(mpg ~ ., df)
summary(model)

model <- lm(mpg ~ hp + wt, df)
summary(model)

model <- lm(mpg ~ drat + hp + wt + disp, df)
model_selected <- step(model, direction = 'backward')
summary(model_selected)



# 연습문제 : 
# HousePrice 데이터 셋에서 다중 선형회귀의 변수 선택을 통해
# 최적의 독립변수 조합을 찾아보자.
# 1. 전진선택법으로 찾은 조합은? R2, Adjusted R2 값은?
# 2. 후진선택법으로 찾은 조합은? R2, Adjusted R2 값은?

df <- read.csv('train.csv')

is.num <- c()
for (i in 1:80){
  is.num[i] <- is.numeric(df[, i])　# 수치형이 아닌 열 제외
}
df <- df[, is.num]  # 수치형 열만 저장
df <- df[, -1]  # ID열 제거
df <- df[complete.cases(df), ]
model <- lm(SalePrice ~ ., df)
lm(SalePrice ~ 1, df)
mod_selected <- step(model, direction = 'backward')
summary(mod_selected)






df <- InsectSprays
model <- lm(count ~ spray, df)
summary(model)

contrasts(df$spray)

df <- mtcars[, 1:6]
str(df)
df$cyl <- factor(df$cyl)
head(df)
table(df$cyl)

lm(mpg ~ ., df)


df <- split(iris, f = iris$Species)
df <- rbind(df$setosa, df$versicolor)

plot(df[, c(1,5)])



# 로지스틱 회귀분석
# 프아송 회귀분석
library(robust)
data(breslow.dat)

df <- breslow.dat
str(df)

df<- df[, c('Base', 'Age', 'Trt', 'sumY')]
str(df)
dim(df)

model <- glm(sumY ~ ., df, family = poisson)
summary(model)

exp(coef(model))



# 이항 로지스틱 회귀분석
df <- split(iris, f = iris$Species)
df <- rbind(df$setosa, df$versicolor)
plot(df[, c(3,5)])


glm(Species ~ Petal.Length, df, family = binomial(link = 'logit'))
