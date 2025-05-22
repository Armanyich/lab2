

def shift_down(field, new_row):
    
    print("До сдвига:")
    for row in field:
        print(row)

    rows = len(field)
    if rows == 0:
        result = [new_row]
    else:
        for i in range(rows - 1, 0, -1):
            field[i] = field[i - 1]
        field[0] = new_row[:]
        result = field

    print("После сдвига:")
    for row in result:
        print(row)
    print("-" * 20)

    return result


if __name__ == "__main__":
    field = [
        [1, 1, 1],
        [0, 0, 0],
        [0, 0, 0],
    ]
    new_row = [2, 2, 2]
    shift_down(field, new_row)
