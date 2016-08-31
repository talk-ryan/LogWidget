"""This file will contain the main function and serve as the starting point for the application"""
import os
import configparser
from datetime import datetime
from datetime import date

# Global Variables
CONFIG_FILE = 'logs.cfg'
FILE_NAMES_OPTION = 'filenames'
PATH_OPTION = 'path'
DELIMITER = ','
ZIPPED_LOGS_LOCATION_OPTION = 'ZIPPED_LOGS_LOCATION'
DESTINATION_SECTION = 'Destination'


# TODO Modify so this works on a server
def get_log_files(network_path):
    """Returns the file paths from the config file that exist"""
    log_files = []
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)

    append_time = '.' + get_log_time()

    for section in config.sections():
        if config.has_option(section, 'path'):
            path = config.get(section, 'path')

            # Check for valid path
            if os.path.exists(network_path + os.path.dirname(config.get(section, 'path'))):
                file_names = get_file_names(section, append_time)
                for file_name in file_names:
                    file = path + "\\" + file_name

                    # Check if file exists
                    if os.path.isfile(file):
                        log_files.append(file)
                    else:
                        print("File from config does not exist: Machine: {0} Section: {1}. filename: {2}".format(
                            network_path, section, file_name))
            else:
                print("PATH from config does not exist. Machine: {0} Section: {1}, path: {2}".format(
                    network_path, section, config.get(section, 'path')))

    return log_files


def get_file_names(section, append_to_name=''):
    """Returns the file names to search for in each path.  Also provides the option to append to file names.
    i.e. a time or date stamp"""
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    file_names = []
    if config.has_section(section):
        if config.has_option(section, FILE_NAMES_OPTION):
            files = config.get(section, FILE_NAMES_OPTION)
            file_names = files.split(DELIMITER)

    if append_to_name != '':
        for i in range(0, len(file_names)):
            file_names[i] = file_names[i] + append_to_name
        return file_names


# TODO Modify to get the time on the server or assume local time is same as server time
def get_log_time():
    """Returns the time string to append to log filenames.
    The format returned is the actual system time"""
    # c_time = subprocess.call('net time ' + r'\\' + ip_address)
    # print(c_time)
    today = date.today().strftime("%Y-%m-%d")
    am_or_pm = '(AM)' if datetime.now().hour < 12 else '(PM)'
    appended_time = today + am_or_pm
    return appended_time


# TODO Setup Zipped Log Location in config file
# TODO Get Zipped Log Location from config file
def get_zipped_log_location():
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    if config.has_section(DESTINATION_SECTION):
        a = 5
    pass

# TODO setup machine names and ip addresses in config files.
# TODO return a dictionary or list of tuples
def get_machine_and_ip_addresses():
    pass
# TODO Get Zipped Log Location from config file

if __name__ == '__main__':
    print('get_log_time(): {0}'.format(get_log_time()))
    append_time = '.' + get_log_time()
    print('get_file_names(\'Web\'): {0}'.format(get_file_names('Web', append_time)))
    print('get_log_files(RT-DESKTOP): {0}'.format(get_log_files('RT-DESKTOP')))
