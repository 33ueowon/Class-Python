# 5개의 정수 입력받기
numbers = []
for i in range(1, 6):
    while True:
        try:
            num = int(input(f"점수 {i} 입력: "))
            numbers.append(num)
            break
        except ValueError:
            print("정수를 입력해주세요.")

# 입력된 점수 출력
print("입력된 점수:", numbers)

# 합계 계산
total = sum(numbers)

# 평균 계산 (소수점 둘째자리까지)
average = total / 5

# 결과 출력
print(f"합계: {total}")
print(f"평균: {average:.2f}")

# 합격 여부 판단
if average >= 60:
    print("합격")
else:
    print("불합격")
