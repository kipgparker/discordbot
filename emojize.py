import os
import json
import numpy as np

from torchmoji.sentence_tokenizer import SentenceTokenizer
from torchmoji.model_def import torchmoji_emojis


def get_data_file_path(relative_path):
    d = os.getcwd()
    # relative_path = r'app/data/' + relative_path
    file_path = os.path.join(d, relative_path)

    return file_path


# A list of all the emojis the model might respond with.
# See https://github.com/cw75/torchMoji/blob/master/examples/text_emojize.py for the full list.
EMOJIS = "😂 😒 😩 😭 😍 \
😔 👌 🤭 💜 😏 \
😀 🎶 😳 💯 😴 \
😌 😌 ✋ 💞 😑 \
😅 🙏 😕 😘 🖕 \
😐 💁 😞 🙈 😫 \
☮️ 😎 😡 👍 😢 \
😴 😋 😤 🤙 😷 \
👏 👀 🔫 😫 👿 \
💦 💔 💛 🎵 🙊 \
😉 💀 😖 😊 😜 \
😠 🙅 💪 👊 🍆 \
🍑 🥰 😬 ✨".split(' ')

# address = get_data_file_path("torchMoji/examples/text_emojize.py")
# with open(address, encoding="utf8") as f:
#     EMOJIS = f.read()
#     f.close()

# EMOJIS = open("./torchMoji/blob/master/examples/text_emojize.py", 'r')

# Specify the paths to the vocabulary and model weights files.
vocab_file_path = 'model/vocabulary.json'
model_weights_path = 'model/pytorch_model.bin'

# Returns the indices of the k largest elements in array.


def top_elements(array, k):
    ind = np.argpartition(array, -k)[-k:]
    return ind[np.argsort(array[ind])][::-1]


class Emojize:
    def __init__(self):
        with open(vocab_file_path, 'r') as f:
            vocabulary = json.load(f)

        max_sentence_length = 100
        self.st = SentenceTokenizer(vocabulary, max_sentence_length)
        self.model = torchmoji_emojis(model_weights_path)

    def predict(self, text):
        if not isinstance(text, list):
            text = [text]

        tokenized, _, _ = self.st.tokenize_sentences(text)
        # print(tokenized)
        prob = self.model(tokenized)[0]
        # print("Prob", prob)
        emoji_ids = top_elements(prob, 1)
        print("Emo Id: ", emoji_ids)
        # Emoji map in emoji_overview.png
        # print(EMOJIS)
        emojis = EMOJIS[emoji_ids[0]]
        # print("emojis", emojis)
        return emojis