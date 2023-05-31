from matplotlib import pyplot as plt
import numpy as np
def HR_makeplot(kid, date, data, start, end, folder, id):
    plt.figure(figsize=(50,30))
    plt.title(f'{kid}, {date}', fontdict={'fontsize': 50})
    plt.plot(data['time'], data['value'], label = 'HR')
    plt.axvline(x=start, color='r', linewidth=3, label=start)
    plt.axvline(x=end, color='r', linestyle='--', linewidth=3, label=end)
    plt.axhline(y=data['value'].mean(), color='g', linewidth=1, label='AVG')
    plt.yticks(np.arange(40,170,10),fontsize=30)
    plt.grid()
    plt.legend(fontsize=40)
    plt.xticks(rotation=90)
    plt.show
    plt.savefig(f'../{folder}/{kid}_{date}_{id}.png',dpi=100, facecolor='#eeeeee',bbox_inches='tight')