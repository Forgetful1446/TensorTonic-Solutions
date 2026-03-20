def color_to_grayscale(image):
    """
    Convert an RGB image to grayscale using luminance weights.
    """
    gray = [[0 for _ in range(len(image[0]))] for _ in range(len(image))]
    for H in range(len(image)):
        for W in range(len(image[0])):
            gray[H][W] = 0.299 * image[H][W][0] + 0.587 * image[H][W][1] + 0.114 * image[H][W][2]
    return gray