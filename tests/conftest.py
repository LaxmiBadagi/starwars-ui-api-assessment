import pytest
import pytest_html

from utils.screenshot_helper import take_screenshot

# Attach screenshot on failure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver:
            screenshot_path = take_screenshot(driver, item.name)
            if screenshot_path:
                # Attach to HTML report
                extra = getattr(rep, "extra", [])
                extra.append(pytest_html.extras.image(screenshot_path))
                rep.extra = extra