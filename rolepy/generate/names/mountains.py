import random as rd

class MountainNameGenerator:

    COMMON_NOUN = ["Dôme", "Mont", "Pic", "Piton", "Puy", "Sommet", "Volcan", "Dômes", "Monts", "Pics", "Pitons", "Puys", "Sommets", "Volcans", "Colline", "Crête", "Montagne", "Collines", "Crêtes", "Montagnes"]
    ADJ_MALE = ["Écarlate", "Éclairé", "Énorme", "Épineux", "Érodé", "Éteint", "Éternel", "Éthéré", "Abandonné", "Adamant", "Affamé", "Agitant", "Ancien", "Aphone", "Arctique", "Ardent", "Argenté", "Aride", "Avide", "Barbare", "Blanc", "Boisé", "Brûlant", "Brillant", "Bronze", "Calme", "Carié", "Charmant", "Chatoyant", "Clair", "Contemplatif", "Coupé", "Creux", "Déchiqueté", "Délaissé", "Délicat", "Déserté", "Désintégré", "Désolé", "Dangereux", "Diabolique", "Dominant", "Doré", "Doux", "Effrayant", "Enchanté", "Endormi", "Fâché", "Fabuleux", "Facile", "Faible", "Flétri", "Foncé", "Fracturé", "Froid", "Furieux", "Géant", "Gargantuesque", "Gelé", "Gigantesque", "Glacé", "Gris", "Hanté", "Immense", "Immobile", "Impitoyable", "Importun", "Imposant", "Incolore", "Infini", "Interdit", "Isolé", "Légendaire", "Léger", "Lointain", "Majestueux", "Maudit", "Monstre", "Monstrueux", "Morne", "Mort", "Muet", "Mystérieux", "Neigeux", "Noir", "Nu", "Nul", "Obscur", "Ombragé", "Ombreux", "Orageux", "Ordinaire", "Oublié", "Pâle", "Paisible", "Perpétuel", "Pompeux", "Pourri", "Précaire", "Profond", "Puissant", "Pur", "Raide", "Ravagé", "Redoutable", "Retentissant", "Ridicule", "Robuste", "Rocheux", "Rouge", "Sacré", "Satané", "Sauvage", "Sec", "Seul", "Silencieux", "Sinistre", "Solide", "Solitaire", "Sombre", "Stérile", "Surplombant", "Symétrique", "Tenace", "Titanesque", "Tranquille", "Triste", "Vaste", "Venteux", "Vermeil", "Vide", "Violent", "Volatil", "Volcanique", "d'Or", "de Diamant", "de Neige", "de l'Est", "de l'Ouest", "du Nord", "du Sud", "en Terrasse", "Glacial", "Oriental", "Occidental", "Colossal", "Brutal", "Boréal", "Austral", "Infernal", "Craignait", "Évasement", "Hivernal"]
    ADJ_FEMALE = ["Écarlate", "Éclairée", "Énorme", "Épineuse", "Érodée", "Éteinte", "Éternelle", "Éthérée", "Abandonnée", "Adamante", "Affamée", "Agitant", "Ancienne", "Aphone", "Arctique", "Ardente", "Argentée", "Aride", "Avide", "Barbare", "Blanche", "Boisée", "Brûlante", "Brillante", "Bronze", "Calme", "Carié", "Charmante", "Chatoyante", "Claire", "Contemplative", "Coupée", "Creuse", "Déchiquetée", "Délaissée", "Délicate", "Désertée", "Désintégrée", "Désolée", "Dangereuse", "Diabolique", "Dominante", "Dorée", "Douce", "Effrayante", "Enchantée", "Endormie", "Fâchée", "Fabuleuse", "Facile", "Faible", "Flétrie", "Foncée", "Fracturée", "Froide", "Furieuse", "Géante", "Gargantuesque", "Gelée", "Gigantesque", "Glacée", "Grise", "Hantée", "Immense", "Immobile", "Impitoyable", "Importune", "Imposante", "Incolore", "Infinie", "Interdite", "Isolée", "Légendaire", "Légère", "Lointaine", "Majestueuse", "Maudite", "Monstre", "Monstrueuse", "Morne", "Morte", "Muette", "Mystérieuse", "Neigeuse", "Noire", "Nue", "Nulle", "Obscure", "Ombragée", "Ombreuse", "Orageuse", "Ordinaire", "Oubliée", "Pâle", "Paisible", "Perpétuelle", "Pompeuse", "Pourrie", "Précaire", "Profonde", "Puissante", "Pure", "Raide", "Ravagée", "Redoutable", "Retentissante", "Ridicule", "Robuste", "Rocheuse", "Rouge", "Sacrée", "Satanée", "Sauvage", "Sèche", "Seule", "Silencieuse", "Sinistre", "Solide", "Solitaire", "Sombre", "Stérile", "Surplombante", "Symétrique", "Tenace", "Titanesque", "Tranquille", "Triste", "Vaste", "Venteuse", "Vermeille", "Vide", "Violente", "Volatile", "Volcanique", "d'Or", "de Diamant", "de Neige", "de l'Est", "de l'Ouest", "du Nord", "du Sud", "en Terrasse", "Glacial", "Oriental", "Occidental", "Colossal", "Brutal", "Boréal", "Austral", "Infernal", "Craignait", "Hivernal", "Évasement"]
    PROPER_NOUN_PREFIX = ["Épi", "Auri", "Avi", "Angou", "Hague", "Houi", "Anti", "Anto", "Or", "Alen", "Argen", "Auber", "Bel", "Besan", "Bor", "Bour", "Cam", "Char", "Cler", "Col", "Cour", "Mar", "Mont", "Nan", "Nar", "Sar", "Valen", "Vier", "Villeur", "Vin", "Ba", "Bé", "Beau", "Berge", "Bou", "Ca", "Carca", "Cha", "Champi", "Cho", "Cla", "Colo", "Di", "Dra", "Dragui", "Fré", "Genne", "Go", "Gre", "Leva", "Li", "Mai", "Mari", "Marti", "Mau", "Montau", "Péri", "Pa", "Perpi", "Plai", "Poi", "Pu", "Roa", "Rou", "Sau", "Soi", "Ta", "Tou", "Va", "Vitro"]
    PROPER_NOUN_SUFFIX = ["gnan", "gnane", "gneux", "llac", "lles", "lliers", "llon", "lly", "nne", "nnet", "nnois", "ppe", "ppes", "rgues", "ssion", "ssis", "ssonne", "ssons", "ssy", "thune", "çon", "béliard", "bagne", "beuge", "bonne", "ciennes", "court", "fort", "gny", "gues", "gueux", "lès", "lême", "let", "limar", "logne", "lon", "luçon", "luire", "lun", "mans", "mart", "masse", "miers", "momble", "mont", "mur", "nau", "nesse", "nin", "noît", "rac", "rault", "ris", "roux", "sart", "seau", "sier", "sir", "teaux", "toise", "tou", "veil", "vers", "ves", "ville", "vin", "yonne", "zieu", "zon"];

    def get():
        if rd.random() < .5:
            word = rd.choice(MountainNameGenerator.PROPER_NOUN_PREFIX) + rd.choice(MountainNameGenerator.PROPER_NOUN_SUFFIX)
            if word[-1].lower() == "s":
                determiner = ["des "]
            elif word[0].lower() in "aéèeiouy":
                determiner = ["d'", "de l'"]
            else:
                determiner = ["de ", "du ", "de la "]
            return rd.choice(MountainNameGenerator.COMMON_NOUN) + " " + rd.choice(determiner) + word
        else:
            common_noun_index = rd.randint(0, len(MountainNameGenerator.COMMON_NOUN) - 1)
            name = MountainNameGenerator.COMMON_NOUN[common_noun_index] + " "
            if common_noun_index < 14:
                name += rd.choice(MountainNameGenerator.ADJ_MALE)
            else:
                name += rd.choice(MountainNameGenerator.ADJ_FEMALE)
            if rd.random() < .5 and name[-1] not in ["s", "x"]:
                return name + "s"
            return name
