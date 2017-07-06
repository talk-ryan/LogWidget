"""This file will contain the main function and serve as the starting point for the application"""
import os
import configparser
from datetime import date

# Global Variables
CONFIG_FILE = 'logs.cfg'
FILE_NAMES_OPTION = 'filenames'
PATH_OPTION = 'path'
DELIMITER = ','
ZIPPED_LOGS_LOCATION_OPTION = 'ZIPPED_LOGS_LOCATION'
DESTINATION_SECTION = 'Destination'
DAL = 'DAL'
CREDENTIALS_SECTION = 'Credentials'
USER_OPTION = 'user'
PASSWORD_OPTION = 'password'


# TODO Modify to write print statements to a log file
def get_all_log_files(network_path):
    """Returns all file paths from the config file that exist"""
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)

    # otherwise use all sections
    return get_log_files_from_sections(network_path, config.sections())


def get_log_files_from_sections(network_path, sections):
    log_files = []
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    append_time = '.' + get_log_time()
    for section in sections:
        # This if statement was to make this function more versatile to get any section with a path option
        if config.has_section(section) and config.has_option(section, PATH_OPTION):
            path = config.get(section, PATH_OPTION)
            # Check for valid path
            if os.path.exists(network_path + os.path.dirname(config.get(section, PATH_OPTION))):
                if section == DAL:
                    file_names = get_file_names(section)
                else:
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
    print(log_files)
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


def get_log_time():
    """Returns the time string to append to log filenames.
    The format returned is the actual system time"""
    today = date.today().strftime("%Y-%m-%d(%p)")
    return today


def get_zipped_log_location():
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    if config.has_section(DESTINATION_SECTION):
        path = config.get(DESTINATION_SECTION, ZIPPED_LOGS_LOCATION_OPTION)
        if path[-1] != '\\':
            path += '\\'
    return path

# TODO setup machine names and ip addresses in config files.
# TODO return a dictionary or list of tuples
def get_machine_and_ip_addresses():
    pass
# TODO Get Zipped Log Location from config file


def get_user():
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    if config.has_section(CREDENTIALS_SECTION):
        if config.has_option(CREDENTIALS_SECTION, USER_OPTION):
            return config.get(CREDENTIALS_SECTION, USER_OPTION)
        else:
            print("No \'" + USER_OPTION + "\' option in the config file")
    else:
        print("No \'"+CREDENTIALS_SECTION + "\' Section in config file")


def get_password():
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    if config.has_section(CREDENTIALS_SECTION):
        if config.has_option(CREDENTIALS_SECTION, PASSWORD_OPTION):
            return config.get(CREDENTIALS_SECTION, PASSWORD_OPTION)
        else:
            print("No \'" + PASSWORD_OPTION + "\' option in the config file")
    else:
        print("No \'"+CREDENTIALS_SECTION + "\' Section in config file")

# TODO update test cases for particular machine - Possibly make a config file for test cases.
if __name__ == '__main__':
    print('get_log_time(): {0}'.format(get_log_time()))
    append_time = '.' + get_log_time()
    print('get_file_names(\'Web\'): {0}'.format(get_file_names('Web', append_time)))
    print('get_log_files(Test-Desktop): {0}'.format(get_all_log_files('Test-Desktop')))
    print('get_zipped_log_location: {0}'.format(get_zipped_log_location()))
    print('get_user(): {}'.format(get_user()))
