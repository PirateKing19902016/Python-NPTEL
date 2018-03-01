a = [[1, 2], [3,4]]
b = [[1, 0], [0,1]]

zip_b = list(zip(*b))

sum_of_product_of_element, product_of_element = 0, 0
matrix = []
tempRow = []
for row_a in a:
    for col_b in zip_b:
        x = 0
        for ele_a, ele_b in zip(row_a, col_b):

            product_of_element = ele_a * ele_b
            sum_of_product_of_element += product_of_element
        # print(sum_of_product_of_element)
        tempRow.append(sum_of_product_of_element)
        sum_of_product_of_element=0
    # print(tempRow)
    matrix.append(tempRow)
    tempRow = []
print(matrix)
