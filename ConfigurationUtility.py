"""This file will contain the main function and serve as the starting point for the application"""
import os
import zipfile
import configparser
import subprocess
from datetime import datetime
from datetime import date

# Global Variables
CONFIG_FILE = 'logs.cfg'


# TODO Modify so this works on a server
def get_log_files(network_path):
    """Returns the file paths from the config file that exist"""
    log_files = []
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)

    for section in config.sections():
        if config.has_option(section, 'path'):
            path = config.get(section, 'path')

            # Check for valid path
            if os.path.exists(network_path + os.path.dirname(config.get(section, 'path'))):
                file_names = get_file_names(section)
                for file_name in file_names:
                    file = path + "\\" + file_name

                    # Check if file exists
                    if os.path.isfile(file):
                        log_files.append(file)
                    else:
                        print("File from config does not exist: Machine: {0} Section: {1}. filename: {2}".format(
                            network_path, section, file_name))
            else:
                print("Path from config does not exist. Section: {0}, path: {1}".format(
                    section, config.get(section, 'path')))

    return log_files


# TODO Make the file names come from the config file and parse multiple names
def get_file_names(section):
    """Returns the file names to search for in each path"""
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)


    file_names = ['WebService.log', 'WebServicePerformance.log']
    append_time = get_log_time()
    for i in range(0, len(file_names)):
        file_names[i] = file_names[i] + "." + append_time
    return file_names


# TODO Modify to get the time on the server or assume local time is same as server time
def get_log_time(ip_address):
    """Returns the time string to append to log filenames.
    The format returned is the actual system time"""
    c_time = subprocess.call('net time ' + r'\\' + ip_address)
    print(c_time)
    today = date.today().strftime("%Y-%m-%d")
    am_or_pm = '(AM)' if datetime.now().hour < 12 else '(PM)'
    appended_time = today + am_or_pm
    return appended_time



if __name__ == '__main__':
    print('get_log_time(): {0}'.format('10.1.1.242'))
    print('get_log_files(RT-DESKTOP): {0}'.format(get_log_files('RT-DESKTOP')))
