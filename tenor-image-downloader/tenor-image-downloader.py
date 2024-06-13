#! python3
# tenor-image-downloader - Download GIF images on Tenor website
# Usage: tenor-image-downloader (search-text) (foldername) (num_of_images)


import os
import sys
import requests
import bs4

try:
    search = str(sys.argv[1])
    folder = str(sys.argv[2])
    num_of_images = int(sys.argv[3])
except IndexError:
    print("Usage: tenor-image-downloader (search-text) (foldername) (num_of_images)")
    sys.exit()


url = 'https://tenor.com/search/' + search
os.makedirs(folder, exist_ok=True)

res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, features='html.parser')
images = soup.select('.Gif img', limit=num_of_images)

print(f'Downloading {num_of_images} images of {search}')

for i, image in enumerate(images):
    image_link = image.get('src')

    if image_link.startswith('/assets'):
        print(f'{i+1} - Can\'t download image')
        continue

    print(f'{i+1} - {image_link}')

    res = requests.get(image_link)
    res.raise_for_status()

    image_name = os.path.basename(image_link) + str(i)

    download_image = open(os.path.join(folder, image_name), 'wb')
    for chunk in res.iter_content(100000):
        download_image.write(chunk)
    download_image.close()

print('Done!')
