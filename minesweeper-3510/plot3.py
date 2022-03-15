import matplotlib.pyplot as plt
from collections import defaultdict
from data import trials
x = []
y = []
allValues = defaultdict(list)
for trial in trials:
  key = trial[0]
  allValues[key].extend([trial[2]/trial[0]])

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
plt.ylabel('Tiles Opened / Total Tiles (%)')
plt.xlabel('Grid Area (with constant bomb density)')
plt.title('Algorithm B: Tiles Opened vs Grid Area')
plt.show()