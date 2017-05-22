import random,time

def Select():
    while True:
        try:
            number_CPU=int(input("CPUの数を入力してください(1人～8人)>"))
            if number_CPU>8 or number_CPU<1:
                print("無効です")
            else:
                Player_tarn=random.randint(1,number_CPU+1)
                member=[number_CPU,Player_tarn]
                return member
        except:
            print("無効です")
    

def CPU():
    print("CPUのターンです")
    time.sleep(1.5)
    action_CPU=random.randint(1,3)
    print("{}を選択しました\n".format(action_CPU))
    return action_CPU

def Player():
    print("あなたのターンです")
    while True:
        try:  
            action_Player=int(input("+1,+2,+3をえらんでください>"))
            if action_Player>3 or action_Player<1:
                print("無効です")
            else:
                return action_Player
        except:
            print("無効です")

def Game():
    point=0
    tarn=1
    member=Select()
    number_CPU=member[0]
    Player_tarn=member[1]
    
    print("あなたは{}番目です".format(Player_tarn))
    time.sleep(1.5)

    while True:
        if tarn==Player_tarn:
            point=point+Player()
        else:
            point=point+CPU()
        print("現在の数>{}\n".format(point))
        time.sleep(1.5)

        if point>=30:
            print("30を超えました\n")
            time.sleep(1.5)
            break

        if tarn==number_CPU+1:
            tarn=0

        tarn=tarn+1

    if tarn==Player_tarn:
        print("あなたの負けです")

    else:
        print("あなたの勝ちです")

Game()

        
    
    
