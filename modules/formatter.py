def display_as_python_tuple(area_codes_map: dict) -> None:
    variable_name = "us_area_codes_tuple = ( "
    spacing = " " * len(variable_name)

    # print initial variable_name
    print(variable_name, end="")
    for i, (state, area_codes_list) in enumerate(area_codes_map.items()):
        # Pr
        if i == 0:
            print(f"# {state}\n{spacing}", end="")
        else:
            print(f"{spacing}# {state}\n{spacing}", end="")
        
        breakline = 10
        for j, area_code  in enumerate(area_codes_list):
            # Separate elements by comma unless it is the last
            # element in the map itself
            if i < len(area_codes_map)-1:
                print(f"{area_code}", end=", ")
            else:
                print(f"{area_code}", end="")

            # Split elements by lines of 10 elements
            if breakline == 1 and j != len(area_codes_list)-1:
                print(f"\n{spacing}", end="")
                breakline = 10
            else:
                breakline -= 1

            # If element is final element in map, print ending parenthesis
            if i == len(area_codes_map)-1 and j == len(area_codes_list)-1:
                print(" )")
            # If element is final element in list, print newline
            elif j == len(area_codes_list)-1:
                print("")
