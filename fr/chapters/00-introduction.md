# Introduction

OpenStack ne s’arrête pas au déploiement.

Le déploiement crée une plateforme : il met en place les services, l’infrastructure et les intégrations nécessaires pour rendre disponibles des capacités de cloud. Mais dès que des charges de travail dépendent de cette plateforme, une responsabilité d’une autre nature commence, et elle dure des années : garder la plateforme compréhensible, exploitable, récupérable et capable d’évoluer. Ce livre porte sur cette responsabilité.

Ce n’est ni un guide de déploiement, ni un manuel de configuration, ni un catalogue de bonnes pratiques universelles. C’est un cadre opérationnel pour les personnes responsables de plateformes OpenStack critiques, en particulier lorsque l’environnement est grand, ancien, complexe ou déjà chargé de dette opérationnelle. Sa question centrale est simple.

***Contrôlez-vous encore votre plateforme OpenStack ?***

Le contrôle ne signifie pas la perfection : des incidents se produisent encore, les composants ne sont pas tous standardisés, la dette technique n’a pas été éliminée. Le contrôle signifie que l’organisation peut encore comprendre, décider, intervenir, rétablir et faire évoluer sans dépendre d’individus, d’hypothèses non documentées ou d’une complexité non maîtrisée. Le chapitre 2 le définit précisément.

OpenStack rend ce problème inhabituellement visible. La plateforme n’est pas un programme mais un ensemble de services qui coopèrent, chacun avec sa propre base de données, sa propre configuration et ses propres modes de défaillance : Keystone pour l’identité, Nova pour le calcul, Neutron pour le réseau, Cinder pour le stockage bloc, Glance pour les images, Placement pour la comptabilité des ressources, et souvent d’autres. Ces services reposent sur un bus de messages, un cluster de bases de données, du stockage, du réseau, des systèmes d’exploitation, un outillage de déploiement et une infrastructure qui ne sont pas du tout OpenStack. Un symptôme dans un service a couramment son origine dans une autre dépendance, et une petite décision d’exploitation peut avoir des conséquences sur toute la plateforme.

La plateforme a aussi une histoire. Les personnalisations s’accumulent. Des patchs locaux sont introduits. Les contournements deviennent des procédures, les procédures deviennent de l’automatisation, l’automatisation devient de l’infrastructure. Les personnes qui comprenaient les raisons d’origine partent, et l’équipe suivante hérite du résultat. La distance entre la plateforme et l’OpenStack upstream dont elle est partie devient une préoccupation opérationnelle à part entière, parce que chaque divergence est de la connaissance, des tests et de la réconciliation que l’organisation doit porter seule. C’est pourquoi le livre revient sans cesse à un principe :

> **Principe.** Rester aussi proche d’upstream que possible en pratique.

Ce n’est pas une interdiction de toute modification locale. Un patch porté localement peut être la bonne décision à court terme lorsqu’une mise à niveau complète créerait un risque immédiat plus grand. La question importante est ce que la décision crée ensuite : un patch peut réduire le risque de changement ce trimestre tout en augmentant, pour des années, la quantité de connaissance propre à la plateforme que l’organisation doit entretenir. Le même raisonnement vaut pour la dette technique, l’automatisation, l’architecture et l’organisation. Aucune n’est bonne ou mauvaise en soi. La question est toujours ce que l’organisation gagne, ce qu’elle devra exploiter, quel risque elle accepte, et si elle reste capable de changer de cap.

Le cadre développé ici est construit autour de quatre capacités :

- **Visibilité** — savoir ce qui se passe ;
- **Stabilité** — protéger ce qui compte et maintenir un état d’exploitation de confiance ;
- **Organisation** — faire en sorte que la connaissance et la capacité survivent aux personnes et aux changements d’organisation ;
- **Gouvernance** — faire en sorte que les décisions soient prises avec les preuves, l’autorité et la responsabilité appropriées.

Ces capacités sont reliées par une boucle d’exploitation, *Observer* → *Comprendre* → *Prioriser* → *Décider* → *Agir* → *Vérifier* → *Apprendre*, que le chapitre 4 développe. La boucle est volontairement simple. Sa valeur vient de son application constante lorsque la plateforme est sous pression.

## Périmètre et limites

Le livre reste délibérément au niveau du raisonnement d’exploitation. Il ne prescrit ni distribution OpenStack, ni outil de déploiement, ni backend réseau, ni pile de supervision, ni organigramme, ni contrat de support ; ces choix dépendent du contexte et changent avec le temps. Le sujet est plus étroit et plus durable : comment une organisation conserve le contrôle d’une plateforme OpenStack critique pendant que la plateforme, ses dépendances, ses charges de travail et ses personnes changent. Le cadre est fait pour aider les gens à prendre de meilleures décisions dans leur propre environnement, pas pour remplacer le jugement d’ingénieur par une recette. Lorsque la réponse opérationnelle dépend réellement du backend ou de la méthode de déploiement, le texte le dit plutôt que de prétendre le contraire.

Les situations décrites sont tirées d’une expérience opérationnelle réelle et abstraites de telle sorte qu’aucun environnement client ne puisse être reconnu. Leur but est d’exposer des schémas de décision, pas de décrire un déploiement particulier.

La difficulté d’OpenStack n’est pas de le faire fonctionner une fois, mais de le garder sous contrôle après que les personnes qui l’ont déployé sont passées à autre chose, après que les hypothèses d’origine ont changé, et après que la plateforme est devenue quelque chose dont l’entreprise ne peut plus se passer.

C’est cela, après-demain.

---

[← Comment lire ce livre](00-comment-lire-ce-livre.md) · [Sommaire](../README.md) · [Chapitre 1 — OpenStack ne s’arrête pas au déploiement →](01-openstack-ne-s-arrete-pas-au-deploiement.md)
