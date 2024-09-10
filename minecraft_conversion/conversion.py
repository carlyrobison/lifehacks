import pandas as pd
import imageio.v2 as imageio
import numpy as np

img_location = "~/Documents/minecraft/worldmapflattened3.bmp"

img = (imageio.imread(img_location, pilmode = 'RGB'))
data = np.array(img)
unique_colors = []

for i in data:
    for j in i:
        # print(j)
        if tuple(j.tolist()) not in unique_colors:
            unique_colors.append(tuple(j.tolist()))
print(len(unique_colors))
unique_colors.sort()
for c in unique_colors:
    print(c)

pd.DataFrame(data[:,:,0]).to_csv("image3R.csv")
pd.DataFrame(data[:,:,1]).to_csv("image3G.csv")
pd.DataFrame(data[:,:,2]).to_csv("image3B.csv")