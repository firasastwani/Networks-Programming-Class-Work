import math
import random


def EWMA(sig, alpha, init_val):

    mu =[init_val]

    for s in sig:
        val = (1 - alpha) * mu[-1] + alpha * s 
        mu.append(val)

    return mu

# make noisy signal

signal = []

for i in range(100):

    noise = (random.random() - .5) * 2
    val = 100 + noise * 10
    signal.append(val)

estimate = EWMA(signal, 0.125, 0)

#make devEstimateRTT
#|sampleRTT - estimateRTT|

dif = []

for i in range(len(signal)):

    val = abs(signal[i] - estimate[i])
    dif.append(val)

# deviation EWMA

devRTT = EWMA(dif, 0.25, 0)

if __name__ == "__main__":
    import matplotlib.pyplot as plt

    x = list(range(len(signal)))
    est_aligned = estimate[1:]
    dev_aligned = devRTT[1:]

    fig, axs = plt.subplots(2, 1, figsize=(10, 6), sharex=True)

    axs[0].plot(x, signal, label='Sample RTT', alpha=0.6)
    axs[0].plot(x, est_aligned, label='EWMA RTT (alpha=0.125)', linewidth=2)
    axs[0].set_ylabel('RTT (ms)')
    axs[0].legend()
    axs[0].set_title('RTT and EWMA Estimate')

    axs[1].plot(x, dif, label='|Sample - EWMA|', alpha=0.6)
    axs[1].plot(x, dev_aligned, label='DevRTT EWMA (alpha=0.25)', linewidth=2)
    axs[1].set_xlabel('Packet index')
    axs[1].set_ylabel('Deviation (ms)')
    axs[1].legend()

    plt.tight_layout()
    plt.show()


        



    