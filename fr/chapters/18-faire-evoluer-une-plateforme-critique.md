*Partie V — Évoluer sans perdre le contrôle*

# Chapitre 18 — Faire évoluer une plateforme critique

L’évolution est nécessaire, et c’est l’un des moments où le contrôle se perd le plus facilement. Une plateforme qui ne change jamais devient difficile à supporter, à sécuriser et à faire évoluer ; une plateforme qui change trop agressivement déstabilise la production et submerge l’organisation. L’évolution part donc de l’état d’exploitation actuel plutôt que de l’architecture cible. L’organisation doit comprendre comment les charges de travail, les dépendances, la reprise et la propriété passeront de là où elles sont à là où elles devraient être, et la direction compte autant que la destination : quels risques doivent diminuer, quelles capacités doivent s’améliorer, quelles dépendances doivent disparaître, à quelle distance d’upstream la plateforme doit rester.

## L’évolution est une suite d’états d’exploitation

Une feuille de route de transformation ne doit pas être une liste de projets techniques. Une mise à niveau, une refonte du réseau, un changement d’outil de déploiement, une migration de stockage ou une réorganisation d’équipe comptent parce qu’ils font passer la plateforme d’un état d’exploitation à un autre, et pour chaque transition l’organisation doit définir ce qui change, ce qui reste protégé, quelle nouvelle capacité est créée, quel risque est introduit et comment elle saura que la transition est terminée. Cela rend la feuille de route opérationnelle plutôt qu’architecturale, et cela fait apparaître la différence entre le séquencement technique et le séquencement du contrôle. Une mise à niveau peut être techniquement possible alors que sa procédure de reprise n’a pas été testée ; la dépendance manquante est le contrôle organisationnel, pas le logiciel. La meilleure séquence est celle qui laisse l’organisation plus capable d’effectuer la transition *suivante*.

Ne transformez pas tout à la fois parce que c’est techniquement possible ; la règle du chapitre 9 contre l’empilement des incertitudes s’applique aux feuilles de route autant qu’aux changements. Le service existant doit être protégé pendant la transformation ; les changements du plan de contrôle et du plan de données peuvent exiger des séquencements différents ; certaines charges de travail exigent une migration à chaud quand d’autres tolèrent un redémarrage. Le périmètre approprié de chaque étape dépend du contrôle que l’organisation possède réellement. Une transformation qui consomme plus de contrôle que l’organisation n’en possède n’est pas contrôlée.

## Les garde-fous avant la notation

Certaines conditions doivent être traitées comme des portes plutôt que comme des dimensions pondérées. Une option doit normalement être rejetée si elle viole une exigence de sécurité ou réglementaire obligatoire, si elle n’a pas de stratégie de reprise crédible à la mesure de ses conséquences, si elle dépasse un impact métier explicitement inacceptable, si elle dépend d’une expertise que l’organisation ne peut ni fournir ni obtenir, ou si elle introduit un rayon d’impact sans limite. La notation ne s’applique qu’aux options qui ont franchi ces portes.

## Un modèle de décision pondéré, appliqué à une situation réaliste

Lorsque plusieurs voies d’évolution restent viables après les portes, un modèle de notation pondérée rend les compromis explicites. C’est le modèle que j’utilise ; ses poids sont illustratifs et doivent changer avec le contexte. Pour montrer ce qu’il décide et ce qu’il ne décide pas, considérons une plateforme dans l’état suivant, qui n’a rien d’inhabituel.

La plateforme exécute une série sortie de maintenance et en retard de deux versions SLURP sur la version courante. Elle porte une douzaine de patchs appliqués localement, dont trois touchent l’ordonnancement de Nova et ont été écrits par un ingénieur parti depuis. La reprise du plan de contrôle a été démontrée une fois, il y a deux ans, par ce même ingénieur. L’équipe est passée de six à quatre personnes au cours de l’année écoulée. Un avis de sécurité affecte la série en production, le correctif upstream n’existe que pour les séries maintenues, et un backport est possible mais non testé. Trois options survivent aux portes : une campagne *immédiate* qui effectue les deux sauts SLURP en un seul programme de maintenance sur un trimestre ; une voie *progressive* qui effectue le premier saut, stabilise et reconstruit la capacité de reprise, puis effectue le second saut six mois plus tard ; et un *report* qui consacre les deux trimestres suivants à retirer les patchs locaux et à reconstruire la reprise avant toute mise à niveau, en portant entre-temps le backport de sécurité. Le report ne franchit la porte de sécurité que parce qu’un backport testé est crédible ; sans cela, l’option serait rejetée avant la notation.

| Dimension (poids) | Immédiate : les deux sauts en un trimestre | Progressive : un saut, stabilisation, second saut | Report : réduire la dette d’abord, mettre à niveau ensuite |
| ------------------------ | :----------: | :----------: | :----------: |
| Valeur métier ou réduction du risque (25 %) | 5 | 4 | 2 |
| Amélioration du contrôle (25 %) | 4 | 4 | 3 |
| Risque de transition (20 %) | 1 | 3 | 4 |
| Complexité opérationnelle (10 %) | 3 | 3 | 4 |
| Cycle de vie et alignement upstream (10 %) | 5 | 4 | 1 |
| Préparation de l’organisation (10 %) | 2 | 3 | 4 |
| **Score pondéré** | **3,45** | **3,60** | **2,95** |

Chaque option est notée de 1 à 5 sur chaque dimension, 5 étant toujours l’extrémité préférable de l’échelle : pour le risque de transition et la complexité opérationnelle, 5 signifie le risque ou la complexité *les plus faibles*. Le score d’une option est la somme des notes de chaque dimension multipliées par leur poids.

