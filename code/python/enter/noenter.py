from hidden import lire

class Fichier:
    def ouvrir(self):
        print("j'ouvre un fichier")

    def fermer(self):
        print("je ferme un fichier")

def main():
    fichier = Fichier()
    fichier.ouvrir()
    lire(fichier)
    fichier.fermer()

if __name__ == '__main__':
    main()