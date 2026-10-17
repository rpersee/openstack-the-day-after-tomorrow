*Partie VI — Décisions du terrain*

# Chapitre 19 — Quand la décision sûre est de s’arrêter

Les équipes d’exploitation sont jugées sur leur aptitude à rétablir le service et à faire avancer le travail. Cela crée un biais en faveur de l’action, et dans les environnements critiques, continuer d’agir n’est pas toujours l’option la plus sûre. Parfois, s’arrêter est la décision qui préserve le contrôle.

## Contexte

Une plateforme OpenStack de production portant des charges de travail métier, avec un plan de contrôle à haute disponibilité : un cluster RabbitMQ et un cluster de bases de données Galera.

## Signal

Les utilisateurs ont signalé qu’ils ne pouvaient plus créer de machines virtuelles. Les instances existantes fonctionnaient normalement. Le premier signal était donc la perte d’une capacité, le provisionnement, et non une panne.

## Incertitude

L’investigation a montré que l’infrastructure partagée du plan de contrôle était en mauvaise santé : RabbitMQ ne parvenait plus à mener les échanges RPC à leur terme de façon fiable, et le cluster MariaDB était lui aussi affecté. Ce que l’on ne savait *pas* à ce stade, c’était pourquoi, quelles requêtes avaient été partiellement appliquées, et ce qu’il adviendrait de l’état de la plateforme si les API continuaient d’accepter des opérations pendant que le bus de messages et la base de données se trouvaient dans cet état.

## Risque métier

L’impact métier immédiat était borné : aucune nouvelle VM ne pouvait être créée, et les consommateurs pouvaient en être informés. Le risque plus grand était invisible. Un plan de contrôle instable qui continue d’accepter des opérations d’API aggrave son propre état, en créant des allocations orphelines, des instances à moitié construites et des enregistrements qui se contredisent entre Nova, Placement et Neutron, et chacun de ces enregistrements rend la reprise plus lente et moins certaine. Les charges de travail déjà en fonctionnement n’étaient pas menacées par l’état du plan de contrôle lui-même ; elles étaient menacées par une tentative non contrôlée de le réparer.

## Options

L’objectif immédiat semblait être de rétablir la création de VM aussi vite que possible, ce qui signifiait réparer le bus de messages et la base de données pendant que les API continuaient d’accepter des requêtes. L’alternative était de cesser d’abord d’accepter des requêtes, de redémarrer l’infrastructure partagée, de vérifier, et seulement ensuite de rouvrir.

## Décision

L’équipe a délibérément arrêté les API OpenStack, redémarré le cluster RabbitMQ après avoir purgé ses files, puis redémarré MariaDB avant de rouvrir la plateforme. L’organisation a accepté une perte temporaire et explicite d’une capacité afin de protéger l’état de la plateforme et les charges de travail qui fonctionnaient déjà. Arrêter d’abord les API signifiait qu’aucune nouvelle requête n’arrivait pendant que le bus de messages et la base de données étaient remis en service ; purger les files signifiait que l’arriéré de messages RPC accumulé pendant la dégradation était écarté plutôt que rejoué contre une base de données qui venait d’être redémarrée. Arrêter les API ne rend pas une plateforme entièrement silencieuse : les conductors, les schedulers et les agents poursuivent leur propre travail, et quand RabbitMQ revient, chaque agent de chaque hôte se reconnecte en même temps, ce qui, sur une grande plateforme, est en soi une charge à anticiper. La purge acceptait que certaines opérations en cours soient perdues.

## Compromis

Le coût était visible et borné : le provisionnement a été indisponible pendant la durée de la reprise, et l’arrêt était une décision que personne ne pourrait présenter ensuite comme « la plateforme est restée disponible ». Le bénéfice était que la reprise s’est déroulée sur une plateforme dont l’état ne changeait plus, ce qui donnait un sens à chaque vérification. Un plan de contrôle instable laissé ouvert aurait produit des conséquences plus larges, plus difficiles à prévoir et plus difficiles à expliquer après coup.

## Résultat

