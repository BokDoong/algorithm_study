import sys

# Main
E, S, M = map(int, sys.stdin.readline().split())
year = 1
while(True):
  if (year-E)%15 == 0 and (year-S)%28 == 0 and (year-M)%19 == 0:
    break
  
  year += 1
  
print(year)