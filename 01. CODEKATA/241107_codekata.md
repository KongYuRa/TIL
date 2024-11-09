#### 1. 영어 알파벳으로 이루어진 문자열 `str`이 주어집니다. 각 알파벳을 대문자는 소문자로 소문자는 대문자로 변환해서 출력하는 코드를 작성해 보세요.

```
제한사항
1 ≤ str의 길이 ≤ 20
str은 알파벳으로 이루어진 문자열입니다.


입출력 예

입력 #1
aBcDeFg

출력 #1
AbCdEfG
```

```
str = input()
```

입력된 문자의 대소문자를 바꾸기 위해서는 `.swapcase()` 를 사용해야 한다.

- `.upper()` : 문자열 모두 대문자로

-  `.lower()` : 문자열 모두 소문자로

-  `.swapcase()` : 문자열의 대문자는 소문자로, 소문자는 대문자로

-  `.capitalize()` : 첫 글자를 대문자로

-  `.title()` : 단어의 첫 글자를 대문자로

```
str = input()

print(str.swapcase())
```

_추가 학습
```
# 방법 1

str = input()

for c in str:
    if c.isupper() == True:
        print(i.lower(), end="")
    else:
        print(i.upper(), end="")

# 방법 2
print(input().swapcase())

# 방법 3
str = input()
str2 = ''

for i in str:
    if i.isupper() == True:
        str2 += i.lower()
    elif i.islower() == True:
        str2 += i.upper()

print(str2)
```

#### 2. 다음과 같이 출력하도록 코드를 작성해 주세요.

```
출력 예시
!@#$%^&*(\'"<>?:;
```

```
print('hello world!')
```

hello world! 문자를 대신하여 `"!@#$%^&*(\'"<>?:;"` 를 넣어 출력환다.

```
print("!@#$%^&*(\\'\"<>?:;")
```

_추가 학습
```
# 방법 1
print('!@#$%^&*(\\\'\"<>?:;')

# 방법 2
print(r'!@#$%^&*(\'"<>?:;')
```

#### 3. 두 정수 `a`, `b`가 주어질 때 다음과 같은 형태의 계산식을 출력하는 코드를 작성해 보세요.

```
제한사항
1 ≤ a, b ≤ 100


입출력 예

입력 #1
4 5

출력 #1
4 + 5 = 9
```

```
a, b = map(int, input().strip().split(' '))
print(a + b)
```

`a`와 `b` 값이 각각 있고, 원하는 결과값은 `a + b`로 출력 가능하지만, 중간에 필요한 기호는 `'+'`, `'='`로 각각 작성한다.

```
a, b = map(int, input().strip().split(' '))
print(a, "+", b, "=", a+b)
```

_추가 학습
```
# 방법 1
a, b = map(int, input().strip().split(' '))
print(f"{a} + {b} = {a + b}")


# 방법 2
a, b = map(int, input().strip().split(' '))
c = a + b
print('{} + {} = {}'.format(a, b, c))
```