import sys
sys.path.append('./src/services')

import unittest
import datetime
import os

from FileCachingService import FileCachingService

def createFile(path):
    utcDatetime = datetime.datetime.utcnow()
    fileName = utcDatetime.strftime("%Y-%m-%d-%H-%M-%S-%f") + ".txt"
    filePath = path + "/" + fileName
    handler = open(filePath, 'w+')
    for i in range(10):
        handler.write("This is line %d\r\n" % (i + 1))
    handler.close()

class TestFileCachingService(unittest.TestCase):

    def testGetCacheDirectory(self):
        cacheDirectory = FileCachingService.getCacheDirectory()
        directoryName = cacheDirectory.split('/')[-1]
        self.assertEquals(directoryName, 'cache')

    def testClear(self):
        cacheDirectory = FileCachingService.getCacheDirectory()
        createFile(cacheDirectory)
        self.assertTrue(len(os.listdir(cacheDirectory)) > 0)
        FileCachingService.clear()
        os.path.exists(cacheDirectory)
        self.assertTrue(len(os.listdir(cacheDirectory)) == 0)

if __name__ == '__main__':
    unittest.main()
