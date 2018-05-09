import time

from PartitionService import PartitionService
from EnvironmentService import EnvironmentService

class USBStorageService(object):

    @staticmethod
    def saveFile(src):
        PartitionService.ensureIsMounted()
        if not PartitionService.isSufficientDiskSpaceAvailable(src):
            raise Exception('insufficient disk space available')
        USBStorageService.do_copy_file(src, PartitionService.getMountPath())

    @staticmethod
    def unmount():
        print('[USBStorageService] unmount()')
        if not EnvironmentService.isPi():
            print('[USBStorageService] unmount() 1')
            time.sleep(2)
            return

        if PartitionService.doesUnmountablePartitionExist():
            print('[USBStorageService] unmount() 2')
            PartitionService.do_unmount()
        else:
            print('partition was not mounted correctly (2)')
            raise Exception('partition was not mounted correctly (2)')

        if not PartitionService.doesUnmountablePartitionExist():
            print('Unmounted successfully')
        else:
            raise Exception('error unmounting')

    @staticmethod
    def isUSBStorageMounted():
        try:
            PartitionService.ensureIsMounted()
        except:
            return False
        return True

    @staticmethod
    def getPath():
        return PartitionService.getMountPath()

    @staticmethod
    def do_copy_file(src, dst):
        command = "cp -f " + src + " " + dst
        print(command)
        result = CommandLineService.run_command(command)
        print(result)