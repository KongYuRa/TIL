# 옹알이 (1)
# 문제 설명
# 머쓱이는 태어난 지 6개월 된 조카를 돌보고 있습니다. 
# 조카는 아직 "aya", "ye", "woo", "ma" 네 가지 발음을 최대 한 번씩 사용해 조합한(이어 붙인) 발음밖에 하지 못합니다. 
# 문자열 배열 babbling이 매개변수로 주어질 때, 머쓱이의 조카가 발음할 수 있는 단어의 개수를 return하도록 solution 함수를 완성해주세요.


# 제한사항
# 1 ≤ babbling의 길이 ≤ 100
# 1 ≤ babbling[i]의 길이 ≤ 15
# 'babbling'의 각 문자열에서 "aya", "ye", "woo", "ma"는 각각 최대 한 번씩만 등장합니다.
# 즉, 각 문자열의 가능한 모든 부분 문자열 중에서 "aya", "ye", "woo", "ma"가 한 번씩만 등장합니다.
# 문자열은 알파벳 소문자로만 이루어져 있습니다.


# 입출력 예
# babbling                                  	 result
# ["aya", "yee", "u", "maa", "wyeoo"]	           1
# ["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]	   3


# 입출력 예 설명
# 입출력 예 #1
# ["aya", "yee", "u", "maa", "wyeoo"]에서 발음할 수 있는 것은 "aya"뿐입니다. 따라서 1을 return합니다.

# 입출력 예 #2
# ["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]에서 발음할 수 있는 것은 "aya" + "ye" = "ayaye", "ye", "ye" + "ma" + "woo" = "yemawoo"로 3개입니다. 따라서 3을 return합니다.


# 유의사항
# 네 가지를 붙여 만들 수 있는 발음 이외에는 어떤 발음도 할 수 없는 것으로 규정합니다. 
# 예를 들어 "woowo"는 "woo"는 발음할 수 있지만 "wo"를 발음할 수 없기 때문에 할 수 없는 발음입니다.
# ※ 공지 - 2022년 10월 27일 문제 지문이 리뉴얼되었습니다. 기존에 제출한 코드가 통과하지 못할 수도 있습니다.


# 코드

def solution(babbling):   # 단어 목록 babbling을 받아서 조카가 발음할 수 있는 단어 개수를 세는 함수 정의
    speakable = ["aya", "ye", "woo", "ma"]   # 조카가 발음할 수 있는 4개의 단어 리스트 정의
    answer = 0   # 최종적으로 발음 가능한 단어 개수를 저장할 변수 초기화

    for word in babbling:   # babbling 리스트의 각 단어(word)를 하나씩 반복하며 검사
        original = word   # 나중에 중복 단어 확인을 위해 현재 단어의 원본 저장
        for speak in speakable:   # 발음 가능한 단어들 중 하나씩 꺼냄
            word = word.replace(speak, " ")   # 해당 발음이 현재 단어에 있다면 빈 칸(" ")으로 바꿈 (제거 효과)

        if word.strip() == "":   # 모든 발음 가능한 단어를 제거한 후, 남은 문자가 없다면(공백만 있다면)
            is_valid = True   # 중복 발음 여부를 확인하기 위한 변수 설정 (처음엔 유효하다고 가정)
            for speak in speakable:   # 네 가지 발음을 하나씩 확인하면서
                if speak * 2 in original:   # 같은 발음이 연속해서 2번 이상 등장했다면
                    is_valid = False   # 유효하지 않은 단어로 표시
                    break   # 중복이 발견되었으므로 더 이상 확인할 필요 없이 반복 종료

            if is_valid:   # 중복 없이 유효한 단어라면
                answer += 1   # 발음 가능한 단어 개수를 하나 증가시킴

    return answer   # 최종적으로 발음 가능한 단어의 총 개수를 반환