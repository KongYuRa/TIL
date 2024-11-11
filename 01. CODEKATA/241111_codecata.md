#### 1. 문자열 `my_string`, `overwrite_string`과 정수 `s`가 주어집니다. 문자열 `my_string`의 인덱스 `s`부터 `overwrite_string`의 길이만큼을 문자열 `overwrite_string`으로 바꾼 문자열을 return 하는 solution 함수를 작성해 주세요.


```
제한사항
my_string와 overwrite_string은 숫자와 알파벳으로 이루어져 있습니다.
1 ≤ overwrite_string의 길이 ≤ my_string의 길이 ≤ 1,000
0 ≤ s ≤ my_string의 길이 - overwrite_string의 길이


입출력 예

my_string	  overwrite_string	  s	     result
"He11oWor1d"	       "lloWorl"     	  2	    "HelloWorld"
"Program29b8UYP"	"merS123"	  7	"ProgrammerS123"


입출력 예 설명

입출력 예 #1

예제 1번의 my_string에서 인덱스 2부터 overwrite_string의 길이만큼에 해당하는 부분은 "11oWor1"이고 이를 "lloWorl"로 바꾼 "HelloWorld"를 return 합니다.

입출력 예 #2

예제 2번의 my_string에서 인덱스 7부터 overwrite_string의 길이만큼에 해당하는 부분은 "29b8UYP"이고 이를 "merS123"로 바꾼 "ProgrammerS123"를 return 합니다.
```

```
def solution(my_string, overwrite_string, s):
    answer = ''
    return answer
```

답
```
def solution(my_string, overwrite_string, s):
    answer = my_string[:s] + overwrite_string + my_string[s+len(overwrite_string):]
    return answer
```


#### 2. 길이가 같은 두 문자열 `str1`과 `str2`가 주어집니다. 두 문자열의 각 문자가 앞에서부터 서로 번갈아가면서 한 번씩 등장하는 문자열을 만들어 return 하는 solution 함수를 완성해 주세요.


```
제한사항
1 ≤ str1의 길이 = str2의 길이 ≤ 10
str1과 str2는 알파벳 소문자로 이루어진 문자열입니다.

입출력 예
str1	str2	result
"aaaaa"	"bbbbb"	"ababababab"
```

```
def solution(str1, str2):
    answer = ''
    return answer
```

답
```
def solution(str1, str2):
    answer = ''
    for i in range(0,len(str1)):
        answer = answer + str1[i] + str2[i]
    return answer
```


#### 3. 문자들이 담겨있는 배열 `arr`가 주어집니다. `arr`의 원소들을 순서대로 이어 붙인 문자열을 return 하는 solution함수를 작성해 주세요.


```
제한사항
1 ≤ arr의 길이 ≤ 200
arr의 원소는 전부 알파벳 소문자로 이루어진 길이가 1인 문자열입니다.

입출력 예
arr	      result
["a","b","c"]	"abc"
```

```
def solution(arr):
    answer = ''
    return answer
```

답
```
def solution(arr):
    answer = ''.join(arr)
    return answer
```