def index(filename, k):
    data = set()
    with open(filename, 'r') as fichier:
        for ligne in fichier:
            for i in range(len(ligne)-k+1):
                data.add(ligne[i:i+k])
    return data

def query(filename, k, data):
    presence = []
    with open(filename, 'r') as fichier:
        for ligne in fichier:
            for i in range(len(ligne)-k+1):
                presence.append(ligne[i:i+k] in data)
    return presence


def main():
    data = index("reads.txt", 31)
    # print(data)
    print(len(query("reads.txt", 31, data)))

if __name__ == "__main__":
    main()