x <- 10
x
20 -> y
y
z <- x + y
z

# 변수는 문자나 마침표로 시작해야 한다.
# 다른건 파이썬이랑 비슷
val.1 <- 200
val.1

# 자료형도 파이썬이랑 비슷
# 논리형(logical)
# 숫자형(numerlic)
# 문자형(character)
# 특수형 -> NA, NaN, NULL, Inf, -Inf 등
class(TRUE)
class('hello')

# 연산자(operators)
# 산술연산자, 논리연산자 등 파이썬과 비슷
x <- 2
y <- 2 * ((x+2)-(x-4)) / 2+3
y
3 < 4
3 > 4

# 조건문(conditional statement)
if (condition)
{condition.true.statements}

# 학생 점수에 따라 학점 부여하기
# 주의 else는 반드시 }가 있는 줄에 있어야함
score <- 91
if (score>=90){
  grade <- 'A'
} else if (score >= 80) {
  grade <- 'B'
} else {
  grade <- 'C'
}
grade

# 반복문(loop statement)
while (condition ){
  condition.true.statement
}
for (variable in start:end){
  loop.statements
}

# 반복문을 이용하여 1에서 10까지의 합 구하기
s <- 0
i <- 1
while(i <= 10) {
  s <- s + i
  i <- i + 1
}
s

s <- 0
for (i in 1:10){
  s <- s+i
}
s

# 임의의 자연수 n에 대하여 n의 약수 출력
# 및 약수의 갯수 구하기
n <- 32
count <- 0
for (i in 1:n){
  if (n %% i == 0){
    cat(i, "")
    count <- count + 1
  }
}
count

# break와 next
# break -> 반복문에서 빠져나감
# next -> 반복 코드 블록에서 다음 반복으로 되돌아감
for (i in 1:10){
  cat(i)
  if (i < 5){
    next
  } else {
    break
  }
}

# 임의의 자연수 n이 소수인지 아닌지 판별
n <- 17
count <- 0
is.prime <- TRUE
for (i in 1:n){
  if (n%%i == 0){
    count <- count + 1
  } else {
    next
  }
}
if (count != 2){
  is.prime <- FALSE
}
is.prime
