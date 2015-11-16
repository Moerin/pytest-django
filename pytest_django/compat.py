import pytest

from django.conf import settings
from django.test.utils import get_runner

""" In case of specifity added in django.settings the "getrunner" method
    is used to fetch a customized test runner
"""

DjangoTestRunner = get_runner(settings)

_runner = DjangoTestRunner(verbosity=pytest.config.option.verbose,
                           interactive=False)

setup_databases = _runner.setup_databases

teardown_databases = _runner.teardown_databases

setup_test_environment = _runner.setup_test_environment
teardown_test_environment = _runner.teardown_test_environment

del _runner
