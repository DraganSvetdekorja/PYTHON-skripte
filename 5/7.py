import os
import tinify
import pandas as pd
tinify.key = "xxxxxxxxxxxxxxxxxxxxxxxxxxx"


images = os.listdir('posts')

df = pd.DataFrame(columns = ['image', 'size_before', 'size_after', 'saving'])

for image in images:
        
    source = tinify.from_file("posts/" + image)
    resized = source.resize(method="scale", width=1000)
    resized.to_file("compressed/" + image)
    size_before = os.path.getsize("posts/" + image)
    size_after = os.path.getsize("compressed/" + image)
    
    row = {
        'image': image,
        'size_before': size_before,
        'size_after': size_after,
        'saving': size_before - size_after
    }
    
    df = df.append(row, ignore_index=True)