import pandas as pd
import matplotlib.pyplot as plt

from pysankey import sankey


# --- First example with fruits.txt ---

df1 = pd.read_csv(
    'pysankey/tests/fruits.txt', sep=' ', names=['true', 'predicted']
)
colorDict = {
    'apple':'#f71b1b',
    'blueberry':'#1b7ef7',
    'banana':'#f3f71b',
    'lime':'#12e23f',
    'orange':'#f78c1b',
    'kiwi':'#9BD937'
}

ax1 = sankey(
    df1['true'], df1['predicted'], aspect=20, colorDict=colorDict,
    leftLabels=['banana','orange','blueberry','apple','lime'],
    rightLabels=['orange','banana','blueberry','apple','lime','kiwi'],
    fontsize=12
)

plt.show() # to display
# plt.savefig('fruit.png', bbox_inches='tight') # uncomment to save


# --- Second example with weight in customers-goods.csv ---

df2 = pd.read_csv(
    'pysankey/tests/customers-goods.csv', sep=',',
    names=['id', 'customer', 'good', 'revenue']
)
weight = df2['revenue'].values[1:].astype(float)

ax2 = sankey(
      left=df2['customer'].values[1:], right=df2['good'].values[1:],
      rightWeight=weight, leftWeight=weight, aspect=20, fontsize=20
)

plt.show() # to display
# plt.savefig('customers-goods.png', bbox_inches='tight') # uncomment to save


# --- Last example passing a matplotlib Axes to sankey()---

ax3 = plt.axes()

ax3 = sankey(
      df1['true'], df1['predicted'], aspect=20, colorDict=colorDict,
      fontsize=12, ax=ax3
)

plt.show()
