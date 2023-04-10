import unittest
from file_operations import load_files
from pydub import AudioSegment

class TestFileOperations(unittest.TestCase):

    def test_load_files(self):
        filepaths = ["test_audio1.mp3", "test_audio2.mp3"]
        audio_files = load_files(filepaths)

        self.assertIsInstance(audio_files[0], AudioSegment)
        self.assertIsInstance(audio_files[1], AudioSegment)

if __name__ == '__main__':
    unittest.main()

