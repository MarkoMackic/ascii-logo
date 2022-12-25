import argparse, os
from PIL import Image, ImageDraw, ImageFont, ImageColor

def generate_ascii_art(text, font):
    font_variant = font.font_variant(size=int(os.environ.get('ASCII_GEN_FONT_SIZE', '50')))
    mask = font_variant.getmask(text, mode="1")
    width,height = mask.size

    lines = []

    for y in range(height):
        single_char_width = width // len(text)
        line = width * ['']
        for x in range(width):
            line[x] = text[x // single_char_width] if mask.getpixel((x,y)) > 0 else ' '

        lines.append(''.join(line))

    return lines



def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-t', '--text', help='Logo text')
    arg_parser.add_argument('-s', '--size', help='Image size in format x,y')
    arg_parser.add_argument('-f', '--font', help='Font file rendering ASCII art')
    arg_parser.add_argument('-fs', '--font-size', help="Font size for rendering final image")
    arg_parser.add_argument('-c', '--color', help='Foreground color')
    arg_parser.add_argument('-bg', '--background-color', help='Background color')
    arg_parser.add_argument('-o', '--output', help='Output file path')

    args = arg_parser.parse_args()

    assert not args.text is None, 'Text parameter must be supplied'

    im_size = tuple([int(size) for size in args.size.split(',')]) if not args.size is None else (200, 200)

    print('Image size is : ', im_size)

    im = Image.new(mode = 'RGBA', size = im_size, color=args.background_color)

    im_font = ImageFont.truetype(font = args.font or "./fonts/SourceCodePro-ExtraBold.ttf", size=int(args.font_size or 8));

    generated_art_str = '\n'.join(generate_ascii_art(args.text, im_font))

    im_draw = ImageDraw.Draw(im)
    im_draw.font = im_font

    (o_left, o_top, o_right, o_bottom) =  im_draw.textbbox(xy=tuple(map(lambda i: i // 2, im_size)), text=generated_art_str, anchor="mm")

    if o_left < 0 or o_top < 0 or o_right > im_size[0] or o_bottom > im_size[1]:
        print("Minimal image size for this configuration is", o_right - o_left, ',',  o_bottom - o_top)
        exit(1)

    # try to adjust font size based on space available

    font = im_font

    while True:
        new_font = font.font_variant(size=font.size + 1)

        (o_left, o_top, o_right, o_bottom) =  im_draw.textbbox(xy=tuple(map(lambda i: i // 2, im_size)), text=generated_art_str, anchor="mm", font=new_font)

        if o_left < 0 or o_top < 0 or o_right > im_size[0] or o_bottom > im_size[1]:
            break;

        font = new_font


    im_draw.font = font

    im_draw.text(xy=tuple(map(lambda i: i // 2, im_size)), text=generated_art_str, fill=ImageColor.getrgb(args.color or 'black'), anchor="mm")

    if not args.output is None:
        im.save(args.output)
    else:
        im.show()

if __name__ == '__main__':
    main()
