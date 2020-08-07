import pandas as pd
from PIL import Image
import pytesseract

# Construct the dataframe because I don't have the input file
df = pd.DataFrame({'Filename': ['Test1001.jpg', 'Test1012.jpg', 'Test1022.jpg', 'Test1071.jpg', 'Test1122.jpg'],
                   'Category': [10, 5, 3, 4, 6]})


def text(img):
    img = Image.open(img)
    text_local = pytesseract.image_to_string(img)
    return text_local


# Iterate over the dataframe and apply the function text to each filename
for x in df.Filename:
    print(text(x))
