#몇 명의 성적을 입력 받아서 총 점과 평균을 출력(반올림 소수점 첫째자리 까지만)

Score = input().split()     #split= 리스트 생성
# Score = list(map(int, input().split()))
Sum = 0
for i in Score:
    Sum += int(i)

print(Sum)
Avr = Sum/len(Score)
print("{:.1f}".format(Avr))

