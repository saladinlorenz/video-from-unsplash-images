import os
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import moviemake



site="https://unsplash.com/s/photos/"


# Third Section: Build the main function
saved_folder = 'images'

def main():
    if not os.path.exists(saved_folder):
        os.mkdir(saved_folder)
    download_images()


# Fourth Section: Build the download function
def download_images():



    data = input('What are you looking for? ')
    saved_folder = 'images'+'/'+data
    n_images = int(input('How many images do you want? '))
    quality=str(input('choose the quality :\n - s for small\n - m for medium\n - l for large\n'))
    if quality=="s" :
        quality="&amp;w=640"
    elif quality=="m":
        quality="&amp;w=1920"
    elif quality=="l":
        quality="&amp;w=2400"
    else:
        quality="&amp;w=640"
    print('searching...')

    search_url = site + data +'?orientation=portrait'


    options = webdriver.ChromeOptions()
    userAgent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.56 Safari/537.36"
    options.add_argument(f'user-agent={userAgent}')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument('--headless')
    driver = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=options)
    driver.maximize_window()

    driver.get(search_url)
    time.sleep(1)

    driver.execute_script("window.scrollBy(0,2800)")
    time.sleep(1)
    try:
        driver.find_element_by_xpath('//button[contains(text(), "Load more photos")]').click()

        time.sleep(2)
        driver.execute_script("window.scrollBy(0,4000)")
        time.sleep(1)
        driver.execute_script("window.scrollBy(0,4000)")
        time.sleep(1)
    except :
        pass







    response = driver.page_source

    html = response

    soup = BeautifulSoup(html, 'html.parser')

    results = soup.findAll('a', href=True)

    count = 1
    links = []
    for result in results:

        try:
            if "https://unsplash.com/photos/" in result['href']:


                links.append(result['href']+"&amp;w=1920")

                count += 1
                if(count > n_images):
                    break

        except KeyError:
            continue

    print(f"Downloading {len(links)} images...")

    if not os.path.exists(saved_folder):
        os.mkdir(saved_folder)
    for i, link in enumerate(links):
        response = requests.get(link)

        image_name = saved_folder + '/' + data + str(i+1) + '.png'

        with open(image_name, 'wb') as fh:
            fh.write(response.content)
    print('job done !')
    print (saved_folder)
    moviegpt.makevideo(saved_folder)








# Fifth Section: Run your code
if __name__ == "__main__":
    main()
