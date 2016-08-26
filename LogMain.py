"""This file will contain the main function and serve as the starting point for the application.
When this file is run as main, zipped logged files should be created and stored in C:\ZippedLogs"""
import os
import zipfile
import configparser
import time
import paramiko
from smb.SMBConnection import SMBConnection
import tempfile
import subprocess
import ConfigurationUtility as Cu
import sys
import shutil
from datetime import datetime
from datetime import date


def create_directory(path):
    """This function will create a directory name to store the log zip files"""
    print('in create_directory')
    if not os.path.exists(path):
        os.mkdir(path)
    return


def zip_logs(log_files):
    """Zips the log_files and stores them in the default location"""
    zip_file = zipfile.ZipFile(r'c:\Test\Test2\UltimateTest2.zip', 'w')
    for file in log_files:
        zip_file.write(file)
    zip_file.close()
    return 1


# TODO Connect to the host and be able to run the get_log_files method
def test_shutil():
    """Test method that Zips the logs from a remote server"""
    network_path = r'\\10.1.1.226'
    user = 'qauser@qa.rsi'
    password = 'test@qa'
    try:
        connect_to_network = 'NET USE ' + network_path + ' /User:' + user + ' ' + password
        subprocess.Popen(connect_to_network, stdout=subprocess.PIPE, shell=True)
        if os.path.exists(network_path + r'\RSI\Logs\BRE\WebService.log.2016-08-22(AM)'):
            print("It exists")
        files = Cu.get_log_files(network_path)
        zip_logs(files)
        disconnect_from_network = 'NET USE ' + network_path + ' /delete'
        subprocess.Popen(disconnect_from_network, stdout=subprocess.PIPE, shell=True)

    except subprocess.SubprocessError:
        disconnect_from_network = 'NET USE ' + network_path + ' /delete'
        subprocess.Popen(disconnect_from_network, stdout=subprocess.PIPE, shell=True)
        e = sys.exc_info()
        print(e)
    # shutil.copy2(network_path + r'\RSI\Logs\BRE\WebService.log.2016-08-22(AM)', r'C:\test.log')
    pass


def main():
    """This is the start of the application"""
    print('In Main')
    create_directory("c:\ZippedLogs")
    test_shutil()
    pass

if __name__ == '__main__':
    # test_shutil()
    # test_paramiko()
    # get_log_time()
    # get_log_files()
    main()
