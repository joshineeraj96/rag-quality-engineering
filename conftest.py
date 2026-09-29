from playwright.sync_api import sync_playwright
import pytest


@pytest.fixture
def api_request():
    with sync_playwright() as p:
        request = p.request.new_context()

        yield request

        request.dispose()
