def chessBoardCellColor(cell1, cell2):
    list_even = ["B", "D", "F", "H"]
    

    def is_black(cell):
        if (cell[0] in list_even) and (int(cell[1]) % 2 == 0) or (cell[0] not in list_even) and (int(cell[1]) % 2 != 0):
            return True
        return False

    return is_black(cell1) == is_black(cell2)
        


print(chessBoardCellColor('H1', 'H1'))


def chessBoardCellColor_winner(cell1, cell2):
    return (ord(cell1[0]) + int(cell1[1]) )%2 == (ord(cell2[0]) + int(cell2[1]) )%2