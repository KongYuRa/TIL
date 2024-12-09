#### 1. 문자열 `str`이 주어질 때, `str`을 출력하는 코드를 작성해 보세요.

```
제한사항
1 ≤ `str`의 길이 ≤ 1,000,000
`str`에는 공백이 없으며, 첫째 줄에 한 줄로만 주어집니다.


입출력 예

입력 #1
HelloWorld!

출력 #1
HelloWorld!
```

```
str = input()
```

답
```
str = input()

print(str)
```

_추가 학습
```
import sys

str = sys.stdin.readline().strip()
```

#### 2. 정수 `a`와 `b`가 주어집니다. 각 수를 입력받아 입출력 예와 같은 형식으로 출력하는 코드를 작성해 보세요.

```
제한사항
-100,000 ≤ a, b ≤ 100,000


입출력 예

입력 #1
4 5

출력 #1
a = 4
b = 5
```

```
a, b = map(int, input().strip().split(' '))
print(a + b)
```
답
```
a, b = map(int, input().strip().split(' '))

print('a =', a)
print('b =', b)
```

_추가 학습

```
# f-string 방법
a, b = map(int, input().strip().split(' '))
print(f'a = {a}')
print(f'b = {b}')

---
# format 방법 - 1
a, b = map(int, input().strip().split(' '))
print('a = {0}'.format(a))
print('b = {0}'.format(b))

# format 방법 - 2
a, b = map(int, input().strip().split(' '))
print('a = {num_a}'.format(num_a=a))
print('b = {num_b}'.format(num_b=b))
```
#### 3. 문자열 `str`과 정수 `n`이 주어집니다. `str`이 `n`번 반복된 문자열을 만들어 출력하는 코드를 작성해 보세요.

```
제한사항
1 ≤ str의 길이 ≤ 10
1 ≤ n ≤ 5


입출력 예

입력 #1
string 5

출력 #1
stringstringstringstringstring
```

```
str, n = input().strip().split(' ')
n = int(n)
```

답
```
str, n = input().strip().split(' ')
n = int(n)

answer = str*n

print(answer)
```

_추가 학습
```
# input 사용
str, n = input().split(' ')
n = int(n)
print(str*n)

---
# sys.stdin.raedline 사용
import sys

str, n = sys.stdin.readline().strip().split(' ')
n = int(n)
print(str*n)
```