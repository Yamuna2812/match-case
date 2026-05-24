file = input("Enter file name: ")

match file.split(".")[-1]:
    case "py":
        print("Python File")

    case "txt":
        print("Text File")

    case "jpg":
        print("Image File")

    case "mp3":
        print("Audio File")

    case _:
        print("Unknown File Type")
