"""This file will contain the main function and serve as the starting point for the application.
When this file is run as main, zipped logged files should be created and stored in C:\ZippedLogs"""
import os
import zipfile
import subprocess
import ConfigurationUtility as Cu
from datetime import datetime
import sys


def create_directory(path):
    """This function will create a directory name to store the log zip files"""
    print('in create_directory')
    if not os.path.exists(path):
        os.mkdir(path)
    return


# TODO remove hard coded file paths and put them in the config file
def zip_logs(log_files, ip_address=''):
    """Zips the log_files and stores them in the default location"""
    if not log_files:
        return

    file_location = Cu.get_zipped_log_location()
    machine_name = ip_address.replace('\\', '')
    file_name = 'LOGS_' + machine_name + '_' + get_timestamp() + '.zip'
    print(file_name)
    with zipfile.ZipFile(file_location + file_name, 'w') as zip_file:
        for file in log_files:
            zip_file.write(file)
    return 1


# TODO remove hard coded file paths and put them in the config file
# TODO permit this method to return an error code
def connect_and_process(network_path, user, password):
    """Test method that Zips the logs from a remote server"""
    try:
        connect_to_network = 'NET USE ' + network_path + ' /User:' + user + ' ' + password
        subprocess.Popen(connect_to_network, stdout=subprocess.PIPE, shell=True)
        files = Cu.get_all_log_files(network_path)
        zip_logs(files, network_path)
        disconnect_from_network = 'NET USE ' + network_path + ' /delete'
        subprocess.Popen(disconnect_from_network, stdout=subprocess.PIPE, shell=True)
        return 0
    except subprocess.SubprocessError:
        disconnect_from_network = 'NET USE ' + network_path + ' /delete'
        subprocess.Popen(disconnect_from_network, stdout=subprocess.PIPE, shell=True)
        e = sys.exc_info()
        print(e)
        return 1
    pass


def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d-%I.%M.%S(%p)")

# TODO Remove hardcoded network paths - Make configurable from UI
# TODO Remove hardcoded username and password - Make configurable in cfg file
def main():
    """This is the start of the application"""
    print('In Main')
    create_directory("c:\ZippedLogs")
    network_path = r'\\networkpath or ip address'
    connect_and_process(network_path, 'username', 'password')
    pass

if __name__ == '__main__':
    # test_shutil()
    # test_paramiko()
    # get_log_time()
    # get_log_files()
    print('get_timestamp(): ' + 'LOGS_' + get_timestamp() + '.log')
    main()
