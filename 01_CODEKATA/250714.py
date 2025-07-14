# 1. 덧셈식 출력하기

# 문제 설명
# 두 정수 a, b가 주어질 때 다음과 같은 형태의 계산식을 출력하는 코드를 작성해 보세요.

# a + b = c
# 제한사항
# 1 ≤ a, b ≤ 100

# 입출력 예
# 입력 #1
# 4 5
# 출력 #1
# 4 + 5 = 9


# 코드

a, b = map(int, input().strip().split(' '))
print(a, "+", b,"=", a+b)



#
# 2. 문자열 붙여서 출력하기

# 문제 설명
# 두 개의 문자열 str1, str2가 공백으로 구분되어 입력으로 주어집니다.
# 입출력 예와 같이 str1과 str2을 이어서 출력하는 코드를 작성해 보세요.

# 제한사항
# 1 ≤ str1, str2의 길이 ≤ 10

# 입출력 예
# 입력 #1
# apple pen
# 출력 #1
# applepen

# 입력 #2
# Hello World!
# 출력 #2
# HelloWorld!


# 코드 

str1, str2 = input().strip().split(' ')
print(str1 + str2)



#
# 3. 문자열 돌리기

# 문제 설명
# 문자열 str이 주어집니다.
# 문자열을 시계방향으로 90도 돌려서 아래 입출력 예와 같이 출력하는 코드를 작성해 보세요.

# 제한사항
# 1 ≤ str의 길이 ≤ 10

# 입출력 예
# 입력 #1
# abcde
# 출력 #1
# a
# b
# c
# d
# e


# 코드

str = input()
for a in str:
    print(a)



#
# 4. 홀짝 구분하기

# 문제 설명
# 자연수 n이 입력으로 주어졌을 때 만약 n이 짝수이면 "n is even"을, 홀수이면 "n is odd"를 출력하는 코드를 작성해 보세요.

# 제한사항
# 1 ≤ n ≤ 1,000
# 입출력 예
# 입력 #1

# 100
# 출력 #1

#100 is even
# 입력 #2

# 1
# 출력 #2

#1 is odd
# ※ 2023년 05월 15일 지문이 수정되었습니다.


# 코드

a = int(input())

if a % 2 == 0:
    print(f'{a} is even')
else:
    print(f'{a} is odd')



#
# 5. 문자열 겹쳐쓰기

# 문제 설명
# 문자열 my_string, overwrite_string과 정수 s가 주어집니다. 문자열 my_string의 인덱스 s부터 overwrite_string의 길이만큼을 문자열 overwrite_string으로 바꾼 문자열을 return 하는 solution 함수를 작성해 주세요.

# 제한사항
# my_string와 overwrite_string은 숫자와 알파벳으로 이루어져 있습니다.
# 1 ≤ overwrite_string의 길이 ≤ my_string의 길이 ≤ 1,000
# 0 ≤ s ≤ my_string의 길이 - overwrite_string의 길이

# 입출력 예
# my_string	overwrite_string	s	result
# "He11oWor1d"	          "lloWorl"	2	"HelloWorld"
# "Program29b8UYP"	"merS123"	7	"ProgrammerS123"

# 입출력 예 설명
# 입출력 예 #1

# 예제 1번의 my_string에서 인덱스 2부터 overwrite_string의 길이만큼에 해당하는 부분은 "11oWor1"이고 이를 "lloWorl"로 바꾼 "HelloWorld"를 return 합니다.
# 입출력 예 #2

# 예제 2번의 my_string에서 인덱스 7부터 overwrite_string의 길이만큼에 해당하는 부분은 "29b8UYP"이고 이를 "merS123"로 바꾼 "ProgrammerS123"를 return 합니다.


#코드

def solution(my_string, overwrite_string, s):
    answer = my_string[:s] + overwrite_string + my_string[s+len(overwrite_string):]
    return answer



#
# a 와 b 출력하기

# 문제 설명
# 정수 a와 b가 주어집니다. 각 수를 입력받아 입출력 예와 같은 형식으로 출력하는 코드를 작성해 보세요.

# 제한사항
# -100,000 ≤ a, b ≤ 100,000

# 입출력 예
# 입력 #1
# 4 5
# 출력 #1
# a = 4
# b = 5


# 코드

a, b = map(int, input().strip().split(' '))
print("a =",a) 
print("b =",b)



#
# 문자열 반복해서 출력하기

# 문제 설명
# 문자열 str과 정수 n이 주어집니다.
# str이 n번 반복된 문자열을 만들어 출력하는 코드를 작성해 보세요.

# 제한사항
# 1 ≤ str의 길이 ≤ 10
# 1 ≤ n ≤ 5

# 입출력 예
# 입력 #1
# string 5
# 출력 #1
# stringstringstringstringstring


# 코드

a, b = input().strip().split(' ')
print(a * int(b))



#
# 문자열 반복해서 출력하기

# 문제 설명
# 문자열 str과 정수 n이 주어집니다.
# str이 n번 반복된 문자열을 만들어 출력하는 코드를 작성해 보세요.

# 제한사항
# 1 ≤ str의 길이 ≤ 10
# 1 ≤ n ≤ 5

# 입출력 예
# 입력 #1
# string 5
# 출력 #1
# stringstringstringstringstring


# 코드

a, b = input().strip().split(' ')
print(a * int(b))