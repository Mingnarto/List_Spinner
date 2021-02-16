# Soal 2 - List Spinner (30 Poin)
# Buatlah sebuah return function dengan 1 argumen yang dapat memutar list angka (Putaran 1X counter-clockwise) seperti keterangan di bawah ini .

# List Awal
# [[1, 2, 3, 4],
# [5, 6, 7, 8],
# [9, 10, 11, 12],
# [13, 14, 15, 16]]

# Function
# Function Initialization
#  def counterClockwise(...):
#      .....
     
# Use the Function
# print(counterClockwise(List_awal))

# List Output
# [[4, 8, 12, 16]
# [3, 7, 11, 15],
# [2, 6, 10, 14],
# [1, 5, 9, 13]]

print('-'*100)

numb = [[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]]

output = [[],[],[],[]]

def deret(numb):
    x = len(numb)-1

    for i in range(len(numb)):
        for j in range(len(numb)):
            output[i].append(numb[j][x-i])

    return output

print('Output:', deret(numb), '\n')