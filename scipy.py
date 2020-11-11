import numpy as np
from scipy.ndimage import binary_dilation, find_objects, label

def colony(N: int) -> np.ndarray:
    """Replicate bacteria reproduction process to obtain a colony of size N."""
    M = np.zeros((N, N))
    n = (N-1)//2
    M[n, n] = 1 # a bacteria at the center then n reproductions
    return binary_dilation(M, iterations = n).astype(int)

def healthy_test(obj: np.ndarray) -> bool:
    """obj is a square grid of size > 1 AND obj == colony(size)"""
    nb_rows, nb_cols = obj.shape
    return nb_rows == nb_cols > 1 and np.array_equal(obj, colony(nb_rows))

def healthy(grid) -> tuple:
    """Center of the greatest healthy bacteria colony."""
    # 0) Need a numpy array (of ints) to use scipy tools
    m = np.asarray(grid)
    # 1) Distinguish the N parts on the grid.
    labels, N = label(m) # Great job done here! (part 1)
    # 2) Objects are labels[slices] with a little cleaning, with 'center' position.
    # Slices given by find_objects(labels): Great job done here! (part 2)
    cleaning_funcs = (np.vectorize(lambda cell: int(cell == nb))
                      for nb in range(1, N+1)) # keep only cells where is nb
    middle = lambda slice: (slice.start + slice.stop - 1)//2 # slice(3,8) -> 5 middle of 34567
    center = lambda slices: tuple(map(middle, slices))
    objects = ((clean(labels[slices]), center(slices))
               for slices, clean in zip(find_objects(labels), cleaning_funcs))
    # 3) (size, center) for healthy colonies among objects.
    healthy_colonies = ((len(obj), obj_center) for obj, obj_center in objects
                                               if healthy_test(obj))
    return max(healthy_colonies, default=(0,(0,0)))[1]