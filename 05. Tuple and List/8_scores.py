scores = []
print('Enter the scores for the test. Use -1 if you want to finish')
score = float(input('score: '))
while score != -1:
    scores.append(score)
    score = float(input('score: '))

scores.sort()
print('The scores (ordered): ', scores)
print('The average of these', len(scores), 'scores =', sum(scores)/len(scores))
