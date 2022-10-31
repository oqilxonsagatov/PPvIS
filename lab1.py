import random
import sys
import time

class soccerShootout:
    player_team = ""
    virtual_player_team = ""
    player_shootout_blocks = 0
    player_shootout_goals = 0
    count_player = 0
    virtual_player_shootout_goals = 0
    virtual_player_shootout_blocks = 0
    count_virtual_player = 0
    event_count = 0
    impact_force = 100

    def increaseEventCount():
        soccerShootout.event_count += 1

    def increaseCountPlayer():
        soccerShootout.count_player += 1

    def increasePlayerShootoutGoals():
        soccerShootout.player_shootout_goals += 1

    def increasePlayerShootoutBlocks():
        soccerShootout.player_shootout_blocks += 1

    def increaseCountVirutalPlayer():
        soccerShootout.count_virtual_player += 1

    def increaseVirutalPlayerShootoutGoals():
        soccerShootout.virtual_player_shootout_goals += 1

    def increaseVirtualPlayerShootoutBlocks():
        soccerShootout.virtual_player_shootout_blocks += 1

def playerTeamRandom():
    player_team = ["Россия", "Узбекистан", "Германия"]
    for name in random.sample(player_team, 1):
        player_team = name
        player_team = player_team.upper()
    soccerShootout.player_team = player_team

def virtualPlayerTeamRandom():
    virtual_player_team = ["Украина", "Казахстан", "Беларусь"]
    for name in random.sample(virtual_player_team, 1):
        virtual_player_team = name
        virtual_player_team = virtual_player_team.upper()
    soccerShootout.virtual_player_team = virtual_player_team

def soccerEvent():
    soccerShootout.increaseEventCount()
    pt = soccerShootout.player_team
    vpt = soccerShootout.virtual_player_team
    ec = soccerShootout.event_count
    print(f"Привет: Добро пожаловать в футбол - {ec} ")
    print("Местоположение: Минск, Беларусь")
    print(f"\n{pt} против {vpt} ")
    print(f"Вы будете представлять {pt} и противник - это {vpt}.")
    print("Пусть начнется футбольная перестрелка!")

def playerKicker():
    pt = soccerShootout.player_team
    print(f"\nВы будете представлять в команде {pt} в качестве кикера.")

def playerGoalie():
    pt = soccerShootout.player_team
    print(f"\nВы будете представлять в команде {pt} в качестве кикера.")
    print("вратарь")

def playerShootoutKicks():
    soccerShootout.increaseCountPlayer()
    cp = soccerShootout.count_player
    pt = soccerShootout.player_team
    impact_force = 100
    while (cp >= 1 and cp <= 3):
        time.sleep(1)
        print(f"\nСила удара по умолчанию: {impact_force}")
        impact_force = int(input("Выбирайте сила удар: "))
        print(f"\nПодготовка к удару в серии {cp}. Куда ты будешь бить по мячу? ")
        ball_kick = input("Пожалуйста, введите слева, по центру или справа: ")
        ball_direction = ball_kick.upper()
        time.sleep(1)
        while (ball_direction != "СЛЕВА" and ball_direction != "ЦЕНТРУ" and ball_direction != "СПРАВА") and (impact_force >= 50):
            print("\nInvalid input.")
            ball_kick = input("Пожалуйста, введите слева, по центру или справа: ")
            ball_direction = ball_kick.upper()
        directions = ["СЛЕВА", "ЦЕНТРУ", "СПРАВА"]
        for i in random.sample(directions, 1):
            kicker_location = i
        if ball_direction == kicker_location:
            soccerShootout.increasePlayerShootoutGoals()
            ipsg = soccerShootout.player_shootout_goals
            time.sleep(1)
            print(f"\nВы забили гол с {kicker_location}.")
            print(f"{pt} забил гол {ipsg} гол(ы)")
            playerShootoutKicks()
        else:
            soccerShootout.increaseVirtualPlayerShootoutBlocks()
            time.sleep(1)
            print(f"\nВратарь заблокировал удар с {kicker_location}.")
            playerShootoutKicks()
    else:
        playerGoalie()
        virtualPlayerShootoutKicks()

def virtualPlayerShootoutKicks():
    directions = ["СЛЕВА", "ЦЕНТРУ", "СПРАВА"]
    soccerShootout.increaseCountVirutalPlayer()
    cvp = soccerShootout.count_virtual_player
    vpt = soccerShootout.virtual_player_team
    while (cvp >= 1 and cvp <= 3):
        time.sleep(1)
        print(f"\nПодготовка к удару в серии в {cvp} для {vpt}. Где вы попытаетесь заблокировать мяч?")
        ball_kick = input("Пожалуйста, введите слева, по центру или справа: ")
        ball_direction = ball_kick.upper()
        time.sleep(1)
        while (ball_direction != "СЛЕВА" and ball_direction != "ЦЕНТРУ" and ball_direction != "СПРАВА"):
            print("\nInvalid input.")
            ball_kick = input("Пожалуйста, введите слева, по центру или справа: ")
            ball_direction = ball_kick.upper()
        for i in random.sample(directions, 1):
            kicker_location = i
        if ball_direction == kicker_location:
            soccerShootout.increaseVirutalPlayerShootoutGoals()
            ivpsg = soccerShootout.virtual_player_shootout_goals
            time.sleep(1)
            print(f"\n{vpt} забил гол с {kicker_location}.")
            print(f"{vpt} забил {ivpsg} гол(ы).")
            virtualPlayerShootoutKicks()
        else:
            pt = soccerShootout.player_team
            soccerShootout.increasePlayerShootoutBlocks()
            time.sleep(1)
            print(f"\n{pt} вратарь заблокировал удар с {kicker_location}.")
            virtualPlayerShootoutKicks()
    else:
        shootoutScore()

def shootoutScore():
    vpt = soccerShootout.virtual_player_team
    pt = soccerShootout.player_team
    psg = soccerShootout.player_shootout_goals
    vpsg = soccerShootout.virtual_player_shootout_goals
    print(f"\n{pt} {psg} - {vpt} {vpsg} ")
    if psg == vpsg:
        print(f"\nМатч завершилась ничьей.")
    elif psg > vpsg:
        print(f"\n{pt} Выигрывает!!!")
    elif psg < vpsg:
        print(f"\n{vpt} Выигрывает!!!")
    confirmPlay()

def confirmPlay():
    time.sleep(3)
    choice = int(input("\nВведите 1, чтобы продолжить игру, или 2, чтобы выйти: "))
    while choice < 1 or choice > 2:
        choice = int(input("\nНеверный ввод, пожалуйста, введите 1, чтобы продолжить игру, или 2, чтобы выйти:"))
    if choice == 1:
        reset()
        playSoccerShooutoutAgain()
    else:
        sys.exit()

def reset():
    soccerShootout.player_shootout_blocks = 0
    soccerShootout.player_shootout_goals = 0
    soccerShootout.count_player = 0
    soccerShootout.virtual_player_shootout_goals = 0
    soccerShootout.virtual_player_shootout_blocks = 0
    soccerShootout.count_virtual_player = 0

def playSoccerShooutoutAgain():
    playerTeamRandom()
    virtualPlayerTeamRandom()
    soccerEvent()
    playerKicker()
    playerShootoutKicks()

playerTeamRandom()
virtualPlayerTeamRandom()
soccerEvent()
playerKicker()
playerShootoutKicks()