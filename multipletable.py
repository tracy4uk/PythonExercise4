def show_multiplication_table(max_value):

    table_str =""
    for i in range(1, max_value + 1):
        for j in range(1, max_value + 1):
            table_str += f"{i * j:4}"
        table_str += "\n"

    return table_str

multiplication_table = show_multiplication_table(12)
print(multiplication_table)

