from fishbread_model import BreadShop

shop = BreadShop()



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
         shop.order_bread()
    elif mode == "관리자":
         shop.admin_mode()
    else:
        print("=" * 70)
        print('                    ❌잘못 입력 하셨습니다❌')
        print("=" * 70)

