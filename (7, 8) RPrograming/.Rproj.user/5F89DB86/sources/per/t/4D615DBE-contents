library(tidyverse)

# 그래픽 디스플레이 창 생성
windows(width = 7, height = 5)

str(diamonds)
str(mpg)

anscombe
ans <- anscombe
mean(ans$x1)
mean(ans$x2)
mean(ans$x3)
mean(ans$x4)

mean(ans$y1)
mean(ans$y2)
mean(ans$y3)
mean(ans$y4)

cor(ans$x1, ans$y1)
cor(ans$x2, ans$y2)
cor(ans$x3, ans$y3)
cor(ans$x4, ans$y4)

lm(y1 ~ x1, data = ans)
lm(y2 ~ x2, data = ans)
lm(y3 ~ x3, data = ans)
lm(y4 ~ x4, data = ans)

par(mfrow = c(2,2))
plot(ans$x1, ans$y1, col = 'orange', pch = 19)
abline(lm(y1 ~ x1, data = ans), col = 'tomato')
plot(ans$x2, ans$y2, col = 'orange', pch = 19)
abline(lm(y2 ~ x2, data = ans), col = 'tomato')
plot(ans$x3, ans$y3, col = 'orange', pch = 19)
abline(lm(y3 ~ x3, data = ans), col = 'tomato')
plot(ans$x4, ans$y4, col = 'orange', pch = 19)
abline(lm(y4 ~ x4, data = ans), col = 'tomato')
par(mfrow = c(1,1))
# aes 
p <- ggplot(data = mpg,
            mapping = aes(x = displ, y = hwy)) 
# class >> 범주형 변수
# alpha >> 투명도, shape >> 모양
p + geom_point(mapping = aes(color = class,
                             size = class,
                             alpha = 0.3))
# class 별(그룹) nrow 개수 2개 (그래프 행) par
p + geom_point(color = 'tomato') +
  facet_wrap(~class, nrow = 2)

p + geom_point(color="tomato") +
  facet_grid(drv ~ cyl)
# jitter 점이 겹쳐 있으면 흔들어서 볼 수 있게
# smooth >> 추세선
p + geom_point(color = 'tomato') +
  geom_smooth(color = 'cyan')

diamonds

p <- ggplot(data = diamonds,
            mapping = aes(x = cut))

table(diamonds$cut)
# geom_bar x축만 알면 count 자동으로
p + geom_bar()
# 누적 막대 그래프
table(diamonds$clarity)
p + geom_bar(mapping = aes(fill = clarity))
# 비율
p + geom_bar(mapping = aes(fill = clarity),
             position = 'fill')
# 
p + geom_bar(mapping = aes(fill = clarity),
             position = 'dodge')

# 데이터 사우르스 그리기
library(datasauRus)

data(pakage = 'datasauRus')
dd <- datasaurus_dozen

str(dd)
unique(dd$dataset)

plot(y ~ x, data = subset(dd, dataset == 'dino'), pch = 19, col = 'tomato')

ggplot(data = dd, mapping = aes(x = x, y = y)) + geom_point(mapping = aes(color = dataset)) + facet_wrap(~ dataset, nrow = 3)


p <- ggplot(mpg, aes(x = class, y = hwy)) + geom_boxplot(aes(color = class)) + coord_flip()
p

ggplot(diamonds, aes(x = cut, fill = cut)) + geom_bar(show.legend = F, width = 0.5)
ggplot(diamonds, aes(x = cut, fill = cut)) + geom_bar(show.legend = F, width = 1) + coord_polar()



world <- map_data('world')
ggplot(world, aes(long, lat, group = group)) + geom_polygon(fill = 'skyblue', color = 'blue')


str(mpg)

sd(mpg[mpg$hwy > mean(mpg$hwy), c(1, 2, 9:11)]$hwy)
mpg[mpg$hwy > mean(mpg$hwy), c(1, 2, 9:11)]

best_in_class <- mpg %>% group_by(class) %>% filter(row_number(desc(hwy)) == 1)


p <- ggplot(mpg, mapping = aes(x=displ, y=hwy)) 
p + geom_point(mapping = aes(color=class)) + 
  geom_label(mapping = aes(label = model), data = best_in_class, nudge_y = 2, alpha=0.5) +
  theme(legend.position = 'bottom') + 
  guides(color = guide_legend(nrow = 1, override.aes = list(size = 4)))
  

library(palmerpenguins)

pg <- penguins
pg <- pg[complete.cases(pg), ]
pg


pg %>% ggplot(aes(x=body_mass_g, fill=sex)) + 
  geom_histogram(color="#e9ecef", alpha=0.6, position = 'identity') + 
  scale_fill_manual(values=c("#69b3a2", "#404080")) + 
  labs(fill = "") + 
  theme_classic()



library(esquisse)
library(gapminder)

esquisse::esquisser()

library(ggplot2)

ggplot(gapminder::gapminder) +
 aes(x = gdpPercap, y = lifeExp, colour = continent, size = pop) +
 geom_point(shape = "circle") +
 scale_color_hue(direction = 1) +
 labs(x = "수입", y = "기대생명", title = "Gapminder 따라하기", 
 subtitle = "나 좀 짱인듯", caption = "Figure 1. 한스 로슬링 표절") +
 theme_minimal() +
 facet_wrap(vars(year))
