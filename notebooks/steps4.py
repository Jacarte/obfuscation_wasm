import matplotlib.pyplot as plt
import sys
import os


def plot(folder, initial):
    print(folder, initial)

    betas = ["0.01", "0.3", "1.1"]
    r = {
        '0.01': [],
        '0.3': [],
        '1.1': []
    }
    r_prev =  {
        '0.01': [],
        '0.3': [],
        '1.1': []
    }
    for betafolder in os.listdir(folder):
        if betafolder in betas:
            mutation_data = open(f"{folder}/{betafolder}/mutation_info.txt").read().split("\n")
            i = 0
            for l in mutation_data:
                if l:
                    cells = l.split("|")
                    reward = cells[2]
                    reward=int(reward)
                    no_detectors = 60 - reward
                    r[betafolder].append(no_detectors)
                    print(betafolder, l)
                    if not "but not moved" in l:
                        r_prev[betafolder].append((no_detectors, i))
                    i += 1

    print(r_prev)
    r2 = {}
    x  = {}
    steps = 50
    for k, vals in r.items():
        # Group in chunks of 50 elements
        chunks = [vals[0]] +  [ vals[i:i + steps][-1] for i in range(0, len(vals), steps)]
        r2[k] = chunks
        print(len(chunks))
        x[k] = [i*steps for i in range(len(chunks))]

    plt.plot(x['0.01'], r2['0.01'], '.--', label="mcmc sigma=0.01", alpha=0.3)
    plt.plot(x['0.3'], r2['0.3'], 'x--', label="mcmc sigma=0.3", alpha=0.3)
    plt.plot(x['1.1'], r2['1.1'], '*--',label="mcmc sigma=1.1", alpha=0.3)
    plt.legend()
    plt.title("046dc081")
    plt.xlabel("Iteration number")
    plt.ylabel("Number of detectors")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    folder = sys.argv[1]
    initial = int(sys.argv[2])
    plot(folder, initial)