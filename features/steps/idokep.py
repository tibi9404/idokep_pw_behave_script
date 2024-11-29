import re
import sys
from behave import step
from playwright.sync_api import Page, expect, sync_playwright
from requests import request
import requests

idokep_base_uri = "https://www.idokep.hu/"
output_files_dir = "output_files/"
what_to_wear = 0
rain_is_expected = False


@step('I navigate to the site')
def step_open_site(context):
    context.page.goto(idokep_base_uri)
    context.page.wait_for_load_state('networkidle')

@step('I accept the open dialog')
def step_accept_open_dialog(context):
    acceptButton = context.page.locator('button', has_text='ELFOGADOM')
    if acceptButton.is_visible():
        acceptButton.click()

@step('Query what to wear today')
def step_query_what_to_wear(context):
    global what_to_wear 
    what_to_wear = context.page.locator('.what-to-wear').text_content()

@step('Write the value to a txt')
def step_write_to_txt(context):
    with open(output_files_dir + "whatToWear.txt", "a", encoding="utf-8") as f: 
        f.write("Az ajánlott viselet: " + what_to_wear) 
        f.write("\n")
    
@step('Query if rain is expected in the next four days')
def step_expected_rain(context):
    daily_columns = context.page.locator('.dailyForecastCol')
    for i in range(4):
        if daily_columns.nth(i).locator('.rainlevel-container').is_visible():
            global rain_is_expected
            rain_is_expected = True


@step('Write the value to a csv')
def step_write_to_csv(context):
    f = open(output_files_dir + "isRanExpected.csv", "a", encoding="utf-8")
    if rain_is_expected:
        f.write("Yes, rain can be expected in the next four days.") 
        f.write("\n")
    else:
        f.write("No,rain cannot be expected in the next four days") 
        f.write("\n")

@step('I navigate to temp map')
def step_nav_to_temp_map(context):
    context.page.locator('#menubarDesktop a', has_text='Hőtérkép').click()
    expect(context.page.locator('#hatter')).to_be_visible()

@step('the temp map can be saved')
def step_save_temp_map(context):
    img_locator = context.page.locator('#hatter')
    img_src = img_locator.get_attribute('src')

    if img_src:
        save_image(img_src, "downloaded_temp_map.jpg")
    else:
        print("Image source not found.")

@step('I navigate to the past rain map')
def step_nav_to_temp_map(context):
    context.page.locator('#menubarDesktop a', has_text='Felhőkép').nth(0).hover()
    context.page.locator('a', has_text='Régi felhőkép').click()
    expect(context.page.locator("img[alt='Felhőkép']")).to_be_visible()

@step('the past rain map can be saved')
def step_save_temp_map(context):
    img_locator = context.page.locator("img[alt='Felhőkép']")
    img_src = img_locator.get_attribute('src')

    if img_src:
        save_image(img_src, "downloaded_past_rain_map.jpg")
    else:
        print("Image source not found.")

def save_image(img_src, file_name):
    response = requests.get(idokep_base_uri + img_src)
    if response.status_code == 200:
        with open(output_files_dir + file_name, "wb") as file:
            file.write(response.content)
            print("Image saved successfully.")
    else:
        print("Downloading image failed.")