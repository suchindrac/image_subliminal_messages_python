from PIL import Image, ImageDraw, ImageFont, ImageColor
import PIL.ImageOps
import argparse
import sys
import textwrap

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--messages_file", type = str, required = True,
                            help = "File containing messages")
    parser.add_argument("-i", "--image_file", type = str, required = True,
                            help = "Image file")
    parser.add_argument("-t", "--text_opacity", type = int, required = True,
                            help = "Text opacity")
    parser.add_argument("-r", "--invert", action = "store_true",
                            help = "Invert image?")
    parser.add_argument("-f", "--font_family", type = str, required = False,
                            help = "Text font family")
    parser.add_argument("-s", "--font_size", type = int, required = False,
                            help = "Font size")
    parser.add_argument("-c", "--text_color", type = str, required = False,
                            help = "Text color")
    parser.add_argument("-o", "--output_file", type = str, required = False,
                            help = "Output file")

    args = parser.parse_args()

    font_family = "DejaVuSansMono.ttf"
    font_size = 40
    text_color = "red"
    output_file = None

    msgs_file = args.messages_file
    img_file = args.image_file
    t_op = args.text_opacity
    inv_img = args.invert

    if args.font_family:
        font_family = args.font_family
    if args.font_size:
        font_size = args.font_size
    if args.text_color:
        text_color = args.text_color

    if args.output_file:
        output_file = args.output_file

    try:
        text_color = ImageColor.getrgb(text_color)
        text_color = list(text_color)
        text_color.append(t_op)
        text_color = tuple(text_color)
    except:
        print("Color %s not defined, exiting" % (text_color))
        print(sys.exc_info())
        sys.exit(1)

    try:
        font = ImageFont.truetype(font_family, font_size)

        img = Image.open(img_file)
        img.mode = "RGB"
        if inv_img:
            img = PIL.ImageOps.invert(img)

        img = img.convert("RGBA")
        img_width, img_height = img.size

        text = Image.new('RGBA', img.size, (255,255,255,0))

        msgs_fd = open(msgs_file, 'r')
        msgs_l = msgs_fd.readlines()
        msgs_l = [x.strip() for x in msgs_l]
        msgs_s = "    ".join(msgs_l)
        msgs_s = "".join([msgs_s for x in range(1000)])

        test = "a"
        line_width, line_height = font.getsize(test)
        while line_width < img_width:
            line_width, line_height = font.getsize(test)
            test += "a"

        text_width = len(test)

        msgs_l = textwrap.wrap(msgs_s, text_width)
        msgs_s = "".join(msgs_l)

        msgs_fd.close()
        draw = ImageDraw.Draw(text)

        y_text = 0
        for line in msgs_l:
            line_width, line_height = font.getsize(line)
            draw.text(((img_width - line_width) / 2, y_text),
                        line, font=font, fill = text_color)
            y_text += line_height

        combined = Image.alpha_composite(img, text)
        if output_file:
            combined.save(output_file)
        else:
            combined.show()
    except:
        print("Exception hit:")
        print(sys.exc_info())
