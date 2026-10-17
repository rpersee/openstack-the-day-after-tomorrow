*Annexes*

# Annexe A — Le cadre de décision du contrôle

Le cadre vise à rendre le jugement opérationnel explicite sans prétendre que les décisions complexes se réduisent à une formule. Une décision importante peut être structurée comme suit ; la structure doit s’alléger pour les décisions de routine et devenir plus explicite à mesure que la conséquence grandit.

1. **Situation** — Que se passe-t-il ?
2. **Objectif métier** — Que cherchons-nous à protéger, à rétablir ou à améliorer ?
3. **Preuves** — Que savons-nous réellement ?
4. **Incertitude** — Qu’est-ce qui reste non démontré ?
5. **Contraintes** — Qu’est-ce qui limite les options disponibles ?
6. **Impact métier** — Que se passe-t-il si la situation se dégrade ?
7. **Options** — Quelles actions réalistes sont disponibles ?
8. **Compromis** — Quel risque et quelle complexité chaque option introduit-elle ?
9. **Droits de décision** — Qui fournit les preuves, qui est propriétaire de la capacité, qui accepte la conséquence, qui décide ?
10. **Action contrôlée** — Comment l’option retenue sera-t-elle exécutée ?
11. **Vérification** — Comment le succès et les effets non voulus seront-ils établis ?
12. **Apprentissage** — Que faut-il changer à la lumière du résultat ?

## Portes de décision

La notation pondérée ne doit jamais l’emporter sur les contraintes fondamentales de sûreté. Avant de noter, vérifier que chaque option a un impact métier acceptable, un chemin de reprise crédible, des preuves techniques suffisantes, un propriétaire défini, une autorité de décision appropriée, un rayon d’impact borné, et qu’elle ne viole aucune exigence obligatoire de sécurité ou de réglementation. Si l’un de ces éléments manque, améliorer la situation avant de comparer les options.

## Modèle de notation pondérée

Lorsque plusieurs options restent crédibles après les portes, un modèle pondéré structure la comparaison. Six dimensions sont notées de 1 à 5 pour chaque option, 5 étant toujours l’extrémité préférable de l’échelle (pour le risque de transition et la complexité opérationnelle, 5 signifie le plus faible), et chaque note est multipliée par le poids de la dimension : valeur métier ou réduction du risque (25 %), amélioration du contrôle (25 %), risque de transition (20 %), complexité opérationnelle (10 %), cycle de vie et alignement upstream (10 %) et préparation de l’organisation (10 %). Le résultat se situe entre 1 et 5. Les poids de référence sont indicatifs et doivent changer avec le contexte : une décision motivée par la sécurité peut donner plus de poids à la réduction du risque, une plateforme instable peut donner plus de poids au risque de transition, une équipe en transition peut donner plus de poids à la préparation. Le chapitre 18 déroule un exemple complet sur une situation réaliste, où le modèle désigne un exercice de reprise plutôt qu’une mise à niveau.

Quel que soit le résultat, les questions qui comptent sont : pourquoi le risque de transition est-il noté 1 plutôt que 3 ? Quelles preuves soutiennent la note de préparation ? Quelle hypothèse est la plus incertaine ? Quel événement changerait le classement ? Existe-t-il une contrainte non négociable qui rejette une option quelle que soit sa note ?

## Le modèle est un outil de conversation

La plus grande valeur de la notation pondérée n’est pas le chiffre final, mais le désaccord rendu visible. Deux ingénieurs peuvent s’accorder sur les options et diverger fortement sur le risque de transition. Un propriétaire métier peut attribuer à une charge de travail une criticité plus élevée que l’équipe plateforme ne l’attendait. Un responsable de plateforme peut voir qu’une option techniquement séduisante crée une divergence excessive de cycle de vie. Le modèle force ces différences à s’exprimer, et il facilite la revue ultérieure : quand la décision est réexaminée après un incident, une mise à niveau ou un changement d’équipe, l’organisation peut identifier quelles hypothèses ont changé plutôt que de repartir de mémoire.

***Les bonnes décisions ne sont pas des décisions sans incertitude. Ce sont des décisions dans lesquelles l’incertitude, la conséquence et la responsabilité sont rendues visibles.***

---

[← Conclusion : garder OpenStack sous contrôle](../chapters/21-conclusion-garder-openstack-sous-controle.md) · [Sommaire](../README.md) · [Annexe B — La fiche d’évaluation du contrôle →](annexe-b-la-fiche-d-evaluation-du-controle.md)
