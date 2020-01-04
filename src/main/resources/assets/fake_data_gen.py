from PIL import Image, ImageDraw, ImageFont
from string import ascii_lowercase
template_model = """{
    "parent": "block/cube_all",
    "textures": {
       "all": "letterblocks:block/%s"
    }
}"""
template_bs = """{
    "variants": {
        "": { "model": "letterblocks:block/%s" }
    }
}"""
template_item = """{
    "parent": "letterblocks:block/%s"
}"""

def make_model(path):
    with open(f'letterblocks/models/block/{path}.json', 'w') as f:
        f.write(template_model % path)
    with open(f'letterblocks/models/item/{path}.json', 'w') as f:
        f.write(template_item % path)
    with open(f'letterblocks/blockstates/{path}.json', 'w') as f:
        f.write(template_bs % path)



def make_texture(name, path):
    img = Image.new('RGB', (16, 16), color='white')
    fnt = ImageFont.truetype('mcfont.otf', 20)
    d = ImageDraw.Draw(img)
    d.text((3,-1), name, fill='black', font=fnt)
    img.save(path)

for char in ascii_lowercase:
    make_texture(char.upper(), f'letterblocks/textures/block/{char}_upper.png')
    make_model(f'{char}_upper')
for char in ascii_lowercase[:]:
    make_texture(char, f'letterblocks/textures/block/{char}_lower.png')
    make_model(f'{char}_lower')
