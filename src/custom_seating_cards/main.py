from PIL import Image, ImageDraw
from pathlib import Path
import random

def main():
    opath = Path("outdir")

    names = ("John", "Jim", "Jones", "Jack", "James")

    for name in names:
        invite = Image.new("RGBA", [360,288], "white")
        draw = ImageDraw.Draw(invite)
        draw.text((160,130), f"{name}\nSeat {random.randint(0,100)}", align="center", fill="black" )
        draw.text((50,20), "definitely a flower", fill="black")
        invite.save(opath / f"{name}sinvite.png")


if __name__ == "__main__":
    main()
