def rm(file_name, lines_to_remove):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()

        remaining_lines = lines[lines_to_remove:]

        with open(file_name, 'w') as file:
            file.writelines(remaining_lines)

        print(f"Top {lines_to_remove} lines removed. File updated in place.")

    except FileNotFoundError:
        print("File not found. Please provide a valid file name.")
file_name = input("Enter the file name: ")
lines_to_remove = int(input("Enter the number of lines to remove from the top: "))

rm(file_name, lines_to_remove)
