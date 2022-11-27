from enum import Enum

class DataProvider:  

    def _init_(self):
        self.SourceWebSite = Enum(
            'SourceWebSite', 
            [
                'FBEF',
                'FOOTBALLIA',
                'MATCHENDIRECT',
                'WIKIPEDIA',
                'LEQUIPE'
            ]
        )

    def getLink(self, link):
        pass

    def integrateData(website) -> None: #website : enum
        pass
    