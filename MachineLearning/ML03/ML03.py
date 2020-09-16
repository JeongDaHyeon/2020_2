import numpy as np

# return the euclidean distance of two vectors
def euclidean_distance(vec1, vec2):
    return np.sqrt(np.sum((vec1 - vec2) ** 2))

def return_centroid(train_data):
    centroid = np.zeros((3, 4), dtype=np.float32)
    cnt = np.zeros(3)
    for data in train_data:
        centroid[int(data[-1]) - 1] += data[:-1]
        cnt[int(data[-1]) - 1] += 1

    for i in range(len(centroid)):
        centroid[i] /= cnt[i]
    return centroid

def test_the_learning(centroid, test_data):
    cnt = 0
    for data in test_data:
        dist = []
        for c in centroid:
            dist.append(euclidean_distance(c, data[:-1]))
        if dist.index(min(dist)) != (int(data[-1]-1)):
            cnt += 1
    return round((cnt / len(test_data)) * 100, 2)

if __name__ == '__main__':
    train_data = np.loadtxt("data/iris_train.csv", delimiter=',', dtype=np.float32)
    test_data = np.loadtxt("data/iris_test.csv", delimiter=',', dtype=np.float32)

    centroid = return_centroid(train_data)

    print(str(test_the_learning(centroid, test_data)) + "%")