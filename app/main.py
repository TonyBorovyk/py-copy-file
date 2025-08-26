import os


def copy_file(command_files: str) -> None:
    parts = command_files.split()
    if len(parts) == 3 and parts[0] == "cp":

        command, file_name_1, file_name_2 = parts
        if (os.path.isfile(file_name_1)
                and f"{file_name_1}" != f"{file_name_2}"):

            with (open(file_name_1, "r") as file_in,
                    open(file_name_2, "w") as file_out):

                file_out.write(file_in.read())
