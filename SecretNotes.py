
def strings_to_add_in_file(collected_string):
    main_string = str(collected_string)
    with open("text_file.txt", mode="a") as strings_to_add:
        strings_to_add.write("Note \n" + main_string + "\n\n")
