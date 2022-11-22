def add_nb_lines(d, filenames):
    for filename in filenames:
        with open(filename, 'r') as fichier:
            n = 0
            for _ in fichier:
                n += 1
            d[filename] = n