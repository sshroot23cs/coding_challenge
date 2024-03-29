import pytest


class TestGoogleFinance:

    @pytest.mark.smoke
    def test_search_stock(self, browser, get_pages_object):
        get_pages_object.home.check_search_element()
        get_pages_object.home.enter_stock_to_search("Keysight Technologies Inc")
        assert "Keysight Technologies Inc" in browser.title, "Title is not matching"

    def test_google_login(self, browser, get_pages_object):
        get_pages_object.home.check_search_element()
        assert "Google Finance - Stock Market Prices" in browser.title, "Title is not matching"

    def test_compare_markets_navigation(self, browser, get_pages_object):
        get_pages_object.home.check_search_element()
        assert "Google Finance - Stock Market Prices" in browser.title, "Title is not matching"

    @pytest.mark.smoke
    def test_market_trends_navigation(self, browser, get_pages_object):
        get_pages_object.home.navigate_to_most_active_page(page_title="Most Active Stocks - Google Finance")
        assert "Most Active Stocks - Google Finance" in browser.title, "Title is not matching"
        assert "Explore market trends\nShare" in get_pages_object.market_page.get_header_text()

    def test_new_watchlist(self, browser, get_pages_object):
        get_pages_object.search.check_search_element()
        assert "Google Finance - Stock Market Prices" in browser.title, "Title is not matching"

    def test_new_portfolio(self, browser, get_pages_object):
        get_pages_object.search.check_search_element()
        # assert "Google Finance - Stock Market Prices, "Title is not matching"

    def test_key_events(self, browser, get_pages_object):
        get_pages_object.search.check_search_element()
        # assert "Google Finance - Stock Market Prices, "Title is not matching"

    def test_most_followed_on_google(self, browser, get_pages_object):
        get_pages_object.search.check_search_element()
        # assert "Google Finance - Stock Market Prices, "Title is not matching"

    def test_earning_calendar(self, browser, get_pages_object):
        get_pages_object.search.check_search_element()
        # assert "Google Finance - Stock Market Prices, "Title is not matching"

    def test_financial_news_navigation(self, browser, get_pages_object):
        get_pages_object.search.check_search_element()
        # assert "Google Finance - Stock Market Prices, "Title is not matching"
