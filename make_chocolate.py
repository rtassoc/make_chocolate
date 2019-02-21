def make_chocolate(small, big, goal):
  maxBig = goal / 5

  if big >= maxBig:
    if small >= (goal - maxBig * 5):
      return goal - maxBig * 5
  if big < maxBig:
    if small >= (goal - big * 5):
      return goal - big * 5
  return -1


print(make_chocolate(4, 1, 9))  # → 4
print(make_chocolate(4, 1, 10))  # → -1
print(make_chocolate(4, 1, 7))  # → 2
