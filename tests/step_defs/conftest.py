import pytest
from pytest_bdd import given
from selenium.webdriver import Chrome
from termcolor import colored
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()

# Fixtures


@pytest.fixture
def browser():
    '''Provides browser instance'''
    browser = Chrome()
    browser.implicitly_wait(10)
    yield browser
    browser.quit()

# Hooks


def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    '''Called when step function failed to execute'''
    print(colored(f'STEP FAILED: {step}', 'red'))


def pytest_bdd_after_step(request, feature, scenario, step, step_func, step_func_args):
    '''Called after step function is successfully executed'''
    print(colored(f'STEP : {step}', 'green'))
