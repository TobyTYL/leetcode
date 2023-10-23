def main():
    with open('x-sudoku.txt')as file:
        sudo_data = file.read().split()

    index = 0
    number = int(sudo_data[index])
    while (number != -1):
        print("*" * 8, "square", str(number), "*" * 8)
        square = [0]*9
        for i in range(9):
            square[i] = [0]*9
            for j in range(9):
                index += 1
                square[i][j] = int(sudo_data[index])
                print(str(square[i][j]), end=" "*2)
            print(" ")
        test_row(square)
        test_columns(square)
        test_main_diag(square)
        test_off_diag(square)

        number = int(sudo_data[index+1])
        index += 1


def test_row(square):
    row_status = [True] * 9

    for i in range(9):
        row_numbers = [0] * 9
        for j in range(9):
            row_numbers[j] = square[i][j]

        for number in range(1, 10):
            if number not in row_numbers:
                row_status[i] = False
    if False not in row_status:
        print("All rows satisfy the requirements!")
    else:
        for i in range(9):
            if row_status[i] == False:
                print("Row", i+1, "violates the requirements!")


def test_columns(square):
    columns_status = [True]*9

    for i in range(9):
        columns_numbers = [0] * 9
        for j in range(9):
            columns_numbers[j] = square[j][i]

        for number in range(1, 10):
            if number not in columns_numbers:
                columns_status[i] = False

    if False not in columns_status:
        print("All columns satisfy the requirements!")
    else:
        for i in range(9):
            if columns_status[i] == False:
                print("Columns", i+1, "violates the requirements!")


def test_main_diag(square):
    main_diag_status = [True] * 9
    main_diag_numbers = [0] * 9
    lst = {}
    for i in range(9):
        main_diag_numbers[i] = square[i][i]

    for i in range(len(main_diag_numbers)):
        if main_diag_numbers[i] not in lst:
            lst[main_diag_numbers[i]] = i
        else:
            main_diag_status[i] = False        

    if False not in main_diag_status:
        print("All main diagonal satisfy the requirements!")
    else:
        for i in range(9):
            if main_diag_status[i] == False:
                print("main diagonal", i + 1, "violates the requirements!")


def test_off_diag(square):
    off_diag_status = [True] * 9
    off_diag_numbers = [0] * 9
    lst = {}
    for i in range(8,-1,-1):
        off_diag_numbers[i] = square[i][8-i]
    print(off_diag_numbers)
    for i in range(8,-1,-1):
        if off_diag_numbers[i] not in lst:
            lst[off_diag_numbers[i]] = i
        else:
            off_diag_status[i] = False     

    if False not in off_diag_status:
        print("All other diagonal satisfy the requirements!")
    else:
        for i in range(9):
            if off_diag_status[i] == False:
                print("Other diagonal", i + 1, "violates the requirements!")


main()
