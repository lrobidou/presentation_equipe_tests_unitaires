def add_nb_lines(d: dict[str, int], filenames: list[str]):
    """Add number of line of every file in d."""
    for filename in filenames:
        try:
            with open(filename, 'r') as fichier:
                number_of_line :int = 0
                for _ in fichier:
                    number_of_line += 1
                d[filename] = number_of_line
        except FileNotFoundError as e:
            print(f"{filename} could not be opened")