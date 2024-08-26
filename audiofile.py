import librosa
import soundfile as sf
import sounddevice as sd
def extract_sample(audio_file, start_time, end_time):
  """Extracts a sample from an audio file.

  Args:
    audio_file: Path to the audio file.
    start_time: Start time of the sample in seconds.
    end_time: End time of the sample in seconds.

  Returns:
    A NumPy array containing the audio sample.
  """

  y, sr = librosa.load(audio_file)
  start_sample = int(start_time * sr)
  end_sample = int(end_time * sr)
  sample = y[start_sample:end_sample]
  return sample

# Example usage:
audio_file = '/home/rguktrkvalley/sam_a_.wav'
y,sr = librosa.load(audio_file)
start_time = 10.0  # seconds
end_time = 15.0  # seconds
sample = extract_sample(audio_file, start_time, end_time)
k=sf.write('output.wav', sample,sr)
sd.play(k,sr)
sd.wait()



