def write_file(file_name, file_content):
   with open(f"{file_name}.txt", mode="w") as file_obj:
       file_obj.write(file_content)

def append_file(file_name, append_content):
    with open(f"{file_name}.txt", mode="a") as file_obj:
        file_obj.write(append_content)

def read_file(file_name):
    with open(f"{file_name}.txt" , mode="r") as file_obj:
        return file_obj.read()