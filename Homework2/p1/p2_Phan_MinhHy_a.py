def line_number(test_1: str, test_2: str):
    """Basically this code copy a text file, placing a line number before each line.
    read_file: name of the text file 1 (to read)
    write_file: name of a text file 2 (to write)
    returns: None cause it's for copying the code, not use for anything else.
    """
    try:
        with open(test_1, "r") as read_file:
            with open(test_2, "w") as write_file:
                number = 1

                # the next loop read each line on by one, copy it and write it in the new file
                for text_line in read_file:
                    new_line = "{}. {}".format(number, text_line)
                    write_file.write(new_line)
                    number = number + 1
    except Exception:
        print("Unable to copy the file. Might want to check the the codes or the files, manager bud.")
        raise
    return

def main():
    """Testing if the code above works correctly. 
    This is by reprinting the whole code at the destination file with line numbers"""
    line_number("p2_Phan_MinhHy_a.py", "p2_Phan_MinhHy_a.py.txt")
    print("Brand new copy of this freshly made code has been created!")

main()
  