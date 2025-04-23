stock = {
    "팥붕어빵" : 10,
    "슈크림붕어빵" : 8,
    "초코붕어빵" : 7
}

salse = {
    "팥붕어빵" : 0,
    "슈크림붕어빵" : 0,
    "초코붕어빵" : 0
}

def order_bread():
    while True:
        bread_type = input('주문할 붕어빵맛을 입력해주세요(팥붕어빵, 슈크림붕어빵, 초코붕어빵) 만약 뒤로가길 원하시면 뒤로가기를 입력하세요')
        if bread_type == "뒤로가기":
            print('뒤로 돌아갑니다')
            break
        if bread_type in stock:
            bread_count = int(input('구매할 갯수를 입력하세요 :'))
            if  stock[bread_type] >= bread_count:
                stock[bread_type] -= bread_count
                salse[bread_type] += bread_count
                print(f'{bread_type}를 {bread_count}개 구매하셨습니다')
            else:
                print(f'재고가 부족합니다 현재 {stock[bread_type]}개만 주문 가능합니다')
        else:
            print('잘못입력하셨습니다')



while True:
    mode = input("원하는 모드를 선택하세요(주문, 관리자, 종료):")
    if mode == "종료":
        print('시스템이 종료되었습니다')
        break
    elif mode == "주문":
        order_bread()
    elif mode == "관리자":
        admin_mode()
    else:
        print('잘못 입력 하셨습니다')