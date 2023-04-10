from pydub import AudioSegment

def create_mashup(audio_files, timestamp_ranges, end=None):
    output = AudioSegment.empty()
    for audio_file, (start, end) in zip(audio_files, timestamp_ranges):
        start_ms = start * 1000
        if end is not None:
            end_ms = end * 1000
            output += audio_file[start_ms:end_ms]
        else:
            output += audio_file[start_ms:]

    return output
