import unittest
from mashup import create_mashup
from pydub import AudioSegment

class TestMashup(unittest.TestCase):

    def test_create_mashup(self):
        audio1 = AudioSegment.from_file("test_audio1.mp3")
        audio2 = AudioSegment.from_file("test_audio2.mp3")

        input_files = [audio1, audio2]
        start = 5
        end = 15

        mashup = create_mashup(input_files, start, end)

        expected_mashup = audio1[start * 1000:end * 1000].append(audio2[start * 1000:end * 1000])
        self.assertEqual(mashup, expected_mashup)

if __name__ == '__main__':
    unittest.main()

