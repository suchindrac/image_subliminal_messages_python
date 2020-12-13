# Embedding subliminal messages in images

# Summary

This is a small utility that helps embed 1000s of characters of text in an image in such a way that it is perceived by the
 subconscious mind, and not the conscious mind. This is done by making the text transparent. The messages are repeated
 multiple times so that they cover the image. Also, the width adjustment is done to ensure that the messages span the
 entire image

# Execution

```bash
suchindra@suchindra-B250M-DS3H:~/src/image_subliminals$ python image_subliminals.py
usage: image_subliminals.py [-h] -m MESSAGES_FILE -i IMAGE_FILE -t TEXT_OPACITY [-r] [-f FONT_FAMILY] [-s FONT_SIZE] [-c TEXT_COLOR]
                            [-o OUTPUT_FILE]
image_subliminals.py: error: the following arguments are required: -m/--messages_file, -i/--image_file, -t/--text_opacity
suchindra@suchindra-B250M-DS3H:~/src/image_subliminals$
suchindra@suchindra-B250M-DS3H:~/src/image_subliminals$ python image_subliminals.py -m msgs.txt -i nature.jpg -t 30 \
 -f "DejaVuSansMono.ttf" -s 20 -r

```
