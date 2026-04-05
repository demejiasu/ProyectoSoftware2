from PIL import Image, ImageDraw, ImageFont

img = Image.new('RGB', (900, 450), color='white')
draw = ImageDraw.Draw(img)

blue = '#4A90D9'
green = '#5D8C4A'
gray = '#666666'

try:
    font = ImageFont.truetype('arial.ttf', 16)
    font_small = ImageFont.truetype('arial.ttf', 12)
except:
    font = ImageFont.load_default()
    font_small = font

def draw_box(x, y, w, h, text, color):
    draw.rectangle([x, y, x+w, y+h], fill=color, outline='#333', width=2)
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    draw.text((x + (w-tw)//2, y + 15), text, fill='white', font=font)

def draw_db(x, y, text, color):
    draw.ellipse([x-55, y-22, x+55, y+22], fill=color, outline='#333', width=2)
    bbox = draw.textbbox((0, 0), text, font=font_small)
    tw = bbox[2] - bbox[0]
    draw.text((x - tw//2, y - 7), text, fill='white', font=font_small)

draw_box(375, 30, 150, 50, 'Cliente', blue)
draw_box(375, 120, 150, 50, 'API Gateway', blue)
draw_box(50, 230, 130, 50, 'Auth :8000', blue)
draw_box(200, 230, 130, 50, 'Users :8001', blue)
draw_box(350, 230, 130, 50, 'Products :8002', blue)
draw_box(500, 230, 130, 50, 'Orders :8003', blue)
draw_box(650, 230, 130, 50, 'Notify :8004', blue)

draw_db(115, 370, 'MySQL', green)
draw_db(285, 370, 'PostgreSQL', green)
draw_db(455, 370, 'MongoDB', green)

draw.line([450, 80, 450, 120], fill=gray, width=2)
draw.line([400, 170, 115, 230], fill=gray, width=2)
draw.line([420, 170, 265, 230], fill=gray, width=2)
draw.line([450, 170, 415, 230], fill=gray, width=2)
draw.line([480, 170, 565, 230], fill=gray, width=2)
draw.line([500, 170, 715, 230], fill=gray, width=2)
draw.line([115, 280, 115, 348], fill=gray, width=2)
draw.line([285, 280, 285, 348], fill=gray, width=2)
draw.line([455, 280, 455, 348], fill=gray, width=2)

draw.text((415, 175), ':3000', fill=gray, font=font_small)

img.save('diagrama.png')
print('diagrama.png creado')