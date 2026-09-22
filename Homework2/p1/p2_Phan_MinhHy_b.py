def parse_functions(read_file: str):
    """This parse fucntion works by returning function information sorted alphabetically by name.
    Returns:
        A bunch of tuples containing each function's original line number, name, parameters as text, and signature and body with blank lines and comments removed.
    """
    source_file = None
    try:
        source_file = open(read_file, "r")

        function_list = []
        line_count = 0
        definition_line = 0
        function_name = ""
        parameters = ""
        function_code = ""

        for current_line in source_file:
            # This would count the line number
            line_count = line_count + 1
            #This would remove the comments
            current_line = current_line.split("#")[0]
            #this remove the empty lines
            if current_line.strip() == "":
                continue
            if current_line[0] not in " \t":
                if function_name != "":
                    function_list.append(
                        [function_name, definition_line,
                         parameters, function_code]
                    )

                    function_name = ""
                    parameters = ""
                    function_code = ""

                if current_line[:4] == "def ":
                    definition_line = line_count
                    header_parts = current_line[4:].split("(")
                    function_name = header_parts[0].strip()
                    parameters = header_parts[1].split(")")[0]
                    function_code = current_line

                    if function_code[-1:] != "\n":
                        function_code = function_code + "\n"

            elif function_name != "":
                function_code = function_code + current_line

                if current_line[-1:] != "\n":
                    function_code = function_code + "\n"

        if function_name != "":
            function_list.append(
                [function_name, definition_line,
                 parameters, function_code]
            )

        source_file.close()
        source_file = None
        function_list.sort()
        parsed_result = ()
        #order of the tuple
        for function_record in function_list:
            function_tuple = (
                function_record[1],  # Element 0: definition line number
                function_record[0],  # Element 1: function name
                function_record[2],  # Element 2: argument list string
                function_record[3]   # Element 3: signature and body string
            )

            # This would build the tuple of tuples to be returned.
            parsed_result = parsed_result + (function_tuple,)
        return parsed_result

    #In case of an error
    except Exception:
        if source_file != None:
            source_file.close()
        print("Unable to read or parse the file. Please check the filename and file contents, manager bud.")
        raise

def main():
    """This will parse the file in problem 1 part a"""
    parsed_result = parse_functions("p2_Phan_MinhHy_a.py")
    print(parsed_result)
    print("Name: Minh Hy Phan")
    print("Student ID: Z23766758")

main()