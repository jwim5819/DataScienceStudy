# 그래픽 디스플레이 창 생성
windows(width = 7, height = 5)

# 두 집단의 차이 검정
# t 검정
str(sleep)
sleep

library(tidyr)
wide_df <- spread(sleep, key = group, value = extra)
summary(wide_df)

tapply(sleep$extra, INDEX = list(sleep$group), FUN = mean)

t.test(extra ~ group, sleep, paired = T) # long format
t.test(wide_df$'1', wide_df$'2', paired = T) # wide format

# 카이제곱분포와 카이제곱검정
# 독립변수와 종속변수가 둘 다 범주형일때 사용한다.

# F분포와 분산분석
v <- rf(n = 10000, df1 = 1, df2 = 30) # df1 그룹의 갯수, df2 그룹의 갯수의 합
hist(v, col = 'steelblue')

x <- seq(0, 15, length = 200)

curve(df(x, df1 = 1, df2 = 30), 0, 15, col = 'tomato', lwd = 2, lty = 1)
curve(df(x, df1 = 5, df2 = 50), 0, 15, col = 'steelblue', lwd = 2, lty = 1, add = T)
curve(df(x, df1 = 10, df2 = 80), 0, 15, col = 'green', lwd = 2, lty = 2, add = T)

qf(p = 0.95, df1 = 1, df2 = 30)
pf(q = 4.170877, df1 = 1, df2 = 30)
pf(q = 4.170877, df1 = 1, df2 = 30, lower.tail = F) # 유의수준

# 일원 분산분석
df <- InsectSprays
str(df)
table(df$spray)

round(tapply(df$count, INDEX = list(df$spray), FUN = mean),2)

boxplot(count ~ spray, df, col = 2:7)

library(gplots)
plotmeans(count ~ spray, df, col = 'tomato', barcol = 'orange', lwd = 3, barwidth = 3)

aov_result <- aov(count ~ spray, df)
model.tables(aov_result, type = 'mean')

plot(TukeyHSD(aov_result), col = 'blue', las = 1)


library(car)
qqplot(df$count, pchisq = 19, col = 'orange')
shapiro.test(df$count)

leveneTest(count ~ spray, df)
bartlett.test(count ~ spray, df)

oneway.test(count ~ spray, df)



df <- ToothGrowth
str(df)
unique(df$dose)

df$dose <- factor(df$dose, levels = c(0.5, 1.0, 2.0), labels = c('L', 'M', 'H'))
str(df)

with(df, tapply(len, INDEX = list(SUPP=supp, DOSE=dose), FUN = mean))

boxplot(len ~ supp * dose, df, col = c('orange', 'steelblue'))

aov_result <- aov(len ~ supp * dose, df)
summary(aov_result)

# 상관관계와 상관분석
cor(cats$Bwt, cats$Hwt)
plot(cats$Bwt, cats$Hwt, pch = 19, col = 'tomato')

cor(cats$Bwt, cats$Hwt, method = 'pearson')
cor(cats$Bwt, cats$Hwt, method = 'spearman')
cor(cats$Bwt, cats$Hwt, method = 'kendall')

# 선형회귀분석
library(HistData)
df <- GaltonFamilies
str(df)

cor(df$midparentHeight, df$childHeight)

plot(jitter(childHeight) ~ jitter(midparentHeight), df, 
        col = adjustcolor('steelblue', alpha = 0.5), pch = 19)

model <- lm(childHeight ~ midparentHeight, df)
abline(model, col = 'tomato', lwd = 3)

x <- runif(n = 100, min = 0, max = 100)
y <- 3 * x + 5 + rnorm(100, mean = 0, sd = 20)
plot(x, y, pch = 19, col = 'orange')

model <- lm(y ~ x)
abline(model, col = 'tomato', lwd = 3, lty = 2)

summary(model)

abline(a = 1, b = 5, col = 'red', lwd = 1, lty = 2)
