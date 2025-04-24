class BreadShop:
    def __init__(self):
        self.stock = {"팥붕어빵" : 100, "슈크림붕어빵" : 100, "초코붕어빵" : 100}
        self.salse = {"팥붕어빵" : 0, "슈크림붕어빵" : 0, "초코붕어빵" : 0}
        self.price = {"팥붕어빵" : 400, "슈크림붕어빵" : 500, "초코붕어빵" : 500}

# 주문기능

    def order_bread(self):       #breadshop.order.bread()
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
            if bread_type in self.stock:
                print("=" * 70)
                print("                   구매할 갯수를 입력하세요")
                print("=" * 70)
                bread_count = int(input('>'))
                if  self.stock[bread_type] >= bread_count:
                    self.stock[bread_type] -= bread_count
                    self.salse[bread_type] += bread_count
                    print("=" * 70)
                    print(f'                {bread_type}을 {bread_count}개 구매하셨습니다')
                    print("=" * 70)
                else:
                    print("=" * 70)
                    print(f'          재고가 부족 합니다 현재 {self.stock[bread_type]}개만 주문 가능합니다')
                    print("=" * 70)
            else:
                print("=" * 70)
                print('                  ❌잘못 입력 하셨습니다❌')
                print("=" * 70)

    def calculate_sales(self):
        total_sales = sum(self.salse[key] * self.price[key] for key in self.salse)
        print("\n" + "=" * 70)
        print("                        ★매출 현황★")
        print("=" * 70)
        print("상품명".ljust(20) + "판매수량".ljust(15) + "가격".ljust(15) + "총액")
        print("-" * 70)
        for item in self.salse:
            item_total = self.salse[item] * self.price[item]
            print(f"{item}".ljust(20) + f"{self.salse[item]}개".ljust(15) +
                  f"{self.price[item]}원".ljust(15) + f"{item_total}원")
        print("-" * 70)
        print(f"총 매출액: {total_sales}원")
        print("=" * 70)



# 붕어빵 admin 기능
    def admin_mode(self):
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
            print("                        관리자 메뉴")
            print("              [ 재고추가, 매출현황, 재고현황, 뒤로가기 ]")
            print("=" * 70)
            menu = input('>')

            if menu == "뒤로가기":
                print("=" * 70)
                print("                      메인으로 돌아갑니다")
                print("=" * 70)
                break
            elif menu == "재고추가":
                self.add_stock()
            elif menu == "매출현황":
                self.calculate_sales()
            elif menu == "재고현황":
                print("\n" + "=" * 70)
                print("                        ★재고 현황★")
                print("=" * 70)
                print("상품명".ljust(20) + "현재 재고".ljust(15) + "가격")
                print("-" * 70)
                for item in self.stock:
                    print(f"{item}".ljust(20) + f"{self.stock[item]}개".ljust(15) + f"{self.price[item]}원")
                print("=" * 70)
            else:
                print("=" * 70)
                print("                    ❌잘못된 메뉴입니다❌")
                print("=" * 70)


    def add_stock(self):
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
            if bread_type in self.stock:
                print("=" * 70)
                print("                  추가할 수량을 입력 해주세요")
                print("=" * 70)
                try:
                    bread_count = int(input('>'))
                    print("=" * 70)
                    self.stock[bread_type] += bread_count
                    print(f"                    {bread_count}개가 추가 되었습니다")
                    print(f"                      현재 재고 : {self.stock[bread_type]}개")
                    print("=" * 70)
                except ValueError:
                    print("=" * 70)
                    print("                  ❌숫자만 입력해주세요❌")
                    print("=" * 70)
            else:
                print("=" * 70)
                print("                  ❌ 정확하게 입력 해주세요❌")
                print("               EX ) 초코붕어빵, 팥붕어빵, 슈크림붕어빵")
                print("=" * 70)
