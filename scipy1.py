from scipy import array_equal
from scipy.ndimage import center_of_mass, find_objects as find, label
from scipy.ndimage import generate_binary_structure as BS, iterate_structure

def healthy(grid, default=(0, 0)):
    labels, num = label(grid) # start with 1
    segments = {i: labels[s] == i for i, s in enumerate(find(labels), 1)}

    def isideal(segment):
        # BS(2, 1): [[0, 1, 0], [1, 1, 1], [0, 1, 0]]
        ideal = iterate_structure(BS(2, 1), (min(segment.shape) - 1) // 2)
        return array_equal(segment, ideal)

    ideals = (i for i in segments if isideal(segments[i]))
    index = max(ideals, key=lambda i: segments[i].shape, default=[])
    return center_of_mass(labels, labels=labels, index=index) or default