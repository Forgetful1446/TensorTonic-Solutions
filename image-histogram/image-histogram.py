def image_histogram(image):
    """
    Compute the intensity histogram of a grayscale image.
    """
    result = [0 for _ in range(256)]
    for row in image:
        for value in row:
            result[value] += 1
            
    return result