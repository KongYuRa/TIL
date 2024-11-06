##### 1. 문자열 `str`이 주어질 때, `str`을 출력하는 코드를 작성해 보세요.

```
입출력 예

입력 #1
HelloWorld!

출력 #1
HelloWorld!
```

```
str = input()
```

기본 출력 문제이기 때문에 `print()`를 사용하여 주어진 str값을 출력한다.

```
str = input()

print(str)
```

##### 2. 정수 `a`와 `b`가 주어집니다. 각 수를 입력받아 입출력 예와 같은 형식으로 출력하는 코드를 작성해 보세요.

```
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

상기의 코드대로 작성하게 되면 a 값과 b 값을 합한 9라는 결과가 나온다.
문자열은 작은 따옴표(' ')를 사용하여 입력 후 바로 뒤에 입력된 정수를 합하여 각자 출력한다.


```
a, b = map(int, input().strip().split(' '))

print('a =', a)
print('b =', b)
```

##### 3. 문자열 `str`과 정수 `n`이 주어집니다. `str`이 `n`번 반복된 문자열을 만들어 출력하는 코드를 작성해 보세요.

```
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

문자열이 원하는 수 만큼 반복해서 출력되어야 하므로, 문자열 str을 정수 n만큼 곱하여 출력하면 된다.

```
str, n = input().strip().split(' ')
n = int(n)

answer = str*n

print(answer)
```

