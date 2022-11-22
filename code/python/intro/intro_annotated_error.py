def add_nb_lines(d: dict[str, int], filenames: list[str]):
    for filename in filenames:
        try:
            with open(filename, 'r') as fichier:
                n :int = 0
                for _ in fichier:
                    n += 1
                d[filename] = n
        except FileNotFoundError as e:
            print(f"{filename} could not be opened")