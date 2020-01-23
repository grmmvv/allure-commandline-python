import subprocess

from src.cache_manager import CacheManager
from src.install_manager import InstallManager


class AllureCLI:
    def __init__(self):
        cache_manager = CacheManager()
        install_manager = InstallManager
        if not cache_manager.has_cached_version:
            self.allure_bin = install_manager.install_allure_cli()
        elif cache_manager.has_new_version:
            installed_version = cache_manager.last_cached_version
            self.allure_bin = install_manager.install_allure_cli()
            install_manager.uninstall_allure_cli(installed_version)
        else:
            self.allure_bin = cache_manager.get_cached_binary()

    def generate(self, results_dir='allure-results', report_dir='allure-report', clean=False):
        cmd = f'{self.allure_bin} generate {results_dir} -o {report_dir}'
        if clean:
            cmd += ' -c'
        subprocess.run(cmd, shell=True, universal_newlines=True, check=True)
