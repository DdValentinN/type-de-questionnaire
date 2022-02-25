def demander_reponse_numerique_utlisateur(min, max):
    reponse_str = input("Votre réponse (entre " + str(min) + " et " + str(max) + ") :")
    try:
        reponse_int = int(reponse_str)
        if min <= reponse_int <= max:
            return reponse_int

        print("ERREUR : Vous devez rentrer un nombre entre", min, "et", max)
    except:
        print("ERREUR : Veuillez rentrer uniquement des chiffres")
    return demander_reponse_numerique_utlisateur(min, max)


def poser_question(question):
    choix = question[1]
    bonne_reponse = question[2]
    print("QUESTION")
    print("  " + question[0])
    for i in range(len(choix)):
        print("  ", i + 1, ")", choix[i])

    print()
    reponse_int = demander_reponse_numerique_utlisateur(1, len(choix))
    if choix[reponse_int - 1].lower() == bonne_reponse.lower():
        print("Bonne réponse ! ")
        print()
        return True
    else:
        print("Mauvaise réponse...")

    print()
    return False

score = 0
def lancer_questionnaire(questionnaire):
    score=0
    for question in questionnaire:
        if poser_question(question):
            score +=1
    print("Score final :", score, "sur", len(questionnaire))


questionnaire = [
    ("Quelle est la meilleure ambiance de France ?", ("Marseille", "Nice", "Paris", "Lens", "Lille"), "Lens"),
    ("Quelle est la capitale de la Croatie ?", ("Rome", "Bohn", "Zagreb", "Milik"), "Zagreb"),
    ("Quelle est la capitale de la Belgique ?", ("Anvers", "Bruxelles", "Bruges", "Liège"), "Bruxelles")
                ]

lancer_questionnaire(questionnaire)



