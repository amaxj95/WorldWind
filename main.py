from PIL import Image, ImageDraw, ImageFont
import requests
import streamlit as st
import re

st.title("NASA Astronomy Picture of the Day")

nasa_api_key = "x7XKtOatslz6OF7IBTYIhrFSptSJ31krNgHBYfhE"

url = "https://api.nasa.gov/planetary/apod?" \
      f"api_key={nasa_api_key}"

# Get the request data as a dictionary
response1 = requests.get(url)
data = response1.json()

# Extract the image title, url and, explanation
title = data["title"]
image_url = data["url"]
explanation = data["explanation"]

# Download the image
image_filepath = "img.png"
response2 = requests.get(image_url)
with open(image_filepath, 'wb') as file:
    file.write(response2.content)

# Download the image
image = Image.open(requests.get(image_url, stream=True).raw)

st.title(title)
st.image(image_url)
st.write(explanation)
# Add a line that links to a Twitter profile
st.write("For more updates, follow [@junk_ez_eth](https://twitter.com/junk_ez_eth)")
