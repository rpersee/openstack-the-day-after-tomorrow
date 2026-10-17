# Comment lire ce livre

Ce livre porte sur le raisonnement d’exploitation, pas sur le déploiement. L’essentiel en est une argumentation : pourquoi le contrôle d’une plateforme s’érode, comment l’évaluer, comment le conserver pendant que la plateforme, ses charges de travail et les personnes qui l’exploitent changent. Pour que cette argumentation reste honnête, le texte distingue quatre sortes d’énoncés, et en signale trois explicitement.

Les **notes techniques** énoncent des faits sur OpenStack qui peuvent être vérifiés dans la documentation des projets : ce que fait un service, ce qu’upstream maintient, ce qu’une commande vérifie. Ce sont les passages du livre les plus exposés au vieillissement ; c’est pourquoi chacun nomme sa source, et les références en fin d’ouvrage en donnent l’emplacement.

> **Note technique.** Les encadrés de ce type contiennent des faits vérifiables sur OpenStack, avec une référence.

Les **principes** sont les règles d’exploitation que le livre défend. La plupart sont des pratiques largement partagées par ceux qui exploitent des plateformes de longue durée ; quelques-unes sont ma position personnelle, et le texte qui les entoure le dit. Un principe est une recommandation, pas un fait, et un lecteur dont la plateforme et l’organisation sont différentes peut légitimement le peser autrement.

> **Principe.** Les encadrés de ce type énoncent une règle d’exploitation que le livre recommande.

Les passages **sur le terrain** décrivent des situations que j’ai rencontrées ou traversées, suffisamment abstraites pour qu’aucun environnement ne soit identifiable. Ils témoignent de ce qui s’est produit dans un contexte donné, pas de ce qui se produira dans le vôtre.

> **Sur le terrain.** Les encadrés de ce type décrivent une situation opérationnelle et la décision qu’elle a exigée.

Tout le reste du livre est du raisonnement : l’argumentation qui relie les faits, les principes et l’expérience. Là où j’exprime une opinion que des ingénieurs compétents peuvent rejeter, je le dis à la première personne.

Le livre a une dette envers des travaux antérieurs qu’il ne répète pas. La boucle d’exploitation du chapitre 4 appartient à la même famille que le cycle planifier–faire–vérifier–agir de Deming et que la boucle observer–s’orienter–décider–agir ; les exercices de reprise du chapitre 10 descendent des tests de reprise après sinistre pratiqués par les grands opérateurs du web et décrits dans la littérature de l’ingénierie de fiabilité des sites (SRE) ; les fiches de décision et la discipline du changement ont une longue histoire dans la gestion des services informatiques. Ce que le livre ajoute, c’est l’application de ces idées à une plateforme qui a la forme particulière d’OpenStack : beaucoup de services, beaucoup de dépendances partagées, une longue durée de vie, et une organisation qui change en dessous.

## Trois lecteurs, trois parcours

Le livre s’adresse à l’ingénieur qui exploite la plateforme, à l’architecte qui la fait évoluer et au manager qui en est responsable. Le parcours prévu est la lecture dans l’ordre. La partie I pose le problème. La partie II montre comment évaluer et mesurer le contrôle. La partie III couvre les disciplines d’exploitation. La partie IV couvre l’organisation. La partie V couvre l’évolution : mises à niveau, dette, automatisation, sécurité et transformation. La partie VI déroule en détail deux décisions prises sur le terrain. Les annexes contiennent les outils.

Un ingénieur qui découvre OpenStack en production tirera le meilleur parti des notes techniques, des chapitres 5, 8, 10 et 14 et des passages de terrain, puis du reste. Un manager ou un sponsor sans connaissance d’OpenStack peut suivre un parcours plus court : l’introduction, les chapitres 1 à 3, le chapitre 7, la dernière section du chapitre 12, les chapitres 13 et 14 jusqu’à la première note technique, les chapitres 19 et 20, la conclusion, et les annexes D et E. Ce parcours explique pourquoi exploiter la plateforme est difficile, quels sont les risques pour l’activité, et quelles questions poser à l’équipe plateforme ; le glossaire explique les noms de services que le texte emploie.

---

[← Pages liminaires](00-pages-liminaires.md) · [Sommaire](../README.md) · [Introduction →](00-introduction.md)
