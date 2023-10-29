# # 案例：请基于会员等级提供的折扣，计算商品的售价
# # 实现（1）
def discount():
    while True:
        grand = int(input('请输入您的会员等级：'
                          '*****1==gold_card, 2==silver_card, 3==common_card*****'))

        if grand == 1:
            dis = 0.85
            print(f'您是金卡会员，享受{dis}折扣优惠。')
            break
        elif grand == 2:
            dis = 0.9
            print(f'您是银卡会员，享受{dis}折扣优惠。')
            break
        elif grand == 3:
            dis = 1.0
            print(f'您是普通卡会员，享受{dis}折扣优惠。')
            break
        else:
            print(f'无效的会员等级。请重新输入。')

    prince = float(input('请输入商品单价：'))
    number = int(input('请输入购买数量：'))

    def count():
        result = prince * number
        pay = result * dis
        print(f'总价{result}，实付：{pay}')

    count()


discount()
