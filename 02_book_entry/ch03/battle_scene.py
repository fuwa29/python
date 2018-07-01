import random

hit_pt_me = 15   # my hit point
hit_pt_slime = 7 # slime hit point

index =0 # 攻撃の順番

while hit_pt_me > 0 and hit_pt_slime > 0:
    # ダメージを乱数にて設定
    attack = random.randint(1,7)

    # 交互に攻撃
    if index % 2 == 0:
        # my turn
        print('スライムに　' + str(attack) + '　のダメージを与えた！')
        hit_pt_slime -= attack
        print('スライムのHP＝',hit_pt_slime)
    else:
        # slime turn
        print('勇者は　' + str(attack) + '　のダメージを受けた！')
        hit_pt_me -= attack
        print('勇者のHP＝',hit_pt_me)
    index += 1

# finished battle
if hit_pt_me > 0:
    print('勇者の勝利！スライムをやっつけた！')
elif hit_pt_slime > 0:
    print('勇者は死んでしまった！！')
