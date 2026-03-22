def rating_normalization(matrix):
    """
    Mean-center each user's ratings in the user-item matrix.
    """
    normalized_rating =  [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    for row in range(len(matrix)):
        means = 0
        rated = 0
        for col in range(len(matrix[0])):
            if matrix[row][col] == 0:
                continue
            means += matrix[row][col]
            rated += 1
        if rated != 0:
            means /= rated
        for col in range(len(matrix[0])):
            if matrix[row][col] == 0:
                continue
            normalized_rating[row][col] =  matrix[row][col] - means
    return normalized_rating