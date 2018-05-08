import unittest
import sys
sys.path.append('./src/services')

from FilenameService import FilenameService

class TestFilenameService(unittest.TestCase):

    def testGenerateTimeBasedFilename(self):
        fileType = 'jpeg'
        fileName = FilenameService.generateTimeBasedFilename(fileType)
        self.assertEqual(fileName[-len(fileType):], fileType)

    def testGetTimeString(self):
        timeString = FilenameService.getTimeString()
        hyphenCount = timeString.count('-')
        self.assertEqual(hyphenCount, 6)

if __name__ == '__main__':
    unittest.main()
