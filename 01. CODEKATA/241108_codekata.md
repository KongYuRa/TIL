#### 1. 두 개의 문자열 `str1`, `str2`가 공백으로 구분되어 입력으로 주어집니다. 입출력 예와 같이 `str1`과 `str2`을 이어서 출력하는 코드를 작성해 보세요.

```
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

#### 2. 문자열 str이 주어집니다. 문자열을 시계방향으로 90도 돌려서 아래 입출력 예와 같이 출력하는 코드를 작성해 보세요.

```
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

#### 3. 자연수 n이 입력으로 주어졌을 때 만약 `n`이 짝수이면 "`n` is even"을, 홀수이면 "`n` is odd"를 출력하는 코드를 작성해 보세요.

```
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

