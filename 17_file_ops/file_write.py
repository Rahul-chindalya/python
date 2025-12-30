with open("file.txt","w") as file_data:
    # file_data.write("First line\n")
    # file_data.write("Second line\n")
    file_data.writelines(["this is one-1\n","this is two-2\n"])
    file_data.writelines(["this is one-1\n","this is two-2\n"])