import pandas as pd
import imageio
import numpy as np

img_location = "REDACTED.bmp"

img = (imageio.imread(img_location, pilmode = 'RGB'))
data = np.array(img)

for i in data:
    print(i)

pd.DataFrame(data[:,:,0]).to_csv("image0R.csv")
pd.DataFrame(data[:,:,1]).to_csv("image0G.csv")
pd.DataFrame(data[:,:,2]).to_csv("image0B.csv")