#### 1. 두 개의 문자열 `str1`, `str2`가 공백으로 구분되어 입력으로 주어집니다. 입출력 예와 같이 `str1`과 `str2`을 이어서 출력하는 코드를 작성해 보세요.

```
제한사항
1 ≤ str1, str2의 길이 ≤ 10


입출력 예

입력 #1
apple pen

출력 #1
applepen

입력 #2
Hello World!

출력 #2
HelloWorld!
```

```
str1, str2 = input().strip().split(' ')
```

두 문자의 입력값을 추가해야하기 때문에 `print()`에 두 문자를 더하는 값 `str1+str2`를 입력한다.

```
str1, str2 = input().strip().split(' ')

print(str1+str2)
```

_추가 학습
```
# 방법1
str1, str2 = input().strip().split(' ')
print(str1+str2)

# 방법2
str1, str2 = input().strip().split(' ')
s = ""
s += str1
s += str2
print(s)

# 방법3
str1, str2 = input().strip().split(' ')
print(''.join([str1, str2]))
```

+join 함수
- '구분자'.join(리스트)'구분자'.join(리스트)를 이용하면 리스트의 값과 값 사이에 '구분자'에 들어온 구분자를 넣어서 하나의 문자열로 합쳐줍니다.'_'.join(['a', 'b', 'c']) 라 하면 "a_b_c" 와 같은 형태로 문자열을 만들어서 반환해 줍니다.

```
# join 함수 예제

#원본 리스트
a = ['a', 'b', 'c', 'd']
print(a) # ['a', 'b', 'c', 'd']

#리스트를 문자열로 합치기
result1 = "_".join(a)
print(result1) # 'a_b_c_d'

#리스트를 문자열로 합치기
result2 = ".".join(a)
print(result2) # 'a.b.c.d'

result3 = "".join(a)
print(result3) # 'abcd'
```

#### 2. 문자열 str이 주어집니다. 문자열을 시계방향으로 90도 돌려서 아래 입출력 예와 같이 출력하는 코드를 작성해 보세요.

```
제한사항
1 ≤ str의 길이 ≤ 10


입출력 예

입력 #1
abcde

출력 #1
a
b
c
d
e
```

```
str = input()
```

문자를 각 리스트로 입력받아서 출력하면 된다.

```
str = input()

for i in str:
    print(i)
```

_추가 학습
```
# 방법 1
str = input()
for i in str:
    print(i)

# 방법2
print('\n'.join(input()))
```

#### 3. 자연수 n이 입력으로 주어졌을 때 만약 `n`이 짝수이면 "`n` is even"을, 홀수이면 "`n` is odd"를 출력하는 코드를 작성해 보세요.

```
제한사항
1 ≤ n ≤ 1,000



입출력 예

입력 #1
100

출력 #1
100 is even

입력 #2
1

출력 #2
1 is odd

```

```
a = int(input())
```

정수를 받았을 때 2로 나눈 나머지를 통해 홀수, 짝수를 판별할 수 있다.
```
a = int(input())

if a % 2 == 0:
    print(f'{a} is even')
else:
    print(f'{a} is odd')
```

_추가 학습
```
나머지 연산자 활용 예시

# 끝의 두자리 수만 원할때
num = 29384792835
print(num%100)

# 요일
days_in_week = 7
current_day = 3  # 현재 요일 (예: 수요일이 3이라고 가정)
days_later = 10  # 10일 후

new_day = (current_day + days_later) % days_in_week
print(f"{days_later}일 후 요일은 {new_day}입니다.")

# 각도 회전
rotation = 370
normalized_rotation = rotation % 360
print(f"정규화된 각도: {normalized_rotation}도")  # 결과는 10도
```