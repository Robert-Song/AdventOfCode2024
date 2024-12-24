import random
from collections import Counter

# 초기화
deck = [1, 1, 1, 2, 2, 3]  # 덱 구성
num_simulations = 10**7     # 시뮬레이션 반복 횟수
play_count = Counter()      # 각 카드가 플레이된 횟수 기록
removed_cards = Counter() # 각 카드가 버려진 횟수 기록

deck_state = deck.copy()
random.shuffle(deck_state)  # 덱 섞기
hand = [deck_state.pop(), deck_state.pop()]  # 초기 손패
# 시뮬레이션 실행
for _ in range(num_simulations):
    if 3 in hand:  # 3카드가 있으면 플레이
        play_count[3] += 1
        hand.remove(3)
        removed_cards[hand[0]] += 1
        hand.clear()
        hand.append(deck_state.pop())
        if len(deck_state) == 0 :
            deck_state = deck.copy()
            random.shuffle(deck_state)
        hand.append(deck_state.pop())
        if len(deck_state) == 0:
            deck_state = deck.copy()
            random.shuffle(deck_state)
    elif 2 in hand:  # 3카드가 없고 2카드가 있으면 플레이
        play_count[2] += 1
        hand.remove(2)
        removed_cards[hand[0]] += 1
        hand.clear()
        hand.append(deck_state.pop())
        if len(deck_state) == 0:
            deck_state = deck.copy()
            random.shuffle(deck_state)
        hand.append(deck_state.pop())
        if len(deck_state) == 0 :
            deck_state = deck.copy()
            random.shuffle(deck_state)
    elif hand == [1, 1]:  # 1카드만 있으면 플레이
        play_count[1] += 1
        hand.remove(1)
        hand.append(deck_state.pop())
        if len(deck_state) == 0:
            deck_state = deck.copy()
            random.shuffle(deck_state)
    else:
        print("error!")
        break

# 결과 출력
total_plays = sum(play_count.values())
print({k: v / total_plays for k, v in play_count.items()})
print({k: v for k, v in removed_cards.items()})

print(0.4633399*4 + 0.2885781*4 + 0.248082*3)
print(1/6*4 + 1 + 1/2*3)

