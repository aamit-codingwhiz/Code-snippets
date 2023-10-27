import os
import sys
import librosa
import torch
import nemo.collections.asr as nemo_asr

if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")

class AudioSimilarityChecker:
    def __init__(self, audio_folder, threshold):
        self.audio_folder = audio_folder
        self.audio_list = []
        self.filenames = []
        self.threshold = threshold
        self.speaker_model = nemo_asr.models.EncDecSpeakerLabelModel.from_pretrained("nvidia/speakerverification_en_titanet_large")
        print("AudioSimilarityChecker class instance created")

    def is_folder_empty(self, folder_path):
        files = os.listdir(folder_path)
        if len(files) == 0:
            print(f'{folder_path} is empty')
            return True
        else:
            return False

    def load_audio_files(self):
        print(f'Loading audio files...')
        self.audio_list.clear()
        self.filenames.clear()
        try:
            for filename in os.listdir(self.audio_folder):
                if filename.endswith(".wav"):
                    file_path = os.path.join(self.audio_folder, filename)
                    self.filenames.append(filename)
                    self.audio_list.append(file_path)
            print(f'Audio files loaded successfully')
        except Exception as e:
            print("Error loading audio files: ", e)

    def compare_audio(self, audio_path):
        if not self.is_folder_empty(self.audio_folder):
            self.load_audio_files()
        else:
            return False, None

        y, sr = librosa.load(audio_path)
        print(f'Audio sample collected')

        batch_size = 10  # Number of audio files to process at once
        num_batches = (len(self.audio_list) + batch_size - 1) // batch_size

        max_similarity = 0.0
        max_index = -1

        for batch_idx in range(num_batches):
            batch_start = batch_idx * batch_size
            batch_end = min((batch_idx + 1) * batch_size, len(self.audio_list))
            batch_audio = [librosa.load(file_path)[0] for file_path in self.audio_list[batch_start:batch_end]]

            embeddings = [self.speaker_model.get_embedding(file_path) for file_path in self.audio_list[batch_start:batch_end]]
            embedding = self.speaker_model.get_embedding(audio_path)

            cosine_sim = torch.nn.CosineSimilarity(dim=-1)
            similarities = [cosine_sim(embedding, emb).item() for emb in embeddings]

            batch_max_similarity = max(similarities)
            batch_max_index = similarities.index(batch_max_similarity)

            if batch_max_similarity > max_similarity:
                max_similarity = batch_max_similarity
                max_index = batch_max_index + batch_start

        print(f'The maximum similarity is {max_similarity:.4f} and it is between {self.filenames[max_index]} and {audio_path}')
        if max_similarity < self.threshold:
            return False, None
        else:
            return True, self.filenames[max_index]


# Usage example
# audio_folder = "audio_record"
# threshold = 0.90
# audio_path = "audio/audio.wav"

# audio_similarity_checker = AudioSimilarityChecker(audio_folder, threshold)
# print(audio_similarity_checker.compare_audio(audio_path))
# print(audio_similarity_checker.compare_audio("audio/audio2.wav"))
# print(audio_similarity_checker.compare_audio("audio/audio3.wav"))
