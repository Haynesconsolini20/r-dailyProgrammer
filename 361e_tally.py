# a:1, b:1, c:1, d:1, e:1
# b:2, d:2, a:1, c:0, e:-2
# Sorted highest to lowest

#dbbaCEDbdAacCEAadcB
#EbAAdbBEaBaaBBdAccbeebaec - challenge input
challengeInput = "dbbaCEDbdAacCEAadcB"

answer = []
while len(challengeInput) > 0:
  points = challengeInput.count(challengeInput[0].lower()) - challengeInput.count(challengeInput[0].upper())
  answer.append((challengeInput[0].lower(), points))
  toRemove = challengeInput[0]
  challengeInput = challengeInput.replace(toRemove.lower(), "")
  challengeInput = challengeInput.replace(toRemove.upper(), "")
  
answer.sort(key=lambda score: score[1], reverse=True)

first = True
for score in answer:
  if first:
    first = False
    pass
  else:
    print(", ", end='')
  print(f'{score[0]}:{score[1]}', end='')
