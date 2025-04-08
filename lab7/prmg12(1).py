import pandas as pd
import matplotlib.pyplot as plt
df2 = pd.read_csv("4laptops.csv")

plt.boxplot(df2["Screen_size_inches"], notch = True, vert = False, showmeans = True, sym = "*", patch_artist = True, widths = 0.1)
plt.xlabel('Columns')
plt.ylabel('Price')
plt.show()

plt.boxplot(df2['Weight_kg'])
plt.xlabel('Columns')
plt.ylabel('Weight_kg')
plt.show()

import seaborn as sns
sns.boxplot(df2['Weight_kg'])
plt.show()
sns.boxplot(x = df2['Weight_kg'], y = df2['RAM'])
plt.show()