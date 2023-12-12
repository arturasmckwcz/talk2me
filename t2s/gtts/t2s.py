from gtts import gTTS
from io import BytesIO

# import pygame
import os
import sys

lang = sys.argv[1] if len(sys.argv) > 1 else "en"

mp3_fp = BytesIO()

text = (
    "Wir werden eine Menge zu tun haben, außer diese Leute zu studieren."
    if lang == "de"
    else "now it is time to go; nothing holds me back; yes I have tried hard; and I have failed."
)
tts = gTTS(text=text, lang=lang)

tts.write_to_fp(mp3_fp)
mp3_fp.seek(0)

# pygame.init()
# pygame.mixer.init()
# pygame.mixer.music.load(mp3_fp)

# pygame.mixer.music.play()
# while pygame.mixer.music.get_busy():
#     pygame.time.Clock().tick(10)

# pygame.mixer.quit()
# pygame.quit()

os.makedirs("../../mp3", exist_ok=True)
tts.save(f"../../mp3/test_gtts_{lang}.mp3")
