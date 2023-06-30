from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time
import boto3

def search_for_items(browser, search_term):
    """search for key words at front page"""
    browser.get("https://images.google.com/")
    time.sleep(2)
    search_box = browser.switch_to.active_element
    search_box.click()
    time.sleep(1)
    search_box.send_keys(search_term)
    time.sleep(1)
    search_box.send_keys('\n')

def find_images(browser):
    """Return image objects"""
    time.sleep(5)
    images = browser.find_elements(By.CSS_SELECTOR, "a.wXeWr.islib.nfEiy div.bRMDJf.islir img")
    return images

def scrape_image_upload(image, search_term, i):
    _ = image.location_once_scrolled_into_view
    image_url = image.get_attribute('src')
    photo_browser.get(image_url)
    image = photo_browser.find_element(By.CSS_SELECTOR, "img")
    image_png = image.screenshot_as_png
    label = "_".join(search_term.split())
    file_name=f'image_{label}_{i}.png'
    print(file_name)
    with open(file_name, 'wb') as f:
        f.write(image_png)
    #remote_pathname="cap_stone/{}/{}_{}.png".format(label,label,i)
    file_name=f'image_{label}_{i}.png'
    #save_to_s3(remote_pathname,file_name)

def scrape_images(images, search_term, photo_browser):
    for i, image in enumerate(images):
        time.sleep(1)
        scrape_image_upload(image, search_term, i)

#def save_to_s3(remote_pathname,file_name):
    #s3.upload_file(
    #Bucket="bucket-for-misaki-cho",
    #Filename=file_name,
    #Key=remote_pathname)


def search_scrape_save(search_terms):
    for search_term in search_terms:
        search_for_items(browser, search_term)
        print("Search complete")
        images = find_images(browser)
        print("Images found" + str(images))
        scrape_images(images, search_term, photo_browser)

if __name__=="__main__":
    browser = Chrome()
    photo_browser = Chrome()
    #s3 = boto3.client("s3")
    search_terms=["interior design cabin look", "interior log cabin"]
    search_scrape_save(search_terms)
