def copy_file(command_files: str) -> None:
    try:
        count_variable = command_files.split()
        command, file_name_1, file_name_2 = count_variable
        if command == "cp" and f"{file_name_1}" != f"{file_name_2}":
            with (open(file_name_1, "r") as file_in,
                  open(file_name_2, "w") as file_out):
                file_out.write(file_in.read())

    except FileNotFoundError:
        print("file not found")

    except ValueError:
        print("not enough values")
