import csv
import sys
import os
from PIL import Image , ImageOps

if len(sys.argv) != 3:
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
    sys.exit(1)

elif not ((sys.argv[1].lower().endswith('.jpg')) or (sys.argv[1].lower().endswith('.png')) or (sys.argv[1].lower().endswith('.jpeg'))):
    print("Invalid input ")
    sys.exit(1)
    
elif not ((sys.argv[2].lower().endswith('.jpg')) or (sys.argv[2].lower().endswith('.png')) or (sys.argv[2].lower().endswith('.jpeg'))):
    print("Invalid input ")
    sys.exit(1)

elif not ((sys.argv[1].lower().endswith('.jpg') and sys.argv[2].lower().endswith('.jpg')) or (sys.argv[1].lower().endswith('.jpeg') and sys.argv[2].lower().endswith('.jpeg')) or (sys.argv[1].lower().endswith('.png') and sys.argv[2].lower().endswith('.png'))):
    print("Input and output have different extensions")
    sys.exit(1)

else:
    try:
        shirt = Image.open("shirt.png")
        user_image = Image.open(sys.argv[1])

        user_image = ImageOps.fit(user_image, shirt.size)
        # Overlay shirt using alpha channel
        user_image.paste(shirt, (0, 0), shirt)

        # Save final image
        user_image.save(sys.argv[2])
    except FileNotFoundError:
        print("Input file does not exist")
        sys.exit(1)