Les nombres sont illustratifs, et le tableau est plus utile par ce qu’il montre que par le vainqueur qu’il désigne. L’écart entre la voie immédiate et la voie progressive est assez petit pour tenir dans l’incertitude des notes ; ce qui les sépare, c’est la ligne du risque de transition, et cette note de 1 repose sur un fait précis, à savoir que la reprise n’a été démontrée par personne qui soit encore dans l’équipe. Si un exercice de reprise était mené avec succès le mois prochain, le risque de transition de l’option immédiate passerait à 2 ou 3 et le classement s’inverserait. Le modèle a donc dit à l’organisation ce qu’il faut faire d’abord, et ce n’est pas une mise à niveau : c’est un exercice de reprise. Le report obtient le score le plus bas parce que la plateforme reste non maintenue deux trimestres de plus, mais il obtient le score le plus élevé en préparation, ce qui est le signal honnête que l’équipe est la contrainte. Ce sont les conversations que le modèle existe pour forcer : pourquoi le risque de transition est-il à 1 plutôt qu’à 3, quelles preuves soutiennent la note de préparation, quelle hypothèse est la plus incertaine, quel événement changerait le classement. Une situation dictée par la sécurité peut donner plus de poids à la réduction du risque ; une plateforme qui souffre déjà d’instabilité peut pondérer plus lourdement le risque de transition et l’amélioration du contrôle ; une équipe en plein changement peut devoir augmenter le poids de la préparation. Le modèle est un mécanisme d’aide à la décision et un outil de conversation, pas un calculateur de risque, et il ne l’emporte jamais sur une porte. L’annexe A donne le cadre complet.

## La feuille de route et ses points de décision

Une feuille de route pratique peut s’exprimer en quatre horizons. L’**état actuel** établit les faits, les risques critiques et les contraintes. L’**horizon de contrôle** comble les lacunes qui rendraient la transition suivante dangereuse. L’**horizon de cycle de vie** effectue les mises à niveau, retire la divergence locale et utilise les grands événements de cycle de vie pour simplifier. L’**horizon futur** fait évoluer l’architecture et les capacités d’exploitation une fois que l’organisation est en mesure de les porter. Les horizons sont des dépendances entre capacités plutôt que des dates, et la feuille de route devient *Évaluer* → *Préparer* → *Réévaluer* → *Changer* → *Vérifier* → *Apprendre* → *Préparer la transition suivante*. Une feuille de route pluriannuelle ne peut pas prédire chaque détail technique, mais elle peut définir quand l’organisation réévaluera : après la validation de la reprise, après une extension de capacité, après une version majeure, après le retrait d’une personnalisation clé, après la formation de l’équipe d’exploitation. Si une mise à niveau planifiée doit être déplacée parce que la reprise n’est pas prête, c’est la preuve que le plan est devenu plus exact, pas un échec de planification.

## Un état cible est un état d’exploitation

Une architecture cible est incomplète sans un état d’exploitation cible. L’organisation doit pouvoir décrire comment la nouvelle plateforme sera supervisée, supportée, rétablie et mise à niveau, qui en sera propriétaire, et qui fera chacune de ces choses : qui est propriétaire de Nova, de Neutron, de Cinder et de leurs dépendances, qui peut les rétablir, quelle part de l’expertise est concentrée sur des individus. Une nouvelle plateforme peut exiger d’autres compétences, d’autres horaires d’exploitation, d’autres dispositifs de support et une autre propriété, et si ces changements ne sont ni financés ni organisés, la transformation technique est incomplète. Une cible techniquement élégante mais exploitée par une équipe qui ne la comprend pas n’est pas une cible réussie.

Chaque évolution est aussi le point de départ de la suivante. Une bonne transformation laisse moins de personnalisations inexpliquées, une meilleure reprise, une documentation plus solide et une équipe qui comprend le résultat, de sorte que la prochaine mise à niveau est plus facile grâce à celle-ci. Avant de déclarer une évolution réussie, demandez-vous si la plateforme obtenue est plus compréhensible, plus récupérable et plus exploitable que la précédente : plus d’une personne peut-elle l’exploiter, l’organisation peut-elle expliquer ses dépendances, peut-elle rétablir les capacités critiques, peut-elle suivre la version suivante sans divergence inexpliquée, peut-elle changer sans épuiser sa capacité, l’équipe peut-elle remettre l’architecture en question.

Le test final est celui que le chapitre 1 appliquait au déploiement : l’organisation pourrait-elle exploiter la plateforme obtenue sans les personnes qui l’ont transformée ?

> **Principe.** Une évolution réussie d’OpenStack est une plateforme dont l’avenir peut encore être exploité délibérément, pas simplement une plateforme plus récente.

Les deux chapitres qui suivent ne sont pas des recettes. Ils déroulent des situations dans lesquelles les preuves techniques, l’impact métier et les contraintes opérationnelles sont entrés en collision, et ils montrent comment le cadre se comporte quand la réponse n’est pas évidente. Chacun est raconté selon la même grille :

**Contexte** → **Signal** → **Incertitude** → **Risque métier** → **Options** → **Décision** → **Compromis** → **Résultat** → **Leçon**

Les deux situations sont abstraites d’opérations réelles. Les détails qui permettraient d’identifier un environnement ont été retirés ; l’enchaînement du raisonnement, non.

---

[← Chapitre 17 — La sécurité est un travail de plateforme](17-la-securite-est-un-travail-de-plateforme.md) · [Sommaire](../README.md) · [Chapitre 19 — Quand la décision sûre est de s’arrêter →](19-quand-la-decision-sure-est-de-s-arreter.md)
