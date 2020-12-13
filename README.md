# Embedding subliminal messages in images

# Summary

This is a small utility that helps embed 1000s of characters of text in an image in such a way that it is perceived by the
 subconscious mind, and not the conscious mind. This is done by making the text transparent. The messages are repeated
 multiple times so that they cover the image. Also, the width adjustment is done to ensure that the messages span the
 entire image

# Execution

```bash
suchindra@suchindra-B250M-DS3H:~/src/image_subliminals/image_subliminal_messages_python$ python image_subliminals.py -h
usage: image_subliminals.py [-h] -m MESSAGES_FILE -i IMAGE_FILE -t TEXT_OPACITY [-r] [-f FONT_FAMILY] [-s FONT_SIZE] [-c TEXT_COLOR]
                            [-o OUTPUT_FILE]

optional arguments:
  -h, --help            show this help message and exit
  -m MESSAGES_FILE, --messages_file MESSAGES_FILE
                        File containing messages
  -i IMAGE_FILE, --image_file IMAGE_FILE
                        Image file
  -t TEXT_OPACITY, --text_opacity TEXT_OPACITY
                        Text opacity
  -r, --invert          Invert image?
  -f FONT_FAMILY, --font_family FONT_FAMILY
                        Text font family
  -s FONT_SIZE, --font_size FONT_SIZE
                        Font size
  -c TEXT_COLOR, --text_color TEXT_COLOR
                        Text color
  -o OUTPUT_FILE, --output_file OUTPUT_FILE
                        Output file
suchindra@suchindra-B250M-DS3H:~/src/image_subliminals$
suchindra@suchindra-B250M-DS3H:~/src/image_subliminals$ python image_subliminals.py -m msgs.txt -i nature.jpg -t 30 \
 -f "DejaVuSansMono.ttf" -s 20 -r

```
