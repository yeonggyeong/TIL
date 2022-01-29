# 02 Control Statement

- python에서 제어문이란 말 그대로 **프로그램을 제어**하는 키워드이다.

    1)  조건별로 실행되는 코드를 작성할때 사용하는 `if`문
    2)  반복을 하고싶을 때 사용하는 `for`, `while`문
    3)  반복을 제어하는 `break`, `continue`, `pass` 

---
### 1. IF문 ( 조건문 )

조건문은 `if`를 사용하여 작성

`if`문은 **참/거짓을 판별하는 조건**과 함께 사용

#### 단일 조건문
```python
if <조건식> :
    <조건식>이 참일때 실행할 문장
else:
    <조건식>이 거짓일때 실행할 문장
```
과 같은 문법으로 사용한다.

이때, **들여쓰기 주의 必**
- 파이썬에서는 들여쓰기를 위해 `tab`을 사용하거나 `spacebar`를 사용
- 한칸의 들여쓰기는 `tab` 1번 혹은 `spacebar` 4번으로 통일

또한 `if`절 혹은 `else`절 뒤에 항상 `:` 을 추가
- `:`이 없다면, 에러 발생

(1) 올바른 사용 예시
```python
if x > 5 :
    print('x는 5보다 크다!')
else :
    print('x는 5보다 작다!')
```

(2) 들여쓰기 오류
```python
if x > 5 :
print('x는 5보다 크다!')
else:
     print('x는 5보다 작다!')
```

(2)번처럼 들여쓰기가 잘못 되었는지 항상 확인이 필요!

#### 다중 조건문
`if`문은 단일 조건뿐 아니라 `elif`를 사용해서 다중 조건도 가능

```python
if <조건식 1> :
    <조건식 1>이 참일때 실행할 문장
elif <조건식 2> :
    <조건식 1>이 거짓이고, <조건식 2>가 참일때 실행할 문장
else:
    <조건식 1>과 <조건식 2> 모두 거짓일때 실행할 문장
```
마찬가지로 조건절 뒤에 `:`과 들여쓰기 확인은 항상 필요

```python
if x < 3 :
    print(1)
elif x < 7 :
    print(2)
else:
    print(3)
```
위의 코드에서 `x=2`라면 1이 출력되며, `x=5`라면 2가 출력

#### 중첩 조건문 
조건문은 다른 조건문에 중첩도 가능

```python
if <조건식 1> :
    if <조건식 2> :
        <조건식 1>, <조건식 2> 모두 참일때 실행할 문장
    else:
        <조건식 1>은 참, <조건식 2>는 거짓일때 실행할 문장
else:
    <조건식 1>과 <조건식 2> 모두 거짓일때 실행할 문장
```

#### 조건 표현식

`if`문을 간결하게 표현 가능
삼항 연산자 (Ternary Operator) 라고 부르기도 함

```python
<조건식>이 참일때 값 if <조건식> else <조건식>이 거짓일때 값
```

```python
num = 10
print('num 은 10') if num == 10 else print('num은 10이 아님')
# 위의 코드를 if문으로 작성
if num == 10:
    print('num 은 10')
else :
    print('num은 10이 아님')
```

`num = 10` 이기 때문에 `print('num은 10')`이 출력