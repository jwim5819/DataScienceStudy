# R을 이용한 통계분석

# 그래픽 디스플레이 창 생성
windows(width = 7, height = 5)

# 베르누이 시행 -> n 관측값의 갯수, size 시행횟수, prob 각각의 성공확률
v <- rbinom(n = 100, size = 10, prob = 0.5)
hist(v, col='orange', breaks = 20)
# n 관측값의 갯수가 늘어날수록 수학적 확률과 가까워 진다.
v <- rbinom(n = 1000000, size = 1000, prob = 0.5)
hist(v, col='orange', breaks = 50)

# 균일분포를 따르는 랜던값 생성(random uniform)
v_2 <- runif(n = 100000, min = 0, max = 100)
hist(v_2, col='sky blue', breaks = 50)
mean(v_2)
sd(v_2)

v_3 <- rnorm(n = 1000000, mean = 50, sd = 20)
hist(v_3, col='steel blue', breaks = 50)

# 정규분포 곡선
x <- seq(-3, 3, length = 100000)
y <- dnorm(x)
plot(x, y, col = 'tomato', lwd = 3, type = 'l')

x <- seq(0, 100, length = 100000)
y <- dnorm(x, mean = 50, sd = 20)
plot(x, y, col = 'tomato', lwd = 3, type = 'l')

# 확률분포 곡선
x <- seq(0, 100, length = 100000)
y <- dunif(x, min = 0, max = 100)
plot(x, y, col = 'tomato', lwd = 3, type = 'l')

# 키 정규분포 곡선
x <- seq(140, 200, length = 100000)
y <- dnorm(x, mean = 170, sd = 10)
plot(x, y, col = 'tomato', lwd = 3, type = 'l')

# 적분을 이용해 확률 구하기
pnorm(35000, mean = 30000, sd = 10000)
pnorm(25000, 30000, 10000)

pnorm(35000, 30000, 10000) - pnorm(25000, 30000, 10000)

pnorm(1, 0, 1) - pnorm(-1, 0, 1)

pnorm(2) - pnorm(-2)
pnorm(2.56) - pnorm(-2.56)

# pnorm과 점수를 이용해 예상 등수 구하기
(1 - pnorm(87, mean = 68, sd = 10)) * 50
pnorm(87, mean = 68, sd = 10, lower.tail = F) * 200

# 소득이 25000$보다 작을 확률은?
pnorm(25000, 30000, 10000)
# 35000$보다 클 확률은?
pnorm(35000, 30000, 10000, lower.tail = F)

# 표준화 및 비교
pnorm(70, 60, 10, lower.tail = F)
pnorm(80, 70, 20, lower.tail = F)

# 이항분포
x <- rbinom(10000, size = 100, prob = 0.5)
hist(x, col = 'sky blue', breaks = 50, prob = T)
sd(x)
curve(dnorm(x, 50, 5), 30, 70, col = 'tomato', add = T, lwd = 3, lty = 2)



# 샘플링
library(MASS)
height <- na.omit(survey$Height)
length(height)
hist(height, col = 'sky blue', breaks = 20)

x_bar <- c()
for (i in 1:100000){
  sample <- height[sample(1:209, size = 30)]
  x_bar[i] <- mean(sample)
  x_sd[i] <- sd(sample)
}
x <- seq(160, 180, length = 200)
hist(x_bar, col = 'steel blue', breaks = 50, probability = T)
curve(dnorm(x, mean(height), sd(x_bar)), 160, 180, col = 'tomato', add = T, lwd = 3, lty = 2)

x_1 <- rnorm(n = 5000, mean = 80, sd = 5)
x_2 <- rnorm(n = 5000, mean = 50, sd = 5)
x <- c(x_1, x_2)
hist(x, col = 'steelblue', breaks = 50)

x_bar <- c()
for (i in 1:100000){
  sample <- x[sample(x, size = 30)]
  x_bar[i] <- mean(sample)
}
hist(x_bar, col = 'steel blue', breaks = 50, probability = T)
x_sample <- seq(78, 84, length = 200)
curve(dnorm(x_sample, mean(x), sd(x_bar)), 78, 84, col = 'tomato', add = T, lwd = 3, lty = 2)

# 귀무/대립가설 실습
cor(iris[, -5])
# 상관계수 검정, t값, df(자유도), p밸류 확인
cor.test(iris$Petal.Width, iris$Petal.Length)

# 100번의 동전을 던져서 앞면이 60번 나왔다면 공평한 동전인가? 가설검정
# h0 -> p=0.5이다.
# h1 -> p!=0.5이다.
binom.test(x = 6000, n = 10000, p = 0.5)

binom.test(x = 65, n = 100, p = 0.5)

binom.test(x = 60, n = 100, p = 0.5, conf.level = 0.99)

binom.test(x = 35, n = 100, p = 0.5, conf.level = 0.99)

# 정규성 검정
shapiro.test(survey$Height)
hist(survey$Height)
shapiro.test(survey$Age)
hist(survey$Age)

qqnorm(survey$Height, col = 'skyblue')
qqline(survey$Height, col = 'tomato', lwd = 3)

qqnorm(survey$Age, col = 'steelblue')
qqline(survey$Age, col = 'tomato', lwd = 3)

# t분포
# t분포로 랜덤넘버 생성
v <- rt(n = 10000, df = 29)
hist(v, col = 'steelblue', breaks = 100, probability = T)
x <- seq(-4, 4, length = 200)
curve(dt(x, df = 3), -4, 4, col = 'tomato', lwd = 4, lty = 2, add = T)
curve(dnorm(x), -4, 4, col = 'magenta', lwd = 4, lty = 2, add = T)

pt(q = 2.04523, df = 29)
qt(p = 0.975, df = 29)
pt(q = 2.756386, df = 29)
qt(p = 0.995, df = 29)

# t분포와 평균검정
# 귀무가설 : 고양이의 몸무게는 2.6kg이다.
data(cats)
str(cats)

table(cats$Sex)

mean(cats$Bwt)
tapply(cats$Bwt, INDEX = list(Swx = cats$Sex), mean)

t.test(Bwt ~ Sex, cats, conf.level = 0.99)
# p밸류가 8.831e-15이기 때문에 귀무가설 기각
# 고양이의 몸무게는 성별에 따라 다르다는 대립가설 채택


str(sleep)

t.test(extra ~ group, sleep, paired = T)

