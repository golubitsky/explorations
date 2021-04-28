# https://github.com/castorini/howl

from howl.client import HowlClient

import torch
print(f'PyTorch version: {torch.__version__}')


def hello_callback(detected_words):
    print("Detected: {}".format(detected_words))


client = HowlClient()

entrypoints = torch.hub.list('pytorch/vision', force_reload=True)

client.from_pretrained("hey_fire_fox", force_reload=False)
client.add_listener(hello_callback)
client.start().join()
