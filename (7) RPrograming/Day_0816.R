# 그래픽 디스플레이 창 생성
windows(width = 7, height = 5)

library(palmerpenguins)
pg <- penguins
str(pg)
pg <- pg[complete.cases(pg), -8]

pg$is.adelie <- factor(ifelse(pg$species == 'Adelie', 'yes', 'no'))

barplot(table(pg$is.adelie))

pg <- pg[, -1]
str(pg)

model <- glm(is.adelie ~ ., pg, family = binomial(link = 'logit'))

summary(model)

model$fitted

pg$pred <- factor(ifelse(model$fitted.values > 0.5, 'yes', 'no'))
table(pg$is.adelie, pg$pred)



library(faraway)
