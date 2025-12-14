from time import perf_counter
from pathlib import Path

import matplotlib.pyplot as plt
import algorithms as algo

def make_arrays(size, ratio):
    arr1 = [2 * i * ratio + 1 for i in range(size)]
    arr2 = [2 * i for i in range(size * ratio)]
    
    return arr1, arr2

def total_time(fn, *args, repeats=10):
    start = perf_counter()
    
    for _ in range(repeats):
        fn(*args)
    
    return perf_counter() - start

def save_bench_plots(ratios, repeats=10, start=100, stop=1000, step=50):
    output_path = Path("plots")
    output_path.mkdir(parents=True, exist_ok=True)

    methods = {
        "two_pointers": algo.two_pointers,
        "binary_search": algo.binary_search_method,
        "exponential": algo.exponential_method,
        "binary_division": algo.binary_division_method,
    }

    for ratio in ratios:
        sizes = []
        timings = {name: [] for name in methods}

        for size in range(start, stop, step):
            arr1, arr2 = make_arrays(size, ratio)
            sizes.append(size)

            for name, fn in methods.items():
                if name == "binary_division":
                    run = total_time(
                        fn,
                        arr1, arr2,
                        0, len(arr1) - 1,
                        0, len(arr2) - 1,
                        repeats=repeats,
                    )
                else:
                    run = total_time(fn, arr1, arr2, repeats=repeats)

                timings[name].append(run)

        fig, ax = plt.subplots()

        ax.set_title(f"Отношение длин={ratio}; Повторений={repeats}")
        ax.set_xlabel("Длина меньшего")
        ax.set_ylabel("Время")

        ax.set_yscale("log")
        ax.set_xscale("log")

        ax.grid(True, which="both", linestyle="--", linewidth=0.7, alpha=0.6)

        for name, _ in methods.items():
            ax.plot(sizes, timings[name], label=name)

        ax.legend()
        fig.tight_layout()

        file_name = f"bench_ratio_{ratio}_rep_{repeats}.png"
        fig.savefig(output_path / file_name, dpi=200)
        plt.close(fig)

if __name__ == "__main__":
    ratio_values = [1, 10, 100, 1000]
    save_bench_plots(ratio_values, repeats=50)
