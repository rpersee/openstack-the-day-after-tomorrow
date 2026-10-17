*Partie II — Évaluer le contrôle*

# Chapitre 6 — Mesurer le contrôle

La mesure doit porter sur la capacité, pas sur l’activité. Le nombre de tickets, de tableaux de bord, de changements, d’automatisations et de documents décrit une activité sans prouver le contrôle. La meilleure question est de savoir si l’organisation est devenue plus capable, et cela s’examine capacité par capacité.

Pour la **visibilité**, mesurer combien de capacités critiques sont couvertes par une observabilité qui a du sens, combien de temps prend la détection, et combien d’événements récurrents restent inexpliqués. Pour la **stabilité**, examiner la récurrence des incidents, la marge de capacité, le recours à la dégradation contrôlée et la fréquence à laquelle la reprise exige de l’improvisation. Pour l’**organisation**, examiner les dépendances à un expert unique, le temps d’intégration, la couverture du transfert de connaissances, les lacunes de propriété et la concentration de la charge opérationnelle. Pour la **gouvernance**, mesurer si les décisions importantes ont des décideurs clairs, une acceptation explicite du risque et un raisonnement consigné. Trois mesures transversales comptent autant : pour la **reprise**, la proportion de capacités critiques dont la reprise a été démontrée, le taux de succès et la durée des reprises, et le nombre de dépendances incluses dans la validation de la reprise ; pour la **qualité du changement**, si les changements importants ont des stratégies de reprise crédibles, un risque explicite, des conditions d’arrêt et une vérification après changement ; pour l’**alignement upstream**, le nombre de modifications locales significatives, le statut de maintenance de la série en production, et l’effort nécessaire pour réconcilier les modifications locales à chaque mise à niveau.

## Les mesures que la plateforme peut produire elle-même

La plupart de ces mesures sont organisationnelles et doivent être collectées à la main. Certaines peuvent être lues dans OpenStack, et celles-là méritent une place dans la revue parce qu’elles ne dépendent de la mémoire de personne : le nombre d’hôtes dont le service compute est désactivé, et pourquoi ; le nombre d’allocations que Placement détient pour des instances qui n’existent plus, rapporté par `nova-manage placement audit` ; le nombre d’instances restées en BUILD, en ERROR ou dans un état de suppression depuis plus d’un jour ; l’âge de la série en production par rapport à son statut de maintenance sur releases.openstack.org ; le nombre de patchs portés localement dans le dépôt de déploiement ; la date du dernier exercice de reprise pour chaque composant partagé. Aucune de ces mesures n’est un score de contrôle. Chacune est un fait qui rend plus difficile d’éviter une conversation sur le contrôle.

## Pas de score unique

Aucun score de contrôle unique ne doit devenir l’objectif. Un score masque les différences : une organisation peut avoir une excellente observabilité et une reprise médiocre, et les combiner en un seul nombre dissimule la faiblesse. Les tendances comptent plus que les valeurs absolues. La question utile est de savoir si chaque capacité se renforce ou s’affaiblit avec le temps, et la mesure doit conduire à des décisions : si la dépendance à un expert unique augmente, la réponse peut être un transfert de connaissances ; si la couverture de la reprise baisse, les exercices de reprise deviennent une priorité ; si la divergence upstream grandit, la prochaine mise à niveau doit inclure une simplification.

## Les métriques ont besoin d’un décideur

Une métrique utile est reliée à une action. Si les échecs récurrents d’ordonnancement de Nova augmentent, quelqu’un doit savoir qui enquête et qui décide si la réponse est un réglage, une extension de capacité, la correction d’un défaut ou une mise à niveau. Si la couverture de la reprise baisse parce qu’une dépendance a changé, la métrique doit déclencher une revue. Sans décideur, une métrique n’est qu’un élément de plus sur un tableau de bord.

## Mesurer la concentration de la capacité

L’une des mesures opérationnelles les plus révélatrices n’est pas technique du tout : à quel point la connaissance critique est-elle concentrée ? Si un ingénieur est la seule personne capable de diagnostiquer un problème de routage Neutron, l’organisation a une dépendance mesurable ; si trois personnes peuvent exécuter la reprise de façon indépendante, la dépendance est nettement plus faible. Cela se mesure mieux par la démonstration que par la déclaration. Il en va de même pour la capacité de changement : si une seule personne peut exécuter une mise à niveau donnée, la mise à niveau est un goulet d’étranglement organisationnel autant qu’une tâche technique.

## Mesurer le coût de l’incertitude, et surveiller les indicateurs avancés

Les incidents récurrents qui restent inexpliqués méritent une attention particulière. Un incident résolu rapidement mais jamais compris peut être plus dangereux qu’un incident plus long qui a produit une connaissance durable, parce que le premier consomme de la capacité de façon répétée. Une tendance utile est la proportion d’événements récurrents pour lesquels l’organisation dispose d’une explication documentée, d’une mesure d’atténuation et d’un propriétaire ; elle relie directement la mesure à l’apprentissage.

Certaines mesures décrivent les défaillances après qu’elles se sont produites. D’autres montrent que l’organisation devient moins préparée : le nombre de capacités critiques pour lesquelles un seul ingénieur a la connaissance, ou le nombre de procédures de reprise qui n’ont pas été exercées récemment. Ces indicateurs avancés peuvent avoir plus de valeur que le nombre d’incidents, parce qu’ils exposent l’affaiblissement d’une capacité avant la défaillance.

## Le rythme, et la preuve de l’amélioration

Les mesures deviennent utiles lorsque quelqu’un examine les tendances et demande ce qui a changé. Une revue mensuelle peut convenir aux capacités critiques ; un événement majeur du cycle de vie justifie une revue plus approfondie. Le rythme doit suivre la vitesse à laquelle le risque sous-jacent change, et la revue doit déboucher sur une conversation sur l’action, sinon ce n’est que du reporting. Un programme de contrôle doit aussi pouvoir prouver que son travail a réduit le risque. Si une personnalisation a été retirée, l’organisation peut-elle montrer que la complexité de la mise à niveau a diminué ? Si la connaissance a été transférée, un autre ingénieur peut-il maintenant exécuter la reprise ? Si l’observabilité s’est améliorée, les incidents sont-ils détectés plus tôt ? L’amélioration doit être visible dans la capacité, pas dans les tâches accomplies.

Le contrôle est une capacité dont l’état doit rester visible pendant toute la vie de la plateforme, pas quelque chose qu’une organisation mesure une fois.

---

[← Chapitre 5 — Évaluer le contrôle de la plateforme](05-evaluer-le-controle-de-la-plateforme.md) · [Sommaire](../README.md) · [Chapitre 7 — Quand le contrôle est déjà perdu →](07-quand-le-controle-est-deja-perdu.md)
