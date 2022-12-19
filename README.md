## Nothing special, nothing much.

Basic ASCII logo generator!

Required Python version : `>=3.7`

## Usage

```
usage: generator.py [-h] [-t TEXT] [-s SIZE] [-f FONT] [-fs FONT_SIZE] [-c COLOR] [-bg BACKGROUND_COLOR] [-o OUTPUT]

options:
  -h, --help            show this help message and exit
  -t TEXT, --text TEXT  Logo text
  -s SIZE, --size SIZE  Image size in format x,y
  -f FONT, --font FONT  Font file rendering ASCII art
  -fs FONT_SIZE, --font-size FONT_SIZE
                        Font size for rendering final image
  -c COLOR, --color COLOR
                        Foreground color
  -bg BACKGROUND_COLOR, --background-color BACKGROUND_COLOR
                        Background color
  -o OUTPUT, --output OUTPUT
                        Output file path
```

If output is specifed then it will save the image, otherwise it'll just show you the image.
Background is transparent by default.
Fonts are TTF only.
Experiment with font size param, and ASCII_GEN_FONT_SIZE environment variable to tweak the sizes of single char vs whole text.
Also the text will try to ocupy the space available, it'll be centered on the image.


## Example

![Example image](example.png)
