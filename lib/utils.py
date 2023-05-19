from configparser import ConfigParser

def convert_seconds_to_time(seconds):
    minutes = seconds // 60
    seconds = seconds % 60

    time_string = "{:02d}:{:02d}".format(minutes, seconds)
    return time_string

def read_ini_config(file_path):
    parser = ConfigParser()
    parser.read(file_path)

    config = {}
    for section in parser.sections():
        config[section] = {}
        for key, value in parser.items(section):
            config[section][key] = value

    return config