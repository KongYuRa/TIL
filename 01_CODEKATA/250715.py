# 1. 두 수의 곱 구하기

# 문제 설명
# 정수 num1, num2가 매개변수 주어집니다. num1과 num2를 곱한 값을 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# 0 ≤ num1 ≤ 100
# 0 ≤ num2 ≤ 100

# 입출력 예
# num1	 num2	result
# 3	     4	     12
# 27	19	     513

# 입출력 예 설명
# 입출력 예 #1
# num1이 3, num2가 4이므로 3 * 4 = 12를 return합니다.
# 입출력 예 #2
# num1이 27, num2가 19이므로 27 * 19 = 513을 return합니다.


# 코드


def solution(num1, num2):
    answer = num1 * num2
    return answer


#
# 2. 두 수의 합 구하기

#문제 설명

# 정수 num1과 num2가 주어질 때, num1과 num2의 합을 return하도록 soltuion 함수를 완성해주세요.

# 제한사항
# -50,000 ≤ num1 ≤ 50,000
# -50,000 ≤ num2 ≤ 50,000

# 입출력 예
# num1	num2	result
# 2   	3	    5
# 100	2	    102

# 입출력 예 설명
# 입출력 예 #1
# num1이 2이고 num2가 3이므로 2 + 3 = 5를 return합니다.
# 입출력 예 #2
# num1이 100이고 num2가 2이므로 100 + 2 = 102를 return합니다.


# 코드

def solution(num1, num2):
    answer = num1 + num2
    return answer



#
# 3. 두 수의 나눗셈

# 문제 설명
# 정수 num1과 num2가 매개변수로 주어질 때, num1을 num2로 나눈 값에 1,000을 곱한 후 정수 부분을 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# 0 < num1 ≤ 100
# 0 < num2 ≤ 100

# 입출력 예
# num1	num2	result
# 3	2	1500
# 7	3	2333
# 1	16	62

# 입출력 예 설명
# 입출력 예 #1
# num1이 3, num2가 2이므로 3 / 2 = 1.5에 1,000을 곱하면 1500이 됩니다.

# 입출력 예 #2
# num1이 7, num2가 3이므로 7 / 3 = 2.33333...에 1,000을 곱하면 2333.3333.... 이 되며, 정수 부분은 2333입니다.

# 입출력 예 #3
# num1이 1, num2가 16이므로 1 / 16 = 0.0625에 1,000을 곱하면 62.5가 되며, 정수 부분은 62입니다.


# 코드

def solution(num1, num2):
    answer = int(num1 / num2 * 1000)
    return answer



#
# 4. 두 수의 차 구하기

# 문제 설명
# 정수 num1과 num2가 주어질 때, num1에서 num2를 뺀 값을 return하도록 soltuion 함수를 완성해주세요.

# 제한사항
# -50000 ≤ num1 ≤ 50000
# -50000 ≤ num2 ≤ 50000

# 입출력 예
# num1	num2	result
# 2	    3	    -1
# 100 	2	    98

# 입출력 예 설명
# 입출력 예 #1
# num1이 2이고 num2가 3이므로 2 - 3 = -1을 return합니다.
# 입출력 예 #2
# num1이 100이고 num2가 2이므로 100 - 2 = 98을 return합니다.


# 코드

def solution(num1, num2):
    answer = num1 - num2
    return answer