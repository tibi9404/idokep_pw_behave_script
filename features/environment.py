import glob
import os
from playwright.sync_api import Page, expect, sync_playwright

def before_all(context):
    delete_all_previously_generated_files("output_files/")
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=False)

def after_all(context):
    context.browser.close()
    context.playwright.stop()

def before_scenario(context, scenario):
    context.page = context.browser.new_page()

def after_scenario(context, scenario):
    context.page.close()

def delete_all_previously_generated_files(folder_path):
    files = glob.glob(os.path.join(folder_path, '*'))

    for file in files:
        try:
            os.remove(file)
        except Exception as e:
            print(f"Error deleting {file}: {e}")