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

### 2. While문 ( 반복문 )

원하는 코드를 반복하기 위해서는 반복문을 사용

`while`문은 조건식이 참인 경우 코드를 반복적으로 실행

```python
while <조건식>:
    <조건식> 이 참일때마다 실행할 문장
```

`while`문도 `if`문과 마찬가지로 **들여쓰기**와 **`:`**이 꼭 必
- 파이썬에서는 들여쓰기를 위해 `tab`을 사용하거나 `spacebar`를 사용
- 한칸의 들여쓰기는 `tab` 1번 혹은 `spacebar` 4번으로 통일
- `:`이 없다면, 에러 발생

```python
i = 0
while i < 5 :
    i += 1
    print(i)
```
i값이 5 미만일때 아래의 코드를 실행

i값을 조건식으로 설정했기 때문에 초깃값 설정이 필요하며, 반복문안에서 i값을 수정해야 함

i값을 수정하지 않는다면, while문은 무한 루프를 돌 가능성이 있음

위의 코드는 i가 0부터 4까지 차례대로 출력

### 3. For문 ( 반복문 )

원하는 코드를 반복하기 위해서는 반복문을 사용

`for`문은 반복가능한 객체들의 요소를 반복

```python
for <임시변수> in <iterable data>:
    반복할 코드
```

`for`문도 다른 제어문과 마찬가지로 **들여쓰기**와 **`:`**이 꼭 必
- 파이썬에서는 들여쓰기를 위해 `tab`을 사용하거나 `spacebar`를 사용
- 한칸의 들여쓰기는 `tab` 1번 혹은 `spacebar` 4번으로 통일
- `:`이 없다면, 에러 발생

```python
# 1. string 반복
for string in 'python':
    print(string)
# p
# y
# t
# h
# o
# n
```
문자열을 반복할시, 문자 하나하씩 출력

```python
# 2. list, tuple 반복
for element in ['apple','banana']:
    print(element)
# apple
# banana
```

#### enumerate()

반복문에서 `enumerate()`를  사용하면, 인덱스와 값을 함께 활용이 가능
```python
for idx, fruit in enumerate(['apple', 'banana', 'mango']):
    print(idx, fruit)
# 0, apple
# 1, banana
# 2, mango
```

인덱스가 0부터 1씩 증가하며 출력

#### List comprehension

List comprehension은 표현식과 제어문을 통해 리스트를 생성

여러 줄의 코드를 한 줄로 줄이기 가능

```python
[ expression for 변수 in iterable data ]
```

```python
# list comprehension
[ num ** 3 for num in range(10)]
# for
nums = []
for num in range(10):
    nums.append(num**3)
```

위의 list comprehension코드와 for문 코드의 결과값은 동일

### 4. 반복 제어문 ( break, continue, pass )

#### 1) break

반복문을 중간에 종료하기 위해서는  `break`를 사용

`for`문, `while`문에서 빠져 나오기 위해 사용

```python
n = 0
while n < 3 :
    print(n)
    if n == 1 :
        break
    n += 1
```

위의 코드가 실행이 된다면 `break`에 의해서 n의 값이 1이 되면 `while`문이 종료

#### 2) continue

일부 조건을 만족할때, 실행을 건너 뛰기 위해 사용

```python
for i in range(6) :
    if i % 2 == 0 :
        continue
    print(f'{i}는 홀수다.')
```

i가 짝수이면 아래의 `print`문은 실행되지 않고 다음 반복으로 넘어감

#### 3) pass

아무것도 하지 않는다는 의미

들여쓰기 이후 문장이 필요하지만, 할 일이 없을때 자리를 채우는 용도로 사용

