# IMPORTS
# IMPORTS
import numpy as np
# np.complex is deprecated in 1.26, so this is a temp workaround (librosa requires 1.24)
if not hasattr(np, 'complex'):
    np.complex = complex

import matplotlib.pyplot as plt # version 3.9.0
import librosa, librosa.display # version 0.10.2.post1

# ----------------------------------------------------------------------#
def compute_spectrogram(filename, sr=22050, n_fft=2048, hop_length=512):
    """
    Computes the spectrogram of an audio file.

    Args:
        filename (str): Path to the audio file.
        sr (int, optional): Sample rate of the audio file. Defaults to 22050 Hz.
        n_fft (int, optional): Window size for the STFT. Defaults to 2048 samples.
        hop_length (int, optional): Hop length for the STFT. Defaults to 512 samples.

    Returns:
        np.ndarray: Log-scaled spectrogram.
        int: Sample rate of the audio file.

    """
    try:
        signal, sr = librosa.load(filename, sr=sr)
        stft = librosa.stft(signal, n_fft=n_fft, hop_length=hop_length)
        spectrogram = np.abs(stft)
        log_spectrogram = librosa.amplitude_to_db(spectrogram)
        return log_spectrogram, sr
    
    except Exception as e:
        print(f"Error: {e}")
        return None, None

# ----------------------------------------------------------------------#
def display_spectrogram(spectrogram, sr, hop_length):
    """
    Displays the given spectrogram.

    Args:
        spectrogram (np.ndarray): Log-scaled spectrogram.
        sr (int): Sample rate of the audio file.
        hop_length (int): Hop length used for the STFT.
    """
    librosa.display.specshow(spectrogram, sr=sr, hop_length=hop_length, x_axis='time', y_axis='hz')
    plt.xlabel("Time")
    plt.ylabel("Frequency")
    plt.colorbar(format='%+2.0f dB')
    plt.tight_layout()
    plt.show()

# ----------------------------------------------------------------------#
def input_to_spectrogram(filename, sr=22050, n_fft=2048, hop_length=512):
    """
    Computes and displays the spectrogram of an audio file.

    Args:
        filename (str): Path to the audio file.
        sr (int, optional): Sample rate of the audio file. Defaults to 22050 Hz.
        n_fft (int, optional): Window size for the STFT. Defaults to 2048 samples.
        hop_length (int, optional): Hop length for the STFT. Defaults to 512 samples.

    """
    spectrogram, sr = compute_spectrogram(filename, sr, n_fft, hop_length)
    if spectrogram is not None:
        display_spectrogram(spectrogram, sr, hop_length)
    else:
        print("Failed to compute spectrogram.")