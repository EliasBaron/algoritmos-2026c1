import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

M = {}
dice = []

def dp(n):
    if n == 0:
      return 0
    
    else for _ in 