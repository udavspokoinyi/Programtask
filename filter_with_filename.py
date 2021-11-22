import numpy as np
from PIL import Image

DEFAULT_SIZE = 10
DEFAULT_STEP = 50
DEFAULT_NUM_GRAD = 6


def find_step(n):
    return int(255 / (n - 1) - 1 if 255 % (n - 1) == 0 else 255 / (n - 1))


def find_av_brightness(i, j, arr, mosaic_height=DEFAULT_SIZE,
                       mosaic_width=DEFAULT_SIZE, step=DEFAULT_STEP):
    br = np.average(arr[i: i + mosaic_height, j: j + mosaic_width])
    return br - br % step


def do_mosaic(arr, mosaic_height=DEFAULT_SIZE,
              mosaic_width=DEFAULT_SIZE, step=DEFAULT_STEP):
    for i in range(0, len(arr), mosaic_height):
        for j in range(0, len(arr[1]), mosaic_width):
            arr[i: i + mosaic_height, j: j + mosaic_width] = \
                find_av_brightness(i, j, arr, mosaic_height, mosaic_width, step)


def save_img(arr, source_name):
    Image.fromarray(arr).save(f"res_{source_name}")


file_name = "img.jpg"
inp_im = np.array(Image.open(file_name))
sizes = [DEFAULT_SIZE, DEFAULT_SIZE]

do_mosaic(inp_im, sizes[0], sizes[1], DEFAULT_STEP)
save_img(inp_im, file_name)
