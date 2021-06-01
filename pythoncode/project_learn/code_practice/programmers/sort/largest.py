# 프로그래머스_정렬_가장 큰 수

# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return
# numbers = [6, 10, 2]

# 조건: numbers의 원소는 0 이상 1,000 이하

def solution(a):
    # 문자열이 3번 반복되었을 때(1,000 이하) 큰 문자열 순으로 정렬
    numbers = sorted(list(map(str, a)), key=lambda x: x*3, reverse=True)
    # 정렬된 순으로 조인
    ans= str(int(''.join(numbers)))
    return ans