Avant de rouvrir les API, l’équipe a vérifié trois choses : que le cluster Galera avait retrouvé sa taille complète en état Primary et que le cluster RabbitMQ était entier, ses files recréées et ses consommateurs connectés ; que chaque service compute et chaque agent réseau se signalait de nouveau ; et qu’une machine virtuelle de test pouvait être créée, atteinte sur le réseau et supprimée de bout en bout. Ce n’est qu’alors que le provisionnement a été rétabli. La cause a été établie après coup : une partition réseau au sein du cluster RabbitMQ, qui avait scindé le bus en deux côtés entre lesquels les services ne parvenaient pas à s’accorder.

## Leçon

C’est cela, la dégradation contrôlée. La capacité indisponible était explicite et bornée ; l’alternative ne l’était pas. Trois choses rendent une décision de ce type possible. L’une est un fait technique : arrêter les API n’arrête pas les charges de travail (chapitre 1). Les deux autres sont organisationnelles : savoir, avant l’incident, qui a l’autorité pour prendre une décision perturbatrice (chapitre 13), et avoir une direction qui soutiendra un ingénieur qui arrête une opération pour une raison qu’il peut expliquer. Une décision d’arrêt doit aussi être communiquée comme une décision de protection : ce qui est restreint, pourquoi continuer créerait un risque plus grand, ce qui reste protégé, et quelle condition permettra de rouvrir la plateforme.

La cause porte sa propre leçon. Une partition RabbitMQ est un mode de défaillance connu, avec un ensemble connu de parades, du réglage de gestion des partitions du cluster sur les versions qui en ont encore un jusqu’à la conception réseau qui empêche la scission en premier lieu, et la revue d’incident doit aller jusque-là, sinon la même situation revient. La note technique du chapitre 10 nomme les réglages ; l’exemple du chapitre 11 montre pourquoi le runbook d’un cluster partitionné n’est pas celui d’un nœud qui l’a quitté.

Le même principe s’applique aux changements planifiés. Un changement peut déjà être en cours lorsqu’un comportement inattendu apparaît, et le temps déjà investi ne crée aucune obligation de continuer. Les conditions d’arrêt doivent être concrètes et, pour les maintenances récurrentes, convenues à l’avance : une dépendance attendue se comporte différemment ; le rayon d’impact dépasse le périmètre approuvé ; la supervision est insuffisante ; la reprise n’est plus crédible ; la performance d’une charge de travail critique franchit un seuil inacceptable ; la capacité requise n’est pas disponible ; l’autorité de décision n’est pas joignable. Des limites convenues à l’avance réduisent la pression à improviser.

S’arrêter doit créer un nouveau point de décision plutôt qu’une interruption sans direction : préserver les preuves, établir l’état courant, communiquer l’impact, réévaluer, définir les conditions du redémarrage. Et une fois arrêté, un changement ne doit pas reprendre automatiquement. La situation a changé ; de nouvelles preuves ont pu apparaître ; l’hypothèse d’origine ne tient peut-être plus. Reprendre est une nouvelle décision. La direction opérationnelle doit distinguer l’inactivité du confinement, parce qu’arrêter une API, geler un déploiement ou refuser une migration à chaud de plus est une décision active pour empêcher le domaine de défaillance de s’étendre, et la culture doit être à la hauteur du processus. Si le processus formel dit « arrêtez quand ce n’est pas sûr » alors que la culture dit « on ne s’arrête jamais », c’est le processus qui perdra. La capacité à s’arrêter en sécurité est un test de maturité organisationnelle : une équipe mûre peut expliquer ce qu’elle a arrêté, pourquoi, ce qu’elle protégeait et ce qui doit devenir vrai avant qu’elle continue.

> **Principe.** S’arrêter n’est pas renoncer au contrôle. Dans les bonnes circonstances, c’est ainsi que le contrôle est préservé.

---

[← Chapitre 18 — Faire évoluer une plateforme critique](18-faire-evoluer-une-plateforme-critique.md) · [Sommaire](../README.md) · [Chapitre 20 — Sécurité, capacité et criticité métier →](20-securite-capacite-et-criticite-metier.md)
