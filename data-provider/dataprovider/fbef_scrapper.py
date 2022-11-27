from data_provider_base_class_interface import DataProviderBaseInterface
from source_web_site_enum import SourceWebSite
from bs4 import BeautifulSoup
import requests
from datetime import datetime, timedelta

class FbefScrapper(DataProviderBaseInterface):
    def __init__(self) -> None:
        super().__init__(SourceWebSite.FBREF) #create soup in bases class constructor

    def scrap(self):

        def getNextDate(currentDate: str) -> str:
            date = datetime.strptime(currentDate, "%Y-%m-%d")
            date = date + timedelta(days=1)
            return date.strftime("%Y-%m-%d")
    
        currentDate = "1888-01-01"

        while True:
            print(f'currentDate : {currentDate}')
            self.baseUrl += currentDate
            req = requests.get(self.baseUrl)
            soup = BeautifulSoup(req.content, 'html.parser')
            tables = soup.find_all('div', {"class": "table_wrapper tabbed"})
            currentDate = getNextDate(currentDate)
        # print(tables[0].prettify())



temp = FbefScrapper()
temp.scrap()