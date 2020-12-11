import numpy as np
from copy import deepcopy


def is_legal(array: np.ndarray):
    for row in array:
        row_sorted, counts = np.unique(row, return_counts=True)
        for i in row_sorted[counts > 1]:
            if i != -1:
                return False
    return True


def n_to_board_aux(table: np.ndarray, array_dict, n):
    out = []
    if -1 not in table:
        return [deepcopy(table)]
    place = np.unravel_index(np.abs(table - (-1)).argmin(), (n, n))
    for i in range(n):
        table[place] = i
        if not is_legal(table) or not is_legal(table.transpose()):
            continue
        x, y = place
        array_dict[(x, y)] = i
        for w in range(n):
            xy = i
            if (y, w) in array_dict.keys():
                yw = array_dict[y, w]
                if (xy, w) in array_dict.keys() and (x, yw) in array_dict.keys() \
                        and array_dict[xy, w] != array_dict[x, yw]:
                    continue
            if (w, x) in array_dict.keys():
                wx = array_dict[w, x]
                if (w, xy) in array_dict.keys() and (wx, y) in array_dict.keys() \
                        and array_dict[w, xy] != array_dict[wx, y]:
                    continue
        ret = n_to_board_aux(deepcopy(table), array_dict, n)
        if ret:
            out.extend(ret)
    return out


def n_to_board(n):
    table = np.full((n, n), fill_value=-1)
    table[0] = list(range(n))
    table[:, 0] = list(range(n))
    array_dict = {}
    for i in range(n):
        array_dict[0, i] = i
        array_dict[i, 0] = i
    return n_to_board_aux(table=table, array_dict=array_dict, n=n)


print(*n_to_board(6), sep="\n\n")
