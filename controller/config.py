import yaml

CONFIG_FILE_PATH = "config.yaml"
_config = {}

DEFAULT_CONFIG = {
                  "CurrentModelSet": "",
                  "CurrentRefAudio": "",
                  "TopK": 5,
                  "TopP": 1.00,
                  "Temp": 1.00,
                  "Lang": "中文",
                  "HowToCut": "凑四句一切",
                  "AlwaysTop": True,
                  "AutoTrans": True,
                  "SavePath": "",
                  "ModelSets": None
                  }


def init():
    global _config
    try:
        with open(CONFIG_FILE_PATH, 'r', encoding="utf-8") as file:
            _config = yaml.safe_load(file)
        if _config is None:
            _config = DEFAULT_CONFIG
    except FileNotFoundError:
        _config = DEFAULT_CONFIG


def get_config(key, default=None):
    keys = key.split('.')
    result = _config
    for k in keys:
        if k in result:
            result = result[k]
        else:
            return default
    return result


def set_config(key, value):
    global _config
    keys = key.split('.')
    config = _config
    for k in keys[:-1]:
        if k not in config:
            config[k] = {}
        config = config[k]
    config[keys[-1]] = value


def save_config():
    with open(CONFIG_FILE_PATH, 'w', encoding="utf-8") as file:
        yaml.dump(_config, file, default_flow_style=False, sort_keys=False, encoding="utf-8")
