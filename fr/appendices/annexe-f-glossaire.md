*Annexes*

# Annexe F — Glossaire

**Alignement upstream** (*upstream alignment*) — Le degré auquel la plateforme reste raisonnablement proche des versions et du comportement d’OpenStack maintenus upstream.

**Backport** — Dans l’OpenStack upstream, un correctif repris (*cherry-pick*) de la branche master vers une branche stable, selon la politique des branches stables. Dans ce livre, plus largement, toute modification portée par la plateforme déployée qui ne fait pas partie de la version qu’elle exécute (chapitre 14).

**Binding du port** (*port binding*) — L’étape au cours de laquelle le mechanism driver de Neutron et l’agent ou le contrôleur OVN d’un hôte de calcul câblent le port d’une instance ; Nova attend la confirmation de Neutron avant de terminer un démarrage (chapitre 5).

**Capacité (capability, capacity)** — L’édition française rend par « capacité » deux mots anglais distincts : *capability*, ce que l’organisation ou la plateforme sait faire (les quatre capacités, une capacité métier), et *capacity*, les ressources finies disponibles (capacité de calcul, capacité de changement). Le contexte lève l’ambiguïté ; lorsque les deux se côtoient, *capacity* est rendu par « ressources » ou « marge de capacité ».

**Capacité de changement** (*change capacity*) — L’aptitude finie de l’organisation à exécuter des changements en production de façon sûre sans submerger l’exploitation.

**Capacité métier** (*business capability*) — Un résultat ou un service dont l’organisation dépend, par opposition à un composant technique.

**Capacité opérationnelle** (*operational capacity*) — Les personnes, le temps, les environnements, les fenêtres de maintenance et l’attention, tous finis, disponibles pour exploiter et changer la plateforme de façon sûre.

**Conductor** — Le service de Nova qui coordonne les opérations en plusieurs étapes, comme les constructions et les migrations, et qui sert d’intermédiaire pour l’accès à la base de données au nom des services compute.

**Contrôle** (*control*) — L’aptitude de l’organisation à comprendre, décider, intervenir, rétablir et faire évoluer la plateforme OpenStack de façon délibérée.

**Day 1 / Day 2** — Day 1 (le jour 1) est la construction de la plateforme ; Day 2 (le jour 2) est tout ce qui suit dès que des charges de travail en dépendent : exploitation, maintenance, incidents, mises à niveau, reprise et l’organisation qui les entoure.

**Dégradation contrôlée** (*controlled degradation*) — Une réduction délibérée et temporaire de capacité destinée à protéger des capacités plus importantes ou à prévenir une instabilité plus large.

**Dette de contrôle** (*control debt*) — Perte d’aptitude organisationnelle causée par des dépendances non documentées, une expertise concentrée, une complexité non maîtrisée, une reprise fragile ou toute autre condition qui réduit le contrôle opérationnel. Distincte de la dette technique : le même artefact peut être l’une, l’autre ou les deux (chapitre 3).

**Dette technique** (*technical debt*) — Un compromis technique délibéré ou accumulé dont la plateforme doit porter les conséquences dans le temps.

**Droits de décision** (*decision rights*) — L’autorité explicite de prendre une décision et d’en accepter la conséquence.

**État de confiance** (*trusted state*) — Un état de la plateforme dont le comportement, les dépendances et les caractéristiques de reprise pertinents sont suffisamment connus pour que l’on puisse s’y fier (chapitre 1).

**File quorum** (*quorum queue*) — Un type de file RabbitMQ répliquée sur une majorité des nœuds du cluster, désormais recommandé par oslo.messaging à la place des files classiques en miroir, que RabbitMQ 4.0 a supprimées (chapitre 10).

**Maintained / Unmaintained / End of Life** — Les phases d’une série de versions OpenStack upstream (maintenue, non maintenue, fin de vie). Distinctes du support d’un éditeur (chapitre 14).

**Modèle de décision pondéré** (*weighted decision model*) — Une technique d’aide à la décision qui compare des options selon des critères explicitement pondérés. Elle ne remplace ni le jugement ni les contraintes de sécurité obligatoires.

**OSSA** — OpenStack Security Advisory : avis de sécurité publié par l’équipe de gestion des vulnérabilités d’OpenStack (Vulnerability Management Team) pour les défauts des services OpenStack (chapitre 17).

**PCPU / VCPU** — Les classes de ressources de Placement pour les CPU de l’hôte respectivement dédiés (épinglés) et partagés (chapitre 15).

**Plan de contrôle / plan de données** (*control plane / data plane*) — Le plan de contrôle est l’ensemble des services d’API OpenStack, des schedulers, des conductors, du bus de messages et des bases de données qui acceptent et exécutent les requêtes ; le plan de données est constitué des hyperviseurs, du stockage et des chemins réseau sur lesquels les instances s’exécutent réellement, ainsi que des agents qui y tournent. Les deux tombent en panne séparément (chapitre 1).

**Rayon d’impact** (*blast radius*) — L’étendue de la plateforme, et des charges de travail qu’elle porte, qu’atteindrait la défaillance d’un changement ou d’un composant donné.

**Responsabilité d’une capacité** (*capability accountability*) — Responsabilité de maintenir une capacité technique exploitable, maintenable, modifiable et récupérable dans le temps.

**Responsabilité opérationnelle** (*operational accountability*) — Responsabilité de la bonne exécution d’une opération (chapitre 12).

**Responsabilité technique de la plateforme** (*platform technical accountability*) — Responsabilité de la cohérence technique de la plateforme OpenStack à travers ses services et ses dépendances.

**Services cités dans ce livre** — Keystone (identité et catalogue de services), Nova (calcul), Neutron (réseau), Cinder (stockage bloc), Glance (images), Placement (inventaire et allocation des ressources). En dessous : RabbitMQ (le bus de messages), MariaDB Galera (le cluster de bases de données), memcached (cache, notamment des jetons), et un répartiteur de charge portant l’IP virtuelle des API.

**SLURP** — Skip Level Upgrade Release Process : la désignation upstream d’une série de versions sur deux comme version depuis laquelle la mise à niveau vers la série SLURP suivante est prise en charge (chapitre 14).

**Théâtre du contrôle** (*control theatre*) — Un mécanisme qui crée l’apparence du contrôle sans améliorer réellement la qualité des décisions ni la capacité opérationnelle.

---

[← Annexe E — Les principes d’exploitation en un coup d’œil](annexe-e-les-principes-d-exploitation-en-un-coup-d-oeil.md) · [Sommaire](../README.md) · [Références et lectures complémentaires →](references-et-lectures-complementaires.md)
