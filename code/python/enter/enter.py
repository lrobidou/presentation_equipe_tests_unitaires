from hidden import lire

class Fichier:
    def ouvrir(self):
        print("j'ouvre un fichier")

    def fermer(self):
        print("je ferme un fichier")

class Lecteur:
    def __enter__(self):
        self.fichier = Fichier()
        self.fichier.ouvrir()
        return self.fichier

    def __exit__(self, *args, **kwargs):
        self.fichier.fermer()

def nouveau_fichier():
    return Lecteur()

def main():
    with nouveau_fichier() as fichier:
        lire(fichier)

if __name__ == '__main__':
    main()