# Créer la classe 'Livre’ qui prend en attributs privés un titre, un auteur et un nombre de
# pages.
# Créer les assesseurs et mutateurs nécessaires afin de pouvoir modifier et afficher les
# attributs. Pour changer le nombre de pages, le nombre doit être un nombre entier
# positif sinon la valeur n’est pas changée et un message d’erreur est affiché.

class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self._titre = titre
        self._auteur = auteur
        self._nb_pages = nb_pages

    # Accesseurs
    def get_titre(self):
        return self._titre

    def get_auteur(self):
        return self._auteur

    def get_nb_pages(self):
        return self._nb_pages

    # Mutateurs
    def set_titre(self, nouveau_titre):
        self._titre = nouveau_titre

    def set_auteur(self, nouvel_auteur):
        self._auteur = nouvel_auteur

    def set_nb_pages(self, nouveau_nb_pages):
        if isinstance(nouveau_nb_pages, int) and nouveau_nb_pages > 0:
            self._nb_pages = nouveau_nb_pages
        else:
            print("Erreur : le nombre de pages doit être un entier positif.")

    # Méthode d'affichage
    def __str__(self):
        return f"{self._titre} par {self._auteur}, {self._nb_pages} pages"


# Création d'un livre
livre1 = Livre("Le Seigneur des anneaux", "J.R.R. Tolkien", 1178)

# Affichage des attributs
print(livre1.get_titre())     # Le Seigneur des anneaux
print(livre1.get_auteur())    # J.R.R. Tolkien
print(livre1.get_nb_pages())  # 1178

# Modification des attributs
livre1.set_titre("Le Hobbit")
livre1.set_auteur("J.R.R. Tolkien")
livre1.set_nb_pages(300)

# Affichage des attributs modifiés
print(livre1.get_titre())     # Le Hobbit
print(livre1.get_auteur())    # J.R.R. Tolkien
print(livre1.get_nb_pages())  # 300

# Tentative de modification avec un nombre de pages invalide
livre1.set_nb_pages(-10)  # Affiche "Erreur : le nombre de pages doit être un entier positif."
