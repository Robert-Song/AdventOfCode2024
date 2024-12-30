import numpy as np
if __name__ == '__main__':


    farm = {(1, 2)}
    farm.add((3, 4))

    print(farm)

a = np.array([[1, 2], [3, 5]])
b = np.array([1, 2])
x = np.linalg.solve(a, b)
print(x)