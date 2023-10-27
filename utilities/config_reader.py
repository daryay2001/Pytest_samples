import configparser
from constants import ROOT_PATH

_abs_path = f"{ROOT_PATH}/configs/app_config.ini"
_config = configparser.RawConfigParser()
_config.read(_abs_path)


class AppConfig:
    url = _config.get("app_data", "url")
    refactor_url = _config.get("app_data", "refactor_url")
    store_page_url = _config.get("app_data", "store_page_url")
    patterns_url = _config.get("app_data", "patterns_url")
    privacy_policy_url = _config.get("app_data", "privacy_policy_url")
    browser_id = _config.get("browser_data", "browser_id")

    # Потім за потреби можна додати логін та пароль, перед цим додавши їх до app_config.ini

