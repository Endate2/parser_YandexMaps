from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException, MoveTargetOutOfBoundsException
from selenium.webdriver import ActionChains


class SoupContentParser(object):

    def get_name(self, soup_content):
        try:
            title_tag = soup_content.find("title")
            if title_tag:
                name = title_tag.getText()
                if "," in name:
                    name = name.split(",")[0]
                name = name.replace(" — Яндекс Карты", "").strip()
                return name
            return ""
        except Exception:
            return ""

    def get_phone(self, soup_content):
        try:
            phones = []
            for data in soup_content.find_all("div", {"class": "orgpage-phones-view__phone-number"}):
                phone = data.getText()
                phones.append(phone)
            return phones
        except Exception:
            return []

    def get_social(self, soup_content):
        try:
            socials = []
            for data in soup_content.find_all("a", {"class": "business-urls-view__link"}):
                social = data['href']
                socials.append(social)
            return socials
        except Exception:
            return []

    def get_address(self, soup_content):
        try:
            for data in soup_content.find_all("a", {"class": "business-contacts-view__address-link"}):
                address = data.getText()
            return address
        except Exception:
            return ""

    def get_website(self, soup_content):
        try:
            for data in soup_content.find_all("span", {"class": "business-urls-view__text"}):
                website = data.getText()
            return website
        except Exception:
            return ""

    def get_opening_hours(self, soup_content):
        opening_hours = []
        try:
            for data in soup_content.find_all("meta", {"itemprop": "openingHours"}):
                opening_hours.append(data.get('content'))
            return opening_hours
        except Exception:
            return ""
    def get_rating(self, soup_content):
        rating = ""
        try:
            for data in soup_content.find_all("span", {"class": "business-rating-badge-view__rating-text"}):
                rating += data.getText()
                break
            return rating
        except Exception:
            return ""
