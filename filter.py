import numpy as np
from PIL import Image

DEFAULT_SIZE = 10
DEFAULT_STEP = 50
DEFAULT_NUM_GRAD = 6


def find_step(n: int = DEFAULT_NUM_GRAD):
    """Converts the number of gradations to the step size.

    :param n: number of gradations
    :type: int

    :return: step
    :rtype: int

    >>> find_step(6)
    50
    >>> find_step(2)
    254
    >>> find_step(5)
    63
    """
    return int(255 / (n - 1) - 1 if 255 % (n - 1) == 0 else 255 / (n - 1))


def find_av_brightness(i: int, j: int, arr: np.ndarray,
                       m_h: int = DEFAULT_SIZE,
                       m_w: int = DEFAULT_SIZE,
                       step: int = DEFAULT_STEP):
    """Searches for the average brightness of a group of pixels.

    :param i: array row
    :type: int
    :param j: array column
    :type: int
    :param arr: the array obtained from the image
    :type: np.ndarray
    :param m_h: height of element mosaic
    :type: int
    :param m_w: width of element mosaic
    :type: int
    :param step: step size
    :type: int

    :return: average brightness
    :rtype: float
    """
    br = np.average(arr[i: i + m_h, j: j + m_w])
    return br - br % step


def do_mosaic(arr: np.ndarray,
              m_h: int = DEFAULT_SIZE,
              m_w: int = DEFAULT_SIZE,
              step: int = DEFAULT_STEP):
    """Modifies the input array so that the image obtained
    from it looks like pixel art.

    :param arr: the array obtained from the image
    :type: np.ndarray
    :param m_h: height of element mosaic
    :type: int
    :param m_w: width of element mosaic
    :type: int
    :param step: step size
    :type: int
    """
    for i in range(0, len(arr), m_h):
        for j in range(0, len(arr[1]), m_w):
            arr[i: i + m_h, j: j + m_w] = \
                find_av_brightness(i, j, arr, m_h, m_w, step)


def save_img(arr: np.ndarray, source_name: str):
    """Saves the array as an image.

    :param arr: the array obtained from the image
    :type: np.ndarray
    :param source_name: the name of the source image (for example: img.jpg)
    :type: str
    """
    inp_res_name = input('Enter the name of the result (for example: res.jpg)'
                         ' or press Enter to apply the default name '
                         '"res_<source name>": ')
    res_name = inp_res_name if len(inp_res_name) > 0 else f"res_{source_name}"
    Image.fromarray(arr).save(res_name)


file_name = input('Enter the name of the source image '
                  '(for example: img.jpg): ')
inp_sizes = input('Enter the height and width of the mosaic element '
                  'separated by comma (for example: 10,10) '
                  'or press Enter to apply the default value: ')
num_grad = input('Enter the number of gradations or press Enter '
                 'to apply the default value: ') \
           or DEFAULT_NUM_GRAD

inp_im = np.array(Image.open(f"{file_name}"))
img = Image.open(f"{file_name}")
sizes = list(map(int, inp_sizes.split(','))) if len(inp_sizes) > 0 \
    else [DEFAULT_SIZE, DEFAULT_SIZE]

do_mosaic(inp_im, sizes[0], sizes[1], find_step(int(num_grad)))
save_img(inp_im, file_name)
