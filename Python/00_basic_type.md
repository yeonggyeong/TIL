# 00_Python Basic

## 변수
- 변수는 컴퓨터 메모리 어딘가에 저장되어 있는 객체를 참조하기 위해 사용되는 이름
- 문자, 정수, 실수 등 여러 가지의 type이 존재

### 변수 선언 및 type 확인
- 변수는 `=`으로 할당
- 변수의 타입을 확인하기 위해서는 `type()`를 사용

```python
# 1) 변수 선언
x = 'GITHUB'
# 2) 변수 타입 확인
type(x)
# 3-1) 동시 같은 값 할당
x = y = 100 # x = 100, y = 100 으로 값 할당
# 3-2) 동시 여러 값 할당
x, y = 1, 2 # x = 1, y = 2 으로 값 할당
```

2)의 결과는 x에 저장된 값에 따라 확인 가능

### 변수명 규칙
- 첫 글자에 숫자가 올 수 없음( 영문, _ 가능 )
- 길이에 제한이 없음
- **아래와 같은 파이썬 예약어를 사용할 수 없음**
```python
False, None, True, and, as, assert, async, await, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield
```
- 내장함수나 모듈 등의 이름으로도 만들면 기존 내장함수나 모듈이 동작하지 않음


## Data Type

 **Data Type은 크게 Boolean, Numeric, String, None 으로 구분**

### 1. Boolean Type
True / False 로 구성

비교 연산 혹은 논리 연산에서 활용

0 -> False, 1 -> True 로 인식

빈 자료형, 빈 문자열, None은 모두 False로 인식

### 2. Numeric Type
Numeric Type은 다시 int, float, complex로 구분

#### 1) int
모든 정수는 `int`로 표현
정수를 8진수(`0b`), 2진수(`0o`), 16진수(`0x`)로 변경 가능
```python
x = 3 # Numeric Type 변수 선언
binary_x = 0b3 # 3의 2진수
decimal_x = 0o3 # 3의 10진수
hexade_x = 0x3 # 3의 16진수
```

#### 2) float
실수는 `float`로 표현
```python
x = 3.4 # Float Type 변수 선언
```

#### 3) complex
complex type이란 복소수 타입을 의미

실수와 허수로 구성

허수를 j로 표현

```python
x = 3 + 4j # complex Type 변수 선언 
```

### 3. String Type

모든 문자열은 str로 표현

문자열을 표현하기 위해서는 `''` 또는 `""`로 감싸서 표현
```python
x = "안녕" 
y = 'python'
z = "안녕 '파이썬'"
```

긴 문자열을 표현하기 위해서는 `'''` 삼중 따옴표를 사용
```python
print("""
안녕
파이썬
""")
```

## Escape Sequence
문자열을 활용할 때 특별한 조작을 하기 위해 사용

`\`를 사용하여 구분

| 문자 |                 의미                  |
| ---- | :-----------------------------------: |
| `\n` |                줄 바꿈                |
| `\t` |                  탭                   |
| `\r` | 캐리지리턴 ( 커서를 행의 앞으로 이동) |
| `\0` |                 Null                  |
| `\\` |                   \                   |
| `\'` |            ' ( 인용 부호 )            |
| `\"` |            " ( 인용 부호 )            |

## Formatting

문자열을 만들 때 원하는 위치에 특정값을 삽입하여 출력

Formatting에도 여러가지 방법이 존재

### 1. %-formatting

% 기호 뒤에 자료형을 가르키는 문자

| 문자 |                 자료형                  |
| ---- | :-----------------------------------: |
| `%s` |                문자열                |
| `%d` |                 정수                 |
| `%f` |                 실수                 |
| `%o` |                 8진수                  |
| `%x` |                  16진수                  |
| `%%` |            % ( 문자 )            |

```python
print('my name is %s'% '파이썬') #my name is 파이썬 출력 -> 문자열 formatting
print('%d = 4 + 1'% 5) # 5 = 4 + 1 출력 -> 정수 formatting
```
### 2. str-formatting

formatting 할 위치에 `{}`을 지정하고 format 함수의 인자들을 삽입하여 출력

```python
# 1. 직접 대입
print('{}! 내 이름은 {}이야'.format('안녕','파이썬')) 
# 2. 변수 대입
string = '안녕'
name = '파이썬'
print('{}! 내 이름은 {}이야'.format(string,name))
```

### f-strings formatting

가장 최근에 나온 formatting 방법

문자열 앞에 f를 추가하고 중괄호 안에 출력하고 싶은 변수명 삽입
```python
print(f'안녕! 내 이름은 {name}이야.')
# 출력 형식 지정 가능
import datetime
to = datetime.datetime.now()
print(f'오늘은 {to:%m}월 {to:%d}일이다.')
```

## None Type
값이 없음을 표현하기 위해 `None` 타입이 존재


