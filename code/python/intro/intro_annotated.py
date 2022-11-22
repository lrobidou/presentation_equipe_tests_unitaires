def add_nb_lines(d: dict[str, int], filenames: list[str]):
    for filename in filenames:
        with open(filename, 'r') as fichier:
            n :int = 0
            for _ in fichier:
                n += 1
            d[filename] = n