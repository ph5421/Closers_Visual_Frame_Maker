from PIL import Image,ImageChops,ImageEnhance
import glob

def changeRGB(r,g,b,img):

    rgb = img.split()
    
    rb = ImageEnhance.Brightness(rgb[0]).enhance(r/100)
    gb = ImageEnhance.Brightness(rgb[1]).enhance(g/100)
    bb = ImageEnhance.Brightness(rgb[2]).enhance(b/100)

    out_img = Image.merge(img.mode, [rb,gb,bb,rgb[3]])

    return out_img
    

def combine(layer1,layer2):

    c_img = Image.new("RGBA", layer1.size)
    c_img = Image.alpha_composite(c_img, layer1)
    c_img = Image.alpha_composite(c_img, layer2)

    return c_img


def main(v_frame,b_image,red,green,blue,path):

    frames = []
    cframes = []
    mframes = []
    
    if v_frame==1:
        imgs = glob.glob("P_VISUAL_FRAME/*.png")
    elif v_frame==2:
        imgs = glob.glob("TC_VISUAL_FRAME/*.png")

    for i in imgs:
        new_frame = Image.open(i)
        frames.append(new_frame)
        
    for i in frames:
        cframes.append(changeRGB(red,green,blue,i))

    for i in cframes:
        mframes.append(combine(Image.open(b_image),i))

    mframes[0].save(path, format='GIF',
                    append_images=mframes[1:],
                    save_all=True,
                    duration=60, loop=0)


#if __name__=="__main__":
#    main(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5])
