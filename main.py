import numpy as np


def is_legal(array: np.ndarray):
    array_sorted, counts = np.unique(array, return_counts=True, return_index=1)
    if array_sorted[counts > 1].all(0):
        return True
    return False


def n_to_board(n):
    table = np.full((n, n), fill_value=-1)
    table[0] = list(range(n))
    table[:, 0] = list(range(n))

    def n_to_board_aux(table: np.ndarray, array_dict={}):
        out = []
        if not is_legal(table) or not is_legal(table.transpose()):
            return out
        if -1 not in table:
            return [table]
        place = np.unravel_index(np.abs(table - (-1)).argmin(), (n, n))
        for i in range(n):
            table[place] = i
            array_dict[place] = i
            x, y = place
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
                ret = n_to_board_aux(table, array_dict)
                if ret:
                    out.extend(ret)
        return out

    return n_to_board_aux(table=table)


print(*n_to_board(4), sep="\n\n")
