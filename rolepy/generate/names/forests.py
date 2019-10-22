import random as rd


class ForestNameGenerator:
    """Contains word bits for the generation of forest names."""

    ADJ_FEMALE_LEFT = ["Douce", "Fausse", "Grande",
                       "Jeune", "Longue", "Petite", "Vaste"]
    ADJ_MALE_LEFT = ["Doux", "Faux", "Grands",
                     "Jeunes", "Longs", "Petits", "Vastes"]
    ADJ_FEMALE_RIGHT = ["Épaisse", "Éternelle", "Éthérée", "Abandonnée",
                        "Antique", "Arctique", "Aride", "Blanche", "Brillante",
                        "Brisée", "Brumeuse", "Céleste", "Cachée", "Chuchotante",
                        "Colossale", "Corrompue", "Creuse", "Cruelle", "Déformée",
                        "d'Émeraude", "d'Épinettes", "d'Érables", "d'Argent", "d'Aulnes",
                        "d'Effroi", "d'Obsidienne", "d'Onyx", "d'Or", "d'Ormes",
                        "de Blaireaux", "de Bouleaux", "de Brume", "de Cèdres",
                        "de Cendres", "de Cerfs", "de Châtaigniers", "de Chêne",
                        "du Courage", "de Cristal", "de Cuivre", "de Cyprès", "de Faucons",
                        "de Fer", "de Hêtres", "de Jade", "de l'Ancien", "de l'Est",
                        "de l'Ombre", "de l'Ouest", "de la Bête", "de la Couronne",
                        "de la Liberté", "de la Lune", "de la Mort", "de la Rédemption",
                        "de la Soie", "de la Terreur", "de la Victoire", "de la Violette",
                        "de Marbre", "de Myrtilles", "de Naissance", "de Noisettes",
                        "de Peupliers", "de Pins", "de Pivert", "de Plumes", "de Rêve",
                        "de Requiem", "de Séquoia", "de Saules", "de Serpent", "des Écureuils",
                        "des Aigles", "des Araignées", "des Bêtes", "des Blaireaux",
                        "des Castors", "des Chacals", "des Chagrins", "des Coyotes",
                        "des Fantômes", "des Fleurs", "des Géants", "des Hérissons",
                        "des Hiboux", "des Hirondelles", "des Loups", "des Oiseaux",
                        "des Ours", "des Phacochères", "des Rêves", "des Renards",
                        "Douce", "du Champion", "du Chaos", "du Diable", "du Miracle",
                        "du Nord", "du Serpent", "du Soleil", "du Sud", "du Tonnerre",
                        "Durable", "en Évolution", "Enchantée", "Endormie", "Fantôme",
                        "Folle", "Froide", "Frontalière", "Géante", "Gargantuesque",
                        "Gelée", "Grossière", "Hantée", "Imposante", "Inconnue",
                        "Infinie", "Isolée", "Jumelle", "Légère", "Libre", "Lumineuse",
                        "Luxuriante", "Méchante", "Maléfique", "Merveilleuse", "Mineure",
                        "Misérable", "Morte", "Mystérieuse", "Nocturne", "Noire", "Nuageuse",
                        "Océanique", "Orageuse", "Pâle", "Parfumée", "Perdue", "Pittoresque",
                        "Planaire", "Primaire", "Puissante", "Radiante", "Royale",
                        "Sanctifiée", "Sereine", "Silencieuse", "Sinistre", "Sombre",
                        "Spirituelle", "Suprême", "Tonnante", "Tranquille", "Unie",
                        "Venteuse", "Verdoyante", "Vibrante", "Vierge", "Volatile"]
    ADJ_MALE_RIGHT = ["Épais", "Éternels", "Éthérés", "Abandonnés", "Antiques",
                      "Arctiques", "Arides", "Blancs", "Brillants", "Brisés",
                      "Brumeux", "Célestes", "Cachés", "Chuchotants", "Colossaux",
                      "Corrompus", "Creux", "Cruels", "Déformés", "d'Émeraude",
                      "d'Épinettes", "d'Érables", "d'Argent", "d'Aulnes", "d'Effroi",
                      "d'Obsidienne", "d'Onyx", "d'Or", "d'Ormes", "de Blaireaux",
                      "de Bouleaux", "de Brume", "de Cèdres", "de Cendres", "de Cerfs",
                      "de Châtaigniers", "de Chêne", "du Courage", "de Cristal",
                      "de Cuivre", "de Cyprès", "de Faucons", "de Fer", "de Hêtres",
                      "de Jade", "de l'Ancien", "de l'Est", "de l'Ombre", "de l'Ouest",
                      "de la Bête", "de la Couronne", "de la Liberté", "de la Lune",
                      "de la Mort", "de la Rédemption", "de la Soie", "de la Terreur",
                      "de la Victoire", "de la Violette", "de Marbre", "de Myrtilles",
                      "de Naissance", "de Noisettes", "de Peupliers", "de Pins",
                      "de Pivert", "de Plumes", "de Rêve", "de Requiem", "de Séquoia",
                      "de Saules", "de Serpent", "des Écureuils", "des Aigles",
                      "des Araignées", "des Bêtes", "des Blaireaux", "des Castors",
                      "des Chacals", "des Chagrins", "des Coyotes", "des Fantômes",
                      "des Fleurs", "des Géants", "des Hérissons", "des Hiboux",
                      "des Hirondelles", "des Loups", "des Oiseaux", "des Ours",
                      "des Phacochères", "des Rêves", "des Renards", "Doux",
                      "du Champion", "du Chaos", "du Diable", "du Miracle",
                      "du Nord", "du Serpent", "du Soleil", "du Sud", "du Tonnerre",
                      "Durables", "en Évolution", "Enchantés", "Endormis", "Fantômes",
                      "Fou", "Froids", "Frontaliers", "Géants", "Gargantuesques",
                      "Gelés", "Grossiers", "Hantés", "Imposants", "Inconnus",
                      "Infinis", "Isolés", "Jumeaux", "Légers", "Libres", "Lumineux",
                      "Luxuriants", "Méchants", "Maléfiques", "Merveilleux", "Mineurs",
                      "Misérables", "Morts", "Mystérieux", "Nocturnes", "Noirs", "Nuageux",
                      "Océaniques", "Orageux", "Pâles", "Parfumés", "Perdus", "Pittoresques",
                      "Planaires", "Primaires", "Puissants", "Radiants", "Royals",
                      "Sanctifiés", "Sereins", "Silencieux", "Sinistres", "Sombres",
                      "Spirituels", "Suprêmes", "Tonnants", "Tranquilles", "Unis",
                      "Venteux", "Verdoyants", "Vibrants", "Vierges", "Volatils"]
    COMMON_NOUN = ["Forêt", "Bois"]
    DETERMINER = []
    PROPER_NOUN_PREFIX = ["Épi", "Auri", "Avi", "Angou", "Anti", "Anto", "Or",
                          "Alen", "Argen", "Auber", "Bel", "Besan", "Bor", "Bour",
                          "Cam", "Char", "Cler", "Col", "Cour", "Mar", "Mont",
                          "Nan", "Nar", "Sar", "Valen", "Vier", "Villeur", "Vin",
                          "Ba", "Bé", "Beau", "Berge", "Bou",
                          "Ca", "Carca", "Cha", "Champi", "Cho", "Cla", "Colo",
                          "Di", "Dra", "Dragui", "Fré", "Genne", "Go", "Gre",
                          "Hague", "Houi", "Leva", "Li", "Mai", "Mari", "Marti",
                          "Mau", "Montau", "Péri", "Pa", "Perpi", "Plai", "Poi",
                          "Pu", "Roa", "Rou", "Sau", "Soi", "Ta", "Tou", "Va", "Vitro"]
    PROPER_NOUN_SUFFIX = ["gnan", "gnane", "gneux", "llac", "lles", "lliers",
                          "llon", "lly", "nne", "nnet", "nnois", "ppe", "ppes",
                          "rgues", "ssion", "ssis", "ssonne", "ssons", "ssy",
                          "thune", "çon", "béliard", "bagne", "beuge", "bonne",
                          "ciennes", "court", "fort", "gny", "gues", "gueux",
                          "lès", "lême", "let", "limar", "logne", "lon", "luçon",
                          "luire", "lun", "mans", "mart", "masse", "miers", "momble",
                          "mont", "mur", "nau", "nesse", "nin", "noît", "rac",
                          "rault", "ris", "roux", "sart", "seau", "sier", "sir",
                          "teaux", "toise", "tou", "veil", "vers", "ves", "ville",
                          "vin", "yonne", "zieu", "zon"]


def get_forest_name(seed):
    """Generate a random forest name."""
    rd.seed(seed)
    mode = rd.randint(1, 8)
    if mode <= 4:
        word = rd.choice(ForestNameGenerator.PROPER_NOUN_PREFIX) + \
            rd.choice(ForestNameGenerator.PROPER_NOUN_SUFFIX)
        if word[-1].lower() == "s":
            determiner = ["des "]
        elif word[0].lower() in "aéèeiouy":
            determiner = ["d'", "de l'"]
        else:
            determiner = ["de ", "du ", "de la "]
        return rd.choice(ForestNameGenerator.COMMON_NOUN) + " " + rd.choice(determiner) + word
    if mode == 5:
        return "" + rd.choice(ForestNameGenerator.ADJ_FEMALE_LEFT) + " Forêt"
    if mode == 6:
        return "" + rd.choice(ForestNameGenerator.ADJ_MALE_LEFT) + " Bois"
    if mode == 7:
        return "Forêt " + rd.choice(ForestNameGenerator.ADJ_FEMALE_RIGHT)
    return "Bois " + rd.choice(ForestNameGenerator.ADJ_MALE_RIGHT)
