
from src.home_page import HomePage
from src.market_trends import MarketTrendsPage


class Pages:

    def __init__(self, driver):
        self.home = HomePage(driver)
        self.market_page = MarketTrendsPage(driver)


