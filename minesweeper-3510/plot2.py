import matplotlib.pyplot as plt
from collections import defaultdict
from data2 import trials
x = []
y = []
allValues = defaultdict(list)
for trial in trials:
  key = trial[1]/trial[0]*100
  allValues[key].extend([trial[3]])

for key in allValues.keys():
  avg = 0
  totalSum = 0
  cnt = 0
  for val in allValues[key]:
    totalSum += val
    cnt += 1
  avg = totalSum / cnt
  x.append(key)
  y.append(avg)

print(x)
print(y)

plt.plot(x, y)
plt.ylabel('Runtime (in seconds)')
plt.xlabel('Bomb Density (%)')
plt.title('Algorithm B: Runtime vs Bomb Density')
plt.show()