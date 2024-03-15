import numpy as np

def max_pooling(matrix, k):
    m = matrix.shape[0]
    output_size = m - k + 1
    output = np.zeros((output_size, output_size))

    for i in range(output_size):
        for j in range(output_size):
            output[i, j] = np.max(matrix[i:i+k, j:j+k])

    return output

if __name__ == "__main__":
    m = int(input())  # Matrix size
    k = Int(input())  # Window size
    matrix = np.random.randint(0, 10, (m, m))
    print("Input Matrix:\n", matrix)
    output = max_pooling(matrix, k)
    print("Max Pooling Output:\n", output)
