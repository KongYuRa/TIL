# 1. 자료형의 종류

print(12345)         # 숫자 자료형
print('안녕하세요', "안녕하세요")     # 문자 자료형
print(True / False)    # 불리안 자료형



# 2. 변수란? 어떤 값을 저장하는 공간

a = 10               # a 라는 공간에 10이라는 값을 저장 / 이렇게 적는 방식이 변수 선언

print(a)             # 변수 값을 출력하기 위해서는 print 함수 사용


# 2-1 변수 이름 규칙
# 1) 문자 또는 _ 로 시작
# 2) 문자, 숫자, _로 구성
# 3) 공백 X, 특수문자 X
# 4) 대소문자 구분
# 5) 키워드(예약어) X
# 6) 소문자 단어, _로 구분된 단어들 (권장)



# 3. 형 변환

int('2')           # 정수로
int('two')         # 문자 형태이기 때문에 X
int(float('2.5'))  # 실수 형태이기 때문에 float()를 통해 실수 변환 후 정수로 변환 가능(소수점은 버림 되므로 2로 출력)

float('1.5')       # 실수로

str(2)             # 문자로

bool()             # 불리안으로 (참이거나 값이 있으면 True / 거짓이거나 값이 없으면 False)



# 4-1. 연산자

print(5+2)          # 더하기
print(5-2)          # 뻬기
print(5*2)          # 곱하기
print(5/2)          # 나누기
print(5%2)          # 나머지
print(5//2)         # 몫
print(5**2)         # 제곱


# 4-2. 비교 연산자 (불리안)

print(5>2)          # 크다
print(5>=2)         # 크거나 같다
print(5<2)          # 작다
print(5<=2)         # 작거나 같다
print(5==2)         # 같다
print(5!=2)         # 같지 않다


# 4-3. 논리 연산자

print(3<5 and 7<5)  # 둘 다 참이면 True
print(3<5 or 7<5)   # 하나라도 참이면 True
print(not 3<5)      # 반전


# 4-4. 멤버 연산자

print('c' in 'cat')      #포함
print('f' not in 'cat')  #미포함



# 5. 주석

# 실제로 읽지는 않지만,참고하기 위해 적어두는 부연 설명 또는 메모

'''
안녕하세요!
# 옆에 있는 친구에게
너도 안녕!
'''

# 5-1. 주석 처리 방법
# 1) 한 줄 주석 : 주석 대상 앞에 # 추가
# 2) 여러 줄 주석 : 대상 영역 앞 뒤에 ''',''' 추가


# 5-2. 주석 사용
# 복잡한 코드에 부연 설명이 필요할 때
# 다른 개발자에게 메모를 남길 때
# 테스트 목적으로 일부 코드의 실행을 막을 때



# 6. 인덱스

# 몇 번째 = 인덱스 
# 0 부터 시작

lang = 'PYTHON'
print(lang[0])      # PYTHON 문자에서 첫 번째 문자 출력
print(lang[5 / -1]) # PYTHON 문자에서 마지막 문자 출력 (마지막 값인 5를 써도 되지만, -1이 마지막 값 이라는 의미)

# P    Y    T    H    O    N
# 0    1    2    3    4    5
# -6  -5   -4   -3   -2   -1



# 7. 슬라이싱

# 어디부터 : 어디까지 = 슬라이싱

lang[0:3]           # 슬라이싱
lang[2:]              # 원하는 구간 부터 끝까지
lang[:4]                # 원하는 처음부터 원하는 구간 까지
lang[:]                   # 처음부터 끝까지



# 8-1. 문자열 처리

num = 3
num = num+2
num += 2 #위 문장과 동일

num -+ 1
num *= 2
num /= 4 


# 8-2. 길이(length)

snack = '쿠크다스'  # 몇 글자?
print(len(snack)) # 4

#여러줄 문자

'''
쿠크다스
맛있다
'''

snack = '''쿠크다스
맛있다'''



# 9. 메소드

# 클래스 내에 정의된 어떤 동작, 기능을 하는 코드들의 묶음
# 문자열.메소드(...)


letter = 'how are YOU?'

#모든 내용을 소문자로
print(letter.lower())

#모든 내용을 대문자로
print(letter.upper())

# 첫 글자만 대문자로
print(letter.capitalize())

# 각 단어들의 첫 글자만 대문자로
print(letter.title())

# 대소문자를 서로 반대로
print(letter.swapcase())

# 문자열 분리 (띄어쓰기 기준으로 나뉘어 리스트 형태로 변환)
print(letter.split())

# 특정 단어의 수
print(letter.count('how'))


s = '나도고등학교'

# 어떤 값으로 시작하는지
print(s.startswith('나도'))

# 어떤 값으로 끝나는지
print(s.endswith('초등학교'))

# 앞 뒤로 불필요한 부분 제거 (괄호 안에 아무것도 적지 않으면 불필요한 공백 제거)
print(s.strip(''))

# 원하는 단어 변경
print(s.replace('고등학교','고교'))

# 원하는 단어 위치 찾기
print(s.find('학교'))

# 다른 문자 사이에 가운데로 입력(10글자 내에 문자가 들어가고, 양 옆으로 - 입력)
print(s.center(10,'-'))



# 10. 문자열 포맷

python = '파이썬'
java = '자바'

#다른 문장 속에 넣으려면
print('개발 언어에는' + python + ',' + java + '등이 있어요')
print('개발 언어에는', python, ',', java, '등이 있어요')


# 1) { } + format
print('개발 언어에는 {}, {} 등이 있어요'.format(python, java))

# 2) {N} + format / N : 0, 1, 2 ...
print('개발 언어에는 {1}, {0} 등이 있어요'.format(python, java))

# 3) f-string (바로 출력)
print(f'개발 언어에는 [python], [java]등이 있어요')



# 11. 탈출 문자

# 역슬래시(\)와 특정 문자(숫자)의 조합으로 표현할 수 없는 기능이나 문자를 표시
# 큰 따옴표는 \"   작은 따옴표는 \'

'''
하지만 '나만 당할 순 없지' 라는 생각에 "엄청 쉽지" 라고 했다.
'''

print('하지만\'나만 당할 순 없지\'라는 생각에\"엄청 쉽지\"라고 했다.')


#경로 입력 시 역슬래시 두 번(\\) 사용하지 않으면 오류 발생
print('C:\\Users\\Documents')


# 줄바꿈은 \n
print('쿠크다스\n맛있다')



# 12. 리스트

# 대괄호
# 리스트 = [값1, 값2, ...]
# 숫자, 불리안, 문자 모두 가능
# 중복값 허용
#빈 리스트 가능
#순서대로 관리


my_list = ['국어', '수학', '영어']
your_list = ['사회', '과학']

# 인덱스에 해당하는 값 확인
print(my_list[0])

# 슬라이싱
print(my_list[0:2])

# 리스트에 포함 되어 있는지
print('수학' in my_list)

# 리스트에 몇 개의 값?
print(len(my_list))

# 리스트 값 수정
my_list[1] = '수학익힘'
print(my_list)

# 리스트 맨 뒤에 값 추가
my_list.append('과학')
print(my_list)

# 리스트 값 삭제
my_list.remove('영어')
print(my_list)

# 리스트 확장(기존 리스트에 다른 리스트 인덱스 추가)
my_list.extend(your_list)
print(my_list)

# 이외 추가적인 리스트 메소드
# 1) insert()  원하는 위치에 값 추가
# 2) pop()     원하는 위치(또는 마지막) 삭제
# 3) clear()   모든 값 삭제
# 4) sort()    값 순서대로 정렬
# 5) reverse() 순서 뒤집기
# 6) copy()    리스트 복사
# 7) count()   어떤 값이 몇 개 있는지
# 8) index()   어떤 값이 어디에 있는지



# 13. 튜플

# 소괄호
# 튜플 = (값1, 값2, ...)
# 한 번 만들면 수정 불가 (읽기 전용 리스트) 그 외에는 리스트와 비슷
# 숫자, 불리안, 문자 모두 가능
# 중복값 허용
# 순서대로 관리


my_tuple = ('국어', '수학','영어') #패킹 (각 값을 튜플에 입력)
(pie1, pie2, pie3) = my_tuple #언패킹 (각 변수에 튜플 값을 입력) (* 사용 가능)

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
(one, two, *others) = numbers #1, 2 제외한 나머지 숫자는 others 변수에 입력(이때 others는 리스트)
(*others, nine, ten) = numbers
(one, *others, ten) = numbers



# 14. 셋

# 셋 = {값1, 값2, ...}
# 순서 X, 중복 X
# 순서가 없기 때문에 인덱스 X


A = {'하늘', '나무', '물'}
B = {'풀', '화분', '물'}

# 교집합
print(A.intersection(B))

# 합집합 (중복이 허용되지 않으므로 중복된 값은 하나만 입력)
print(A.union(B))

# 차집합
print(A.difference(B))


my_set = {'하늘', '나무', '물'}

# 추가
my_set.add('땅')

# 제거
my_set.remove('나무')

# 모든 값 제거
my_set.clear() # 값이 없는 셋

# 셋 제거
del my_set # 완전 삭제


# 이외 추가적인 셋 메소드
# 1) copy()         셋 복사
# 2) discard()      값 삭제 (해당 값이 없어도 에러 발생 X)
# 3) isdisjoint()   두 셋에 겹치는 값이 없는지 여부
# 4) issubset()     다른 셋의 부분집합인지 여부
# 5) issuperset()   다른 셋의 상위집합인지 여부
# 6) update()       다른 셋의 값들을 더함


# 이후 추가 예정