import librosa
import numpy as np



class AudioAnalysis:
    def __init__(self) -> None:
        self.__mfcc_count = 39
        self.__feature_list = list()
        self.__generate_feature_list()

    def __generate_feature_list(self) -> None:
        for i in range(1, self.__mfcc_count + 1):
            self.__feature_list.append(f'mfcc_{i}')
        self.__feature_list += ['spectral_centroid', 'spectral_flux', 'zero_crossing_rate', 'short_time_energy']

    def get_feature_list(self):
        return self.__feature_list

    def __get_spectral_flux(self, audio_data):
        # Compute the spectrogram of the audio data using the short-time Fourier transform (STFT)
        spectrogram = librosa.stft(audio_data)
        # Calculate the magnitude of the spectrogram
        magnitude_spectrogram = np.abs(spectrogram)
        # Calculate the spectral flux by computing the squared difference between the current frame and the previous frame
        spectral_flux = np.zeros(len(magnitude_spectrogram[0]))
        for i in range(1, len(magnitude_spectrogram[0])):
            spectral_flux[i] = np.sum((magnitude_spectrogram[:, i] - magnitude_spectrogram[:, i-1])**2)
        # Normalize the spectral flux by dividing each value by the maximum value
        spectral_flux /= np.max(spectral_flux)
        return np.mean(spectral_flux)

    def get_features(self, audio_data, sample_rate):
        features = list()
        features += np.mean(librosa.feature.mfcc(y=audio_data, sr=sample_rate, n_mfcc=self.__mfcc_count), axis=1).tolist()
        features.append(np.mean(librosa.feature.spectral_centroid(y=audio_data, sr=sample_rate), axis=1)[0])
        features.append(self.__get_spectral_flux(audio_data))
        features.append(np.mean(librosa.feature.zero_crossing_rate(y=audio_data)[0]))
        features.append(np.mean(librosa.feature.rms(S=librosa.magphase(librosa.stft(audio_data))[0]), axis=1)[0])
        return features
