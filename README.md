# quran-verse-recognition
# quran-verse-recognition
An audio classification model trained on Quran verses. Data collected from [Al Quran's](https://alquran.cloud/) CDN.
Total of almost 200,000 .mp3 files (26 audio samples for each of the 6223 verses in the Quran).


## Project log

### Sept. 02, 2023
- Wrote scripts for verse classification 
- Thinking of generating a dataset of 161,798 audio samples, 26 for each of the 6223 verses,
 where each sample corresponds to a unique reciter

### Sept. 03, 2023
- Learned about threading in Python and used it to drastically speed up data collection, which involved many HTTP requests and so was IO-based
- Learned that audio classification can be considered image classification on audio spectrograms since any audio sample has a unique spectrogram
- Reorganized directory structure
- Choosing to use PyTorch instead of TensorFlow because the latter only supports .wav file formats for audio classification
- **Finished data collection, almost 200k .mp3 files**

