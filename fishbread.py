stock = {
    "팥붕어빵" : 0,
    "슈크림붕어빵" : 0,
    "초코붕어빵" : 0
}

salse = {
    "팥붕어빵" : 0,
    "슈크림붕어빵" : 0,
    "초코붕어빵" : 0
}

price = {
    "팥붕어빵" : 400,
    "슈크림붕어빵" : 500,
    "초코붕어빵" : 500
}

# 주문기능
def order_bread():
    while True:
        print("\n" + "=" * 70)
        print("                 주문할 붕어빵맛을 입력 해주세요")
        print("              [ 팥붕어빵, 슈크림붕어빵, 초코붕어빵 ]")
        print("            ❌뒤로가길 원하시면 뒤로가기를 입력하세요❌")
        print("=" * 70)
        bread_type = input('>')
        if bread_type == "뒤로가기":
            print('                      뒤로 돌아갑니다')
            break
        if bread_type in stock:
            print("=" * 70)
            print("                   구매할 갯수를 입력하세요")
            print("=" * 70)
            bread_count = int(input('>'))
            if  stock[bread_type] >= bread_count:
                stock[bread_type] -= bread_count
                salse[bread_type] += bread_count
                print("=" * 70)
                print(f'                {bread_type}을 {bread_count}개 구매하셨습니다')
                print("=" * 70)
            else:
                print("=" * 70)
                print(f'          재고가 부족 합니다 현재 {stock[bread_type]}개만 주문 가능합니다')
                print("=" * 70)
        else:
            print("=" * 70)
            print('                  ❌잘못 입력 하셨습니다❌')
            print("=" * 70)

# 붕어빵 admin 기능
def admin_mode():
    PASSWORD = "1234"  # 관리자 비밀번호

    print("\n" + "=" * 70)
    print("                        ★관리자 모드★")
    print("                      비밀번호를 입력해주세요")
    print("=" * 70)
    password_attempt = input(">")

    if password_attempt != PASSWORD:
        print("=" * 70)
        print("                ❌ 비밀번호가 일치하지 않습니다 ❌")
        print("                        메인으로 돌아갑니다")
        print("=" * 70)
        return

    print("=" * 70)
    print("                    ✓ 로그인 성공했습니다")
    print("=" * 70)
    while True:
        print("\n" + "=" * 70)
        print("                 추가할 붕어빵 맛을 입력해주세요")
        print("              [ 팥붕어빵, 슈크림붕어빵, 초코붕어빵 ]")
        print("           ❌뒤로 돌아가시려면 뒤로가기를 입력해주세요❌")
        print("=" * 70)
        bread_type = input('>')
        if bread_type == "뒤로가기":
            print("=" * 70)
            print('                       뒤로 돌아갑니다')
            print("=" * 70)
            break
        if bread_type in stock:
            print("=" * 70)
            print("                  추가할 수량을 입력 해주세요")
            print("=" * 70)
            bread_count = int(input('>'))
            print("=" * 70)
            stock[bread_type] += bread_count
            print(f"                    {bread_count}개가 추가 되었습니다")
            print(f"                      현재 재고 : {stock[bread_type]}개")
            print("=" * 70)
        else:
            print("=" * 70)
            print("                  ❌ 정확하게 입력 해주세요❌")
            print("               EX ) 초코붕어빵, 팥붕어빵, 슈크림붕어빵")
            print("=" * 70)

def calculate_sales():
    total_sales = sum(salse[key] * price[key] for key in salse)
    return total_sales



# 모드선택, 메인메뉴
while True:
    print("\n" + "=" * 70)
    print("                 ★붕어빵 재고 관리 시스템★")
    print("         원하는 모드를 선택하세요 [주문, 관리자, 종료]")
    print("=" * 70)
    mode = input(">")
    if mode == "종료":
        print("=" * 70)
        print('                       시스템이 종료 됩니다')
        print("=" * 70)
        break
    elif mode == "주문":
        order_bread()
    elif mode == "관리자":
        admin_mode()
    else:
        print("=" * 70)
        print('                    ❌잘못 입력 하셨습니다❌')
        print("=" * 70)

