import requests
from bs4 import BeautifulSoup

def get_html_content(url):
    """
    Retrieve the HTML content of a website.

    Args:
    - url (str): The URL of the website.

    Returns:
    - str: The HTML content of the website.
    """
    try:
        response = requests.get(url)
        html_content = response.text
        return html_content
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None

def hotdog(word):
    if word.lower() == "hotdog":
        return True
    else:
        return False


def check_website_status(url):
    """
    Check the status code of a website.

    Args:
    - url (str): The URL of the website to check.

    Returns:
    - int: The status code of the website.
    """
    try:
        response = requests.get(url)
        return response.status_code
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None


