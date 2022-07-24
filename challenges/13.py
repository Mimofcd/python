board = [
    ["X", "O", "X"],
    [" ", " ", " "],
    ["O", " ", " "],
]
def get_row_col(text):
    tic=text.upper()
    col=tic[0]
    row=int(tic[1])-1
    board_keys={"A":0,"B":1,"C":2}
    for key in board_keys:
        if key==col:
            column=board_keys[key]
            print (row,column)
            return (row,column)
            

get_row_col("C2")
get_row_col("B1")