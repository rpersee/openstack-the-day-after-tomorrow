*Partie V — Évoluer sans perdre le contrôle*

# Chapitre 16 — Automatisation et complexité opérationnelle

L’automatisation réduit l’effort manuel tout en augmentant la complexité opérationnelle. Elle introduit du logiciel, des dépendances, des modes de défaillance, du versionnement et des besoins de connaissance, et elle peut propager une erreur plus vite que n’importe quel opérateur humain. La première question est donc de savoir si automatiser quelque chose rendra la plateforme plus facile et plus sûre à exploiter pour cette organisation, ce qui est une autre question que celle de savoir si la chose peut être automatisée.

## L’automatisation doit suivre la compréhension

Automatiser un contournement non résolu fait survenir le problème plus vite et à plus grande échelle. L’automatisation doit suivre la compréhension, et ma position, que toutes les cultures d’ingénierie ne partagent pas, est qu’il faut automatiser l’exécution avant le jugement. Une action prévisible peut généralement être automatisée sans danger. Une décision qui exige un contexte métier, un diagnostic incertain ou une acceptation de risque doit en général rester sous autorité humaine, parce qu’une automatisation peut établir qu’un hôte est disponible, mais ne doit pas établir en silence qu’une charge de travail critique peut être perturbée, sauf si l’organisation a explicitement délégué cette décision. L’exemple d’évacuation du chapitre 10 en est la forme la plus nette : une automatisation qui évacue sur perte du battement de cœur (heartbeat) sans fencing s’est vu déléguer un jugement qu’elle ne peut pas rendre. La distinction entre exécution et jugement est le cœur du sujet.

La semi-automatisation est souvent la meilleure conception. Un script peut préparer une opération, collecter des preuves et proposer un résultat tandis qu’un ingénieur décide de poursuivre ou non ; cela préserve le jugement sans ramener tout le processus au travail manuel. Il y a aussi des raisons légitimes de ne pas automatiser du tout : les opérations peu fréquentes, les décisions très contextuelles et les procédures dont le coût d’automatisation dépasse la valeur peuvent rester manuelles ou semi-automatiques.

## L’automatisation est du logiciel de production

Dès qu’une automatisation peut affecter des ressources OpenStack de production, elle mérite la discipline de la production : un propriétaire, une gestion de versions, des tests, une documentation, de l’observabilité et un chemin de reprise. Que son implémentation ne soit « qu’un script » ne réduit pas sa conséquence, et un script créé par commodité devient une dépendance de production la première fois qu’il est utilisé pendant un incident. L’organisation doit savoir quand une automatisation s’est exécutée, ce qu’elle a changé, si elle a réussi et comment l’arrêter ou revenir à l’état antérieur.

Le périmètre compte. Une automatisation qui peut affecter tous les hôtes de calcul a besoin de garde-fous plus solides qu’une automatisation qui agit sur une seule ressource de test. Chaque fois que c’est possible, les actions automatisées doivent avoir des limites explicites et des chemins de reprise ; une automatisation qui migre des charges de travail, modifie le réseau ou touche un grand nombre de ressources ne doit pas s’exécuter comme un lot opaque, et plus l’action est destructrice, plus la prévisualisation, l’exécution à blanc (*dry run*), le périmètre explicite, la confirmation, la supervision et les conditions d’arrêt deviennent importants. Un opérateur doit pouvoir déterminer ce qu’une automatisation va faire avant d’autoriser une action à forte conséquence.

## L’automatisation peut cacher la complexité et devenir de la dette de contrôle

Une plateforme fortement automatisée paraît simple parce que les humains voient moins de commandes. La complexité n’a pas disparu ; elle s’est déplacée dans du logiciel, des pipelines, des dépendances et de la gestion d’état, et un opérateur doit pouvoir expliquer ce que fait une automatisation avant de lui faire confiance pendant un incident. Une automatisation que seul son créateur peut expliquer ou rétablir est de la dette de contrôle : elle a réduit le travail manuel d’aujourd’hui et augmenté l’incertitude de demain.

La valeur de l’automatisation est donc un compromis métier plutôt qu’un simple gain de temps d’ingénierie. Elle peut réduire l’erreur humaine, améliorer la cohérence et accélérer la réponse ; en face se trouvent l’effort de développement, la maintenance, les modes de défaillance, l’expertise et le coût de cycle de vie.

> **Principe.** L’objectif est le bon niveau d’automatisation pour la plateforme que l’organisation est réellement capable d’exploiter, et c’est rarement le maximum.

---

[← Chapitre 15 — Complexité, dette technique et simplification](15-complexite-dette-technique-et-simplification.md) · [Sommaire](../README.md) · [Chapitre 17 — La sécurité est un travail de plateforme →](17-la-securite-est-un-travail-de-plateforme.md)
