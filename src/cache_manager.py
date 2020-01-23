import os

from pkg_resources import parse_version

from src.install_manager import InstallManager
from src.vars import RELEASE_FILE, CACHE_DIR


class CacheManager:
    @property
    def has_cached_version(self):
        try:
            with open(RELEASE_FILE):
                return True
        except FileNotFoundError:
            return False

    @property
    def last_cached_version(self):
        if self.has_cached_version:
            with open(RELEASE_FILE) as src:
                return src.read()

    @property
    def has_new_version(self):
        if parse_version(self.last_cached_version) < parse_version(InstallManager().get_latest_version()):
            return True
        return False

    def get_cached_binary(self):
        return os.path.join(CACHE_DIR, f'allure-{self.last_cached_version}', 'bin', 'allure')
