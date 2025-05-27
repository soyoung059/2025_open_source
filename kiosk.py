menus = [
    ["아이스 아메리카노", 0, 2000],
    ["카페 라떼", 0, 2500],
    ["유자차", 0, 2400],
    ["자바칩 프라푸치노", 0, 7000]
]  # [[메뉴, 수량, 단가], ...]

def select_menu(i):
    """
    1) 메뉴 선택 시 해당 메뉴 중간 디스플레이
    2) 선택한 메뉴 수량 업데이트
    3) 소계 기능
    :param i: 선택한 메뉴 - 1
    :return: 없음
    """
    menus[i][1] = menus[i][1] + 1
    print(f"{menus[i][0]} {menus[i][1]}잔 주문...")
    subtotal = 0
    for j in range(len(menus)):
        subtotal = subtotal + (menus[j][2] * menus[j][1])  # (단가 * 수량) 누적
    print(f"소계 : {subtotal}")


def print_receipt():
    """
    영수증 출력 기능
    :return: 없음
    """
    print("=" * 38)
    total_price = 0
    for j in range(len(menus)):
        if menus[j][1] > 0:  # 각 메뉴들의 수량이 1 이상이면
            print(f"품명: {menus[j][0]}\n\t단가: {menus[j][2]} / 수량: {menus[j][1]:2} / 금액: {menus[j][1] * menus[j][2]:6}")
            total_price = total_price + (menus[j][1] * menus[j][2])  # 가격 리스트에서 가격 추출해서 합산
    print(f"총 금액은 {total_price}원 입니다.")


def get_ticket_number():
    """
    번호표 기능 (파일 입출력)
    :return: 번호
    """
    try:
        with open("ticket.txt", "r") as fp:
            number = int(fp.read())
    except FileNotFoundError:
        number = 0

    number = number + 1

    with open("ticket.txt", "w") as fp:
        fp.write(str(number))

    return number

