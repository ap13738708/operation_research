import knapsackDP as knapsackDP

reload(knapsackDP)
final = knapsackDP.knapsackDP(8, [3, 8, 5], [4, 6, 5])
print 'objective value: ', final.f
print 'combinations are: ', final.result

final = knapsackDP.knapsackDP(4, [2, 3, 1], [31, 47, 14])
print 'objective value: ', final.f
print 'combinations are: ', final.result

