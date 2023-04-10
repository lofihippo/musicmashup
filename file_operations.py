from pydub import AudioSegment

def load_files(filepaths):
    """
    Load MP3 files from the given filepaths.

    :param filepaths: List of strings containing the filepaths of the MP3 files.
    :return: List of AudioSegment instances.
    """

    audio_files = []

    for filepath in filepaths:
        audio = AudioSegment.from_mp3(filepath)
        audio_files.append(audio)

    return audio_files