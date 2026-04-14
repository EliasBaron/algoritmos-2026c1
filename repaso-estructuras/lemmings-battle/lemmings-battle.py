import heapq
import sys
input = sys.stdin.readline

def solve():
    B, SG, SB = map(int, input().split())
    
    green = [-int(input()) for _ in range(SG)]
    blue = [-int(input()) for _ in range(SB)]
    
    heapq.heapify(green)
    heapq.heapify(blue)
    
    while green and blue:
        g_fighters = []
        b_fighters = []
        
        for _ in range(min(B, len(green), len(blue))):
            g_fighters.append(heapq.heappop(green))
            b_fighters.append(heapq.heappop(blue))
        
        # Simulamos cada batalla
        for g, b in zip(g_fighters, b_fighters):
            diff = g - b 
            if diff < 0:       
                heapq.heappush(green, diff)
            elif diff > 0:     
                heapq.heappush(blue, diff)
            # Si diff == 0, ambos mueren, no pusheamos nada
    
    if not green and not blue:
        print("green and blue died")
    elif green:
        print("green wins")
        while green:
            print(-heapq.heappop(green))
    else:
        print("blue wins")
        while blue:
            print(-heapq.heappop(blue))

T = int(input())
for i in range(T):
    if i > 0:
        print()
    solve()