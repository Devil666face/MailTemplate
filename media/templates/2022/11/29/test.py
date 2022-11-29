string = "уацуацуа"
# string with encoding 'utf-8'
arr = bytes(string, 'utf-8')
arr2 = bytes(string, 'ascii')

with open('test.txt', 'wb') as file:
    file.write(arr)
