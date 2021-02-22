from PIL import Image

# ascii characters used
ascii_chars = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."]


# resizing the image
def resize_image(image, new_width=25):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return (resized_image)


# converting image into greyscale
def grayscale(image):
    grayscale_image = image.convert("L")
    return (grayscale_image)


# convert each pixel into a corresponding ASCII Character
def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ascii_chars[pixel // 25] for pixel in pixels])
    return (characters)


def main(new_width=25):
    # take the image from the user
    path = input('Enter a valid pathname to the image: ')
    try:
        image = Image.open(path)
    except:
        print(path, 'is not a valid pathname to the image')

# convert image into ascii
    new_image_data = pixels_to_ascii(grayscale(resize_image(image)))

# format
    pixel_count = len(new_image_data)
    ascii_image = '\n'.join(new_image_data[i:(i + new_width)] for i in range(0, pixel_count, new_width))

# print result
    print(ascii_image)

# save result to a txt file
    with open("ascii_image.txt","w") as f:
        f.write(ascii_image)

main()
