import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def our_browser():
    current_file = os.path.abspath(__file__)
    project_root_dir = os.path.dirname(current_file)
    if not os.path.exists('tmp'):
        os.mkdir('tmp')

    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": os.path.join(project_root_dir, 'tmp'),
        "download.prompt_for_download": False
    }
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield driver
    os.rmdir(os.path.join(project_root_dir, 'tmp'))