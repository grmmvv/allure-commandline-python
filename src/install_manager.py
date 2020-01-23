import os
import shutil
import tarfile
import tempfile
from urllib.parse import urljoin
from xml.etree import ElementTree as ET

import requests

from src.vars import REPO_URL, RELEASE_FILE, CACHE_DIR


class InstallManager:
    @staticmethod
    def get_latest_version():
        url = urljoin(REPO_URL, 'maven-metadata.xml')
        root = ET.fromstring(requests.get(url).content)
        version = root.findall('./versioning/latest')[-1]
        return version.text

    @staticmethod
    def write_downloaded_version(version: str):
        with open(RELEASE_FILE, 'w') as dst:
            dst.write(version)

    @staticmethod
    def install_allure_cli(version='latest'):
        if version == 'latest':
            version = InstallManager.get_latest_version()
        url = urljoin(REPO_URL, f'{version}/allure-commandline-{version}.tgz')
        response = requests.get(url, stream=True)
        with tempfile.NamedTemporaryFile() as dst:
            for chunk in response:
                dst.write(chunk)
            dst.seek(0)
            tar = tarfile.open(dst.name)
            tar.extractall(CACHE_DIR)
            InstallManager.write_downloaded_version(version)
            allure_bin = os.path.join(CACHE_DIR, f'allure-{version}', 'bin', 'allure')
            return allure_bin

    @staticmethod
    def uninstall_allure_cli(version):
        shutil.rmtree(os.path.join(CACHE_DIR, f'allure-{version}'))
