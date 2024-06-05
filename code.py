inputs = [84, 8, 4, 2, 7, 9, 0, 1, 9, 8, 3]
#first number is starting total
#next 3 are player's cards
total = inputs[0]
remaining_hands = inputs[6:]
player_hand = inputs[1:5]
player_hand.append(inputs[6])
player_hand.append(inputs[8])
player_hand.append(inputs[10])

dealer_hand = inputs[5:5]
dealer_hand.append(inputs[5])
dealer_hand.append(inputs[7])
dealer_hand.append(inputs[9])
focus_p = 0
focus_d = 0
winner = ""
focus = player_hand[0]
banned = [9, 4, 0]
for i in range(1,len(inputs)): 
    if i % 2 == 1:
        focus = player_hand[focus_p]
        focus_p += 1
        winner = "dealer"
    else:
        focus = dealer_hand[focus_d]
        focus_d += 1
        winner = "player"
    if focus not in banned:
        total = total + focus
    if focus == banned[0]:
        total = total + 0
    elif focus == banned[1]:
        total = total - 10
    elif focus == banned[2]:
        if total <= 88:
            total = total + 11
        else: 
            total = total + 1
    if total > 99:
        print(total, winner)
        break 
    
    
