with open("file.txt","r") as file_data:
    # print(file_data.read) #read whole line
    # print(file_data.readlines())#Return a list of lines from the stream.
    # print(file_data.readline())#Return a line from the stream.
    # for i in file_data.read():
    #     print(i)

    data = file_data.readlines()
    for i in data:
        print(i.strip())