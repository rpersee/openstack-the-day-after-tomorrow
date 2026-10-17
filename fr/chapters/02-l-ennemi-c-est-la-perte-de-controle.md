*Partie I — Comprendre le problème*

# Chapitre 2 — L’ennemi, c’est la perte de contrôle

Le concept central de ce livre est le contrôle. Une plateforme OpenStack critique est sous contrôle quand l’organisation peut comprendre son état, prendre des décisions délibérées, intervenir sans danger, rétablir le service quand il le faut et continuer d’évoluer sans dépendre de circonstances qu’elle ne comprend pas.

Cette définition dépasse délibérément la disponibilité. Une plateforme peut être disponible tout en étant difficile à exploiter. Elle peut servir des charges de travail alors que sa reprise dépend d’un seul ingénieur. Elle peut avoir d’excellents tableaux de bord sans que personne sache quels signaux comptent. Elle peut avoir une approbation des changements stricte alors que les décisions sont prises à partir d’informations incomplètes. La disponibilité est un résultat ; le contrôle est une capacité, et il n’exige pas la perfection. Il y aura toujours de l’incertitude, des incidents et de la dette technique. L’objectif est de maintenir assez de capacité pour gérer l’incertitude qui compte.

## Quatre capacités

La **visibilité** est la capacité d’observer l’état de la plateforme, de comprendre les signaux significatifs et d’identifier les situations qui exigent de l’attention. Elle inclut les métriques, les journaux, les événements, la capacité, la performance et les retours des utilisateurs, mais aussi la propriété et les dépendances. Le but est une preuve utile, pas davantage de données.

La **stabilité** est la capacité de maintenir un état d’exploitation de confiance, de protéger les capacités critiques, et d’absorber les incidents et les changements sans perte de contrôle inutile. Elle inclut la dégradation contrôlée, la gestion de la capacité, le changement sûr et la reprise.

L’**organisation** est la capacité de maintenir les personnes, la connaissance, les compétences, la propriété et la collaboration nécessaires pour exploiter la plateforme durablement. Une collection d’experts n’est pas une équipe. Une équipe devient résiliente quand la capacité critique survit au départ de ses experts.

La **gouvernance** est la capacité de prendre, de communiquer et d’assumer les décisions concernant la plateforme, en particulier quand les objectifs métier, les contraintes techniques et les risques entrent en conflit. Tout le monde peut contester. Quelqu’un doit décider.

Ces capacités forment un système, et chacune échoue différemment quand les autres sont absentes. La visibilité sans compréhension produit de l’information sans action. La stabilité sans organisation dépend de héros. L’organisation sans gouvernance produit de l’optimisation locale. La gouvernance sans preuves devient de la bureaucratie. Le chapitre 4 décrit la boucle d’exploitation qui les relie en pratique. Le but est une organisation qui reste capable de composer avec un système imparfait, parce qu’un système parfait n’est pas proposé.

## Le contrôle est relatif à la conséquence

Le contrôle ne devrait jamais être évalué indépendamment de la conséquence métier. Un environnement de test non critique peut tolérer une capacité de reprise inférieure à celle d’une capacité de production qui soutient un processus métier critique. Une intégration expérimentale peut légitimement rester à une maturité inférieure à celle d’une dépendance partagée d’identité ou de réseau. L’objectif est de trouver où un contrôle faible croise une conséquence forte, parce que cette intersection est là où l’investissement doit se concentrer, plutôt que d’amener chaque composant au même niveau.

## Le contrôle inclut l’indépendance

Une plateforme peut paraître techniquement contrôlée tout en restant dépendante d’un fournisseur, d’un ingénieur de déploiement ou d’un processus d’exploitation propriétaire. L’indépendance ne signifie pas éliminer toute relation externe ; l’expertise externe peut être extrêmement précieuse, en particulier pour les problèmes OpenStack rares ou complexes, et la plupart des plateformes critiques tournent sur une distribution commerciale avec un contrat de support. Le risque apparaît quand l’organisation ne peut pas fonctionner sans ce tiers. Une relation saine avec un éditeur ou un spécialiste augmente la capacité interne avec le temps : l’organisation devient plus à même de comprendre la plateforme, de contester les recommandations et de prendre ses propres décisions. C’est particulièrement pertinent là où des modifications locales d’OpenStack ou un outillage spécialisé sont en jeu. Si les seules personnes capables d’expliquer le comportement de la plateforme travaillent pour quelqu’un d’autre, la plateforme a une lacune de contrôle organisationnelle, quelle que soit la qualité de fonctionnement de la technologie. Le chapitre 14 revient sur ce que cela signifie quand une distribution s’interpose entre la plateforme et upstream.

## Le contrôle est un état mouvant, et une capacité plutôt qu’un sentiment

Le contrôle s’améliore et se détériore. Une équipe perd de l’expertise, une version vieillit, une dépendance cesse d’être maintenue, une personnalisation est introduite, une procédure de reprise éprouvée devient obsolète après un changement d’architecture. Le contrôle doit être entretenu ; ce n’est pas une certification qui reste valide indéfiniment.

Il doit aussi être étayé par des preuves. Les ingénieurs expérimentés développent une intuition juste de leur plateforme, et cette intuition est précieuse, mais une organisation ne peut pas mesurer le contrôle par la confiance. Une équipe peut avoir le sentiment de contrôler sa plateforme parce que les incidents ont historiquement été résolus ; pourtant, si la reprise n’a jamais été exécutée par quelqu’un d’autre que l’ingénieur le plus expérimenté, l’organisation détient une preuve d’expertise, pas une preuve de résilience. C’est pourquoi le cadre traite la maturité comme un profil plutôt que comme une note : une plateforme peut être fortement contrôlée sur une capacité et faible sur une autre, et le chapitre 5 place chaque capacité sur un spectre avec des critères explicites.

## Le contrôle peut se perdre sans incident

Une plateforme n’a pas besoin de tomber en panne pour que le contrôle se détériore. Le départ d’un ingénieur clé réduit le contrôle. Une nouvelle personnalisation le réduit. Une version qui atteint sa fin de vie le réduit. Un corpus de documentation qui vieillit le réduit. Rien de tout cela ne produit d’alerte. C’est ce qui rend la gestion du contrôle différente de la gestion des incidents. La gestion des incidents répond à une défaillance observée ; la gestion du contrôle cherche aussi les conditions qui rendront une défaillance future plus difficile à comprendre ou à rétablir. C’est pourquoi les signaux organisationnels et de cycle de vie ont leur place dans la même discussion que la télémétrie technique, et pourquoi le chapitre 6 les traite comme mesurables.

---

[← Chapitre 1 — OpenStack ne s’arrête pas au déploiement](01-openstack-ne-s-arrete-pas-au-deploiement.md) · [Sommaire](../README.md) · [Chapitre 3 — Pourquoi de bonnes plateformes deviennent difficiles à exploiter →](03-pourquoi-de-bonnes-plateformes-deviennent-difficiles-a-exploiter.md)
