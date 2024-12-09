#### 1. 문자열 `my_string`과 정수 `k`가 주어질 때, `my_string`을 `k`번 반복한 문자열을 return 하는 solution 함수를 작성해 주세요.




```
제한사항

1 ≤ my_string의 길이 ≤ 100
my_string은 영소문자로만 이루어져 있습니다.
1 ≤ k ≤ 100

입출력 예
my_string	k	result
"string"	3	"stringstringstring"
"love"	10	"lovelovelovelovelovelovelovelovelovelove"

입출력 예 설명

입출력 예 #1
예제 1번의 my_string은 "string"이고 이를 3번 반복한 문자열은 "stringstringstring"이므로 이를 return 합니다.

입출력 예 #2
예제 2번의 my_string은 "love"이고 이를 10번 반복한 문자열은 "lovelovelovelovelovelovelovelovelovelove"이므로 이를 return 합니다.
```

```
def solution(my_string, k):
    answer = ''
    return answer
```

답
```
def solution(my_string, k):
    return my_string * k
```

#### 2. 연산 ⊕는 두 정수에 대한 연산으로 두 정수를 붙여서 쓴 값을 반환합니다. 예를 들면 다음과 같습니다.

12 ⊕ 3 = 123
3 ⊕ 12 = 312

양의 정수 `a`와 `b`가 주어졌을 때, `a` ⊕ `b`와 `b` ⊕ `a` 중 더 큰 값을 return 하는 solution 함수를 완성해 주세요.

단, `a` ⊕ `b`와 `b` ⊕ `a`가 같다면 `a` ⊕ `b`를 return 합니다.




```
제한사항
1 ≤ a, b < 10,000

입출력 예
a	b	result
9	91	991
89	8	898

입출력 예 설명

입출력 예 #1
a ⊕ b = 991 이고, b ⊕ a = 919 입니다. 둘 중 더 큰 값은 991 이므로 991을 return 합니다.

입출력 예 #2
a ⊕ b = 898 이고, b ⊕ a = 889 입니다. 둘 중 더 큰 값은 898 이므로 898을 return 합니다.
```

```
def solution(a, b):
    answer = 0
    return answer
```

답
```
def solution (a, b) :
    return int(max(f"{a}{b}", f"{b}{a}"))
```

#### 2. 연산 ⊕는 두 정수에 대한 연산으로 두 정수를 붙여서 쓴 값을 반환합니다. 예를 들면 다음과 같습니다.

12 ⊕ 3 = 123
3 ⊕ 12 = 312
양의 정수 `a`와 `b`가 주어졌을 때, `a` ⊕ `b`와 `2 * a * b` 중 더 큰 값을 return하는 solution 함수를 완성해 주세요.

단, `a` ⊕ `b`와 `2 * a * b`가 같으면 `a` ⊕ `b`를 return 합니다.


```
제한사항
1 ≤ a, b < 10,000

입출력 예
a	b	result
2	91	364
91	2	912

입출력 예 설명

입출력 예 #1
a ⊕ b = 291 이고, 2 * a * b = 364 입니다. 둘 중 더 큰 값은 364 이므로 364를 return 합니다.

입출력 예 #2
a ⊕ b = 912 이고, 2 * a * b = 364 입니다. 둘 중 더 큰 값은 912 이므로 912를 return 합니다.
```

```
def solution(a, b):
    answer = 0
    return answer
```

답
```


```

