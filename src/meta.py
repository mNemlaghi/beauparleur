from collections import OrderedDict

TITLE = "Beau parleur 🥖🥖🥖 : plateforme d'expérimentation de modèle génératif en langue française"

HEADER1 = "Principes et objectifs"
HEADER2 = "Méthodes de génération"
HEADER3 = "Expérimentons ! "

body = OrderedDict()

body[HEADER1] = []
body[HEADER1].append("Les modèles génératifs sur base des [Transformers](https://fr.wikipedia.org/wiki/Transformeur) ont permis une avancée notable en ce qui concerne la compréhension automatisée du langage. Ceci a permis des innovations de rupture dans plusieurs domaines, notamment dans la qualification de texte. Mais _quid_ du domaine créatif ? C'est ici qu'interviennent les modèles génératifs tels que [GPT](https://openai.com/blog/language-unsupervised/),[GPT-2](https://openai.com/blog/better-language-models/) ou encore le récent - et révolutionnaire - [GPT3](https://arxiv.org/abs/2005.14165).")

body[HEADER1].append("Ces modèles sont pré-entraînés : ceci veut dire que les paramètres qui les déterminent ont déjà été appris par une grande volumétrie de données. Ainsi, libre à l'utilisateur de ce modèle de l'utiliser directement, ou bien de  _spécialiser_ le modèle en ajoutant une couche d'apprentissage supplémentaire (on parle alors de _fine-tuning_)")

body[HEADER1].append("Ceci étant, les modèles génératifs sont biaisés en ce qui concerne les langues traitées. Ainsi, la donnée ayant servi à créer les modèles génératifs GPT est principalement de langue anglaise, ce qui peut avoir tendance à entraver l'adoption de l'intelligence artificielle dans le monde dans le monde.")


body[HEADER1].append("La langue française n'est pas épargnée par une telle prépondérance de la langue anglaise. Notons néanmoins la remarquable initiative [PiaF](https://aclanthology.org/2020.lrec-1.673/), initiative issue de l'[EtaLab](https://www.etalab.gouv.fr/politique-de-la-donnee), plateforme gouvernementale de partage de la donnée.")

body[HEADER1].append("Fort heureusement, la langue française ne se résume pas au territoire hexagonal ! Ainsi Antoine Louis a pré-entraîné un modèle GPT-2 sur près de 60Gb de donnée française et a mis à disposition ce modèle sur Hugging Face. Ce modèle se nomme [BelGPT-2](https://github.com/antoiloui/belgpt2), et c'est celui-ci que nous utiliserons.")


body[HEADER2] = []
body[HEADER2].append("Nous allons explorer 3 méthodes de génération. Les personnes intéressées pourront se référer au [post de blog de Hugging Face sur les modèles génératif](https://huggingface.co/blog/how-to-generate)")
body[HEADER2].append("En bref, un modèle de type GPT2 est __auto-régressif__: conditionnellement à un mot que l'on prononce au sein d'une phrase, le modèle apprend à déterminer le mot suivant le plus probable.")

body[HEADER2].append("Trois méthodes de générations sont possibles à partir de ce modèle")
body[HEADER2].append(" - Une génération _greedy_ : les mots générés sont les mots les plus probables. Cette méthode n'a pas l'avantage de la diversité, car il n'en découle qu'un seul scénario possible.")
body[HEADER2].append(" - Une génération par faisceaux, dite _beam search_ : les mots générés font partie d'une arborescence de mots les plus probables.")
body[HEADER2].append(" - Une génération par échantillonage, ou une génération _sampling_ : On échantillone suivant la loi de probabilité calibrée par le modèle.")

body[HEADER3] = []
body[HEADER3].append("Il est grand temps d'expérimenter la génération et de se laisser entraîner par les différentes propositions")
body[HEADER3].append("⚠️  Suivant les paramètres d'entrée, les textes générés peuvent être vulgaires, voire offensants. Ceux-ci peuvent être instructifs en ce qui concerne toxicité actuelle des discours sur Internet : en effet, la donnée sur laquelle ces modèles sont appris   ⚠️ ")
