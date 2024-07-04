# 초기 데이터 딕셔너리로 정의
products = {
    '메로나': {'가격': 1000, '수량': 20},
    '비비빅': {'가격': 700, '수량': 3},
    '바밤바': {'가격': 850, '수량': 100}
}

# 딕셔너리 데이터 출력
print("상품명\t가격\t수량")
for product, info in products.items():
    print(f"{product}\t{info['가격']}\t{info['수량']}")
