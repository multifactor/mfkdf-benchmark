import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.ticker import ScalarFormatter

file = open('results.txt', 'r')
lines = file.readlines()

factors = ["key", "password", "hotp", "uuid"]
labels = ["Key", "Password", "HOTP", "UUID"]
N = len(factors)

setup2 = [ [] for i in range(N) ]
derive2 = [ [] for i in range(N) ]
setup3 = [ [] for i in range(N) ]
derive3 = [ [] for i in range(N) ]

setup2m = []
derive2m = []
setup3m = []
derive3m = []

for line in lines:
    words = line.split(" ")
    if (words[0] == "mfkdf_2_3"):
        if (words[2] == "setup"):
            if (words[3] == "key"):
                setup2[0].append(float(words[4]))
            elif (words[3] == "factor"):
                index = factors.index(words[4])
                setup2[index].append(float(words[5]))
            elif (words[3] == "full"):
                setup2m.append(float(words[4]))
        elif (words[2] == "derive"):
            if (words[3] == "key"):
                derive2[0].append(float(words[4]))
            elif (words[3] == "factor"):
                index = factors.index(words[4])
                derive2[index].append(float(words[5]))
            elif (words[3] == "full"):
                derive2m.append(float(words[4]))
    elif (words[0] == "mfkdf_3"):
        if (words[2] == "setup"):
            if (words[3] == "key"):
                setup3[0].append(float(words[4]))
            elif (words[3] == "factor"):
                index = factors.index(words[4])
                setup3[index].append(float(words[5]))
            elif (words[3] == "full"):
                setup3m.append(float(words[4]))
        elif (words[2] == "derive"):
            if (words[3] == "key"):
                derive3[0].append(float(words[4]))
            elif (words[3] == "factor"):
                index = factors.index(words[4])
                derive3[index].append(float(words[5]))
            elif (words[3] == "full"):
                derive3m.append(float(words[4]))

derive2[3] = [0] * 100

for i in range(N):
    setup3[i] = np.mean(setup3[i])
    derive3[i] = np.mean(derive3[i])
    setup2[i] = np.mean(setup2[i])
    derive2[i] = np.mean(derive2[i])

data = np.array([setup3, derive3, setup2, derive2])

fig, ax = plt.subplots()

ax.bar([0.8,1.2,1.8,2.2], data[:,3], width=0.3, label=labels[3], bottom=np.add(np.add(data[:,0],data[:,1]),data[:,2]), color='pink')
ax.bar([0.8,1.2,1.8,2.2], data[:,2], width=0.3, hatch='\\\\', alpha=0.99, label=labels[2], bottom=np.add(data[:,0],data[:,1]), color='green')
ax.bar([0.8,1.2,1.8,2.2], data[:,1], width=0.3, label=labels[1], bottom=data[:,0], color='orange')
ax.bar([0.8,1.2,1.8,2.2], data[:,0], width=0.3, hatch='//', alpha=0.99, label=labels[0], color='blue')
# ax.axes.get_xaxis().set_visible(False)
ax.axes.get_xaxis().set_ticks([0.8,1.2,1.8,2.2])
plt.gca().set_xticklabels(["Setup", "Derive", "Setup", "Derive"], fontsize=12)

print(np.mean(setup3m))
print(np.mean(derive3m))
print(np.mean(setup2m))
print(np.mean(derive2m))

plt.xlim(0.5, 2.5)
plt.ylabel('Computation Time (ms)', fontsize=12)
plt.xlabel('3-of-3 MFKDF                          2-of-3 MFKDF', fontsize=12)

plt.legend(loc='upper left')
plt.savefig('mfkdf.pdf', bbox_inches='tight')
