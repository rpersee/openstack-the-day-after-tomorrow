*Partie IV — L’organisation derrière la plateforme*

# Chapitre 13 — Les droits de décision

Une organisation techniquement compétente peut encore perdre le contrôle si personne ne sait qui a l’autorité de décider.

> **Principe.** Tout le monde peut contester. Quelqu’un doit décider.

L’expertise n’est pas l’autorité. La personne qui a la connaissance technique la plus profonde n’est pas nécessairement celle qui répond de la conséquence métier, et les droits de décision doivent suivre la conséquence. Avant une décision significative, quatre questions doivent avoir une réponse : qui fournit l’évaluation technique, qui est propriétaire de la capacité concernée, qui répond du résultat, et qui a l’autorité de décider. Le décideur ne doit jamais être coupé des preuves. Pendant les incidents, un responsable d’incident désigné coordonne le processus de décision tandis que les experts techniques fournissent l’investigation et les conséquences, et la criticité métier doit être représentée lorsque des actions perturbatrices sont envisagées. Pendant les changements planifiés, la proposition, la validation technique, l’impact opérationnel, la propriété de la capacité, la préparation de la reprise, l’impact sur les consommateurs et l’acceptation du risque doivent tous être visibles. Les équipes techniques évaluent le risque technique. Les propriétaires habilités acceptent le risque métier correspondant.

La chaîne va de l’action à l’autorité :

**Action** → **Responsabilité opérationnelle** → **Propriété de la capacité** → **Responsabilité de la plateforme** → **Conséquence métier** → **Autorité de décision**

La gouvernance n’est complète que lorsque l’autorité finale est visible.

## Les droits de décision doivent être visibles avant l’incident

La pression d’un incident est un mauvais moment pour découvrir qui peut autoriser une action perturbatrice. Pour les capacités OpenStack critiques, l’organisation doit identifier à l’avance qui peut décider de suspendre les API, d’isoler un composant, de redémarrer une dépendance, de prioriser la migration des charges de travail ou d’accepter une dégradation temporaire. Cela ne signifie pas une grande matrice d’approbation. Cela signifie définir le petit nombre de décisions lourdes de conséquences pour lesquelles l’ambiguïté serait dangereuse, et s’assurer que l’autorité du responsable d’incident s’exerce dans des limites prédéfinies : suffisante pour coordonner une action rapide, mais pas absolue au point que les experts techniques ne puissent pas contester une action dangereuse ou que l’impact métier disparaisse du champ de vision.

## L’autorité technique et l’autorité métier sont différentes

Un ingénieur peut être la personne la mieux placée pour déterminer si la réinitialisation d’une dépendance est techniquement sûre. Cela ne fait pas de lui le propriétaire de la conséquence métier de la désactivation d’un service pendant une heure. À l’inverse, un propriétaire métier peut décider qu’une interruption est inacceptable, mais il ne peut pas déterminer si une action technique proposée rétablira le service en sécurité. Une bonne gouvernance relie les deux plutôt que de les fondre en un seul rôle.

## Les droits de décision suivent le domaine de défaillance

Une décision qui touche une charge de travail n’exige pas la même autorité qu’une décision qui touche tout le plan de contrôle. Les droits de décision doivent refléter la conséquence et le rayon d’impact, ce qui permet aux opérations de routine de rester rapides pendant que les actions lourdes de conséquences reçoivent un examen attentif. Les droits de décision doivent aussi survivre aux changements d’organisation : si l’autorité n’existe que parce qu’un manager particulier a toujours pris une certaine décision, le modèle de gouvernance est fragile.

## Fiches, options rejetées et expiration

Les fiches de décision préservent le raisonnement, la responsabilité et le contexte historique, et les options rejetées peuvent avoir autant de valeur que celle qui a été retenue. Si une mise à niveau a été reportée parce que la capacité de reprise était insuffisante, cette raison doit rester visible ; sinon, l’équipe suivante lit le report comme de l’inertie. Les décisions historiques évitent aux organisations de reconsidérer la même question encore et encore sans tirer de leçon de la réponse précédente (l’annexe C fournit une fiche minimale).

L’acceptation d’un risque doit expirer. Un risque accepté aujourd’hui peut ne plus l’être lorsque la criticité métier, la capacité ou l’exposition de sécurité changent, ou lorsqu’une nouvelle version d’OpenStack offre une meilleure solution. L’acceptation doit être assortie d’une condition de revue plutôt que de devenir une autorisation permanente de porter de la dette.

La gouvernance par comité est une tentation à laquelle il faut résister ; je le dis comme une préférence, et les organisations à forte culture du consensus le pèseront différemment. La consultation a de la valeur ; la responsabilité collective devient de l’ambiguïté. Une bonne gouvernance n’empêche pas les gens de décider. Elle s’assure que la bonne personne décide, avec les bonnes preuves, et accepte la bonne conséquence.

---

[← Chapitre 12 — Construire l’équipe derrière la plateforme](12-construire-l-equipe-derriere-la-plateforme.md) · [Sommaire](../README.md) · [Chapitre 14 — Mises à niveau, backports et alignement upstream →](14-mises-a-niveau-backports-et-alignement-upstream.md)
