import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.ticker import ScalarFormatter

file = open('results.txt', 'r')
lines = file.readlines()

factors = ["uuid", "hmacsha1", "question", "password", "hotp", "ooba", "totp"]
labels = ["UUID", "HMAC-SHA1\n(YubiKey)", "Security\nQuestion", "Password", "HOTP", "OOBA", "TOTP"]
N = len(factors)
setup = [ [] for i in range(N) ]
derive = [ [] for i in range(N) ]

for line in lines:
    words = line.split(" ")
    if (words[0] == "mfkdf_all"):
        if (words[3] == "factor"):
            index = factors.index(words[4])
            if (words[2] == "setup"):
                setup[index].append(float(words[5]))
            elif (words[2] == "derive"):
                derive[index].append(float(words[5]))

fig, axes = plt.subplots(nrows=N, sharex=True)
fig.subplots_adjust(hspace=0)

for i in range(N):
    box = axes[i].boxplot([setup[i], derive[i]], showfliers=False, widths = 0.8, vert=False)
    box['boxes'][0].set_color('orange')
    box['medians'][0].set_color('orange')
    box['caps'][0].set_color('orange')
    box['caps'][1].set_color('orange')
    box['whiskers'][0].set_color('orange')
    box['whiskers'][1].set_color('orange')
    box['boxes'][1].set_color('blue')
    box['medians'][1].set_color('blue')
    box['caps'][2].set_color('blue')
    box['caps'][3].set_color('blue')
    box['whiskers'][2].set_color('blue')
    box['whiskers'][3].set_color('blue')
    axes[i].set_ylabel(labels[i], rotation=0, ha='right', va='center', fontsize=12)
    axes[i].set(yticks=[])
    axes[i].set(ylim=(0.25,2.75))
    axes[i].invert_yaxis()

    smean = np.mean(setup[i]);
    if (smean < 1): smean = str(round(smean*1000, 1)) + ' µs';
    else: smean = str(round(smean, 2)) + ' ms';

    dmean = np.mean(derive[i]);
    if (dmean < 1): dmean = str(round(dmean*1000, 1)) + ' µs';
    else: dmean = str(round(dmean, 2)) + ' ms';

    offset = 0.15
    if (i < 5):
        x, y = box['caps'][1].get_xydata()[1]
        axes[i].annotate('   x̄ = ' + smean, xy=(x, y+offset), ha='left', va='bottom', fontsize=10)
        x, y = box['caps'][3].get_xydata()[1]
        axes[i].annotate('   x̄ = ' + dmean, xy=(x, y+offset), ha='left', va='bottom', fontsize=10)
    else:
        x, y = box['caps'][0].get_xydata()[1]
        axes[i].annotate('x̄ = ' + smean + '   ', xy=(x, y+offset), ha='right', va='bottom', fontsize=10)
        x, y = box['caps'][2].get_xydata()[1]
        axes[i].annotate('x̄ = ' + dmean + '   ', xy=(x, y+offset), ha='right', va='bottom', fontsize=10)

    if (i != 0):
        axes[i].spines['top'].set_visible(False)
    if (i != N-1):
        axes[i].get_xaxis().set_visible(False)
        axes[i].spines['bottom'].set_visible(False)

plt.xscale('log')
lines = [Line2D([0], [0], color='orange', lw=4), Line2D([0], [0], color='blue', lw=4)]
axes[0].legend(lines, ['Setup', 'Derive'], loc='upper right')
axes[0].set_zorder(100)

ticks = ['', '', '10 µs', '100 µs', '1 ms', '10 ms']
plt.gca().set_xticklabels(ticks, fontsize=12)
# fig.suptitle('Setup & Derivation Time for MFKDF Factors')
plt.savefig('factors_h.pdf', bbox_inches='tight')
