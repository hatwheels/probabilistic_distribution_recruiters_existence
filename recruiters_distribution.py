import sys
import itertools as it
import matplotlib.pyplot as plt
from collections import OrderedDict

if __name__ == "__main__":
        if not sys.argv[1].isdecimal():
                print("Pass a number")
        else:
                n = int(sys.argv[1])
                array = { i:[-1, 0, 2, 3] for i in range(1, n + 1) }
                greater = 0

                sum_of_combinations = 4**n
                combinations = it.product(*(array[index] for index in array))
                dataset = {}

                for item in list(combinations):
                        result = sum(i for i in item)
                        if result in dataset:
                                dataset[result] += 1
                        else:
                                dataset[result] = 1
                        if result >= 0:
                                greater += 1

                sorted_dataset = sorted(dataset.items())
                x = [k + n for k, v in sorted_dataset]
                y = [v / sum_of_combinations for k, v in sorted_dataset]


                p_not_falling = round((greater / sum_of_combinations) * 100, 2)
                p_falling =  round(100 - p_not_falling, 2)

                # Plot Probabilistic Distribution
                fig, a = plt.subplots()
                a.scatter(x, y)
                a.axvline(x=n, color='red')
                a.text(0.05, 0.95, 'P(n[t+1] >= n[t]) = ' + str(p_not_falling) + '%\n' + 'P(n[t+1] < n[t]) = ' + str(p_falling) + '%\n' + 'n = ' + str(n), transform=a.transAxes, fontsize=14, verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
                plt.title('Probability Distribution of the new number of recruiters (end of day t)')
                plt.xlabel('Number of Recruiters')
                plt.ylabel('Probability')
                plt.show()
