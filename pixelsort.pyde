import os.path
from os.path import expanduser

def setup():
    global img
    global sorted_image_filename
    sorted_image_filename = "sorted.jpg"
    original_filename = "IMG_0183.JPG"
    img = loadImage(original_filename)
    size(410, 600)


def draw():
    img.loadPixels()
    sorted_img = createImage(img.width, img.height, RGB)
    sorted_img.loadPixels()
    sorted_img.pixels = mergesort(img.pixels)
    sorted_img.updatePixels()
    image(sorted_img, 0, 0)
    save(os.path.join(os.path.expanduser("~"), "Downloads", sorted_image_filename))


def mergesort(arr):
    if len(arr) <= 1:
        return arr
    else:
        left = arr[:len(arr) / 2]
        right = arr[len(arr) / 2:]
        return _merge(mergesort(left), mergesort(right))


def _merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result += left
    result += right
    return result