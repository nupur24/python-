



from PIL import Image

img= Image.open("sample.jpg")

s=img.convert("L")

p=s.rotate(-90)

htw= p.size[0]/2
hth= p.size[1]/2

t= p.crop(
        (
                htw -80,
                hth -102,
                htw +80,
                hth +102
        )
)        


t.size

t.thumbnail((75,75))

t.show()

u=raw_input("enter name")

t.save(u+".jpg")






