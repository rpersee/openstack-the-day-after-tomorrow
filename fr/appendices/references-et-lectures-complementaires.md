# Références et lectures complémentaires

Le cadre présenté dans ce livre est la synthèse, par l’auteur, d’une expérience opérationnelle. Les références ci-dessous ancrent les notes techniques dans la documentation de référence ; elles étayent les faits techniques, pas le cadre d’exploitation lui-même. OpenStack évolue en permanence, et le statut des versions, la documentation et les détails des projets changent après la publication. Pour les décisions de cycle de vie, consultez toujours la documentation courante de la version et des projets plutôt qu’une affirmation de ce livre.

## Architecture et services

- Documentation OpenStack, portail central. https://docs.openstack.org/
- Nova, *Nova System Architecture* (composants et leurs responsabilités ; chapitre 5). https://docs.openstack.org/nova/latest/user/architecture.html
- Nova, *Cells v2* (bases de données de cellules, découverte des hôtes ; chapitre 5). https://docs.openstack.org/nova/latest/admin/cells.html
- Documentation de Nova. https://docs.openstack.org/nova/latest/
- Documentation de Neutron, y compris les références sur les agents et OVN utilisées au chapitre 1. https://docs.openstack.org/neutron/latest/
- Documentation de Cinder. https://docs.openstack.org/cinder/latest/
- Documentation de Glance. https://docs.openstack.org/glance/latest/
- Documentation de Keystone. https://docs.openstack.org/keystone/latest/
- Documentation de Placement. https://docs.openstack.org/placement/latest/
- Références des API OpenStack. https://docs.openstack.org/api-ref/

## Exploitation

- Nova, *Configure live migrations* (prérequis, stockage partagé et migration par bloc ; chapitre 20). https://docs.openstack.org/nova/latest/admin/configuring-migrations.html
- Nova, *Live-migrate instances*. https://docs.openstack.org/nova/latest/admin/live-migration-usage.html
- Nova, *Migrate instances* (migration à froid ; chapitre 20). https://docs.openstack.org/nova/latest/admin/migration.html
- Nova, *Evacuate instances* (chapitres 10 et 20). https://docs.openstack.org/nova/latest/admin/evacuate.html
- Nova, *CPU topologies* (politique de CPU dédiés, `cpu_dedicated_set`, politique des threads d’émulation ; chapitre 15). https://docs.openstack.org/nova/latest/admin/cpu-topologies.html
- Nova, *nova-manage* (audit et réparation de Placement, archivage des lignes supprimées ; chapitres 6 et 10). https://docs.openstack.org/nova/latest/cli/nova-manage.html
- oslo.messaging, *RabbitMQ driver* (files quorum et options associées ; chapitre 10). https://docs.openstack.org/oslo.messaging/latest/admin/rabbit.html
- RabbitMQ, *Quorum Queues* (exigence de majorité, suppression du miroir classique dans la version 4.0 ; chapitre 10). https://www.rabbitmq.com/docs/quorum-queues
- RabbitMQ, *Clustering and Network Partitions* (traitement des partitions ; chapitres 10 et 19). https://www.rabbitmq.com/docs/partitions
- RabbitMQ, *Monitoring* (chapitre 8). https://www.rabbitmq.com/docs/monitoring
- Documentation de Galera Cluster, *Weighted Quorum* (quorum et état non-Primary ; chapitre 10). https://galeracluster.com/library/documentation/weighted-quorum.html
- Documentation de Galera Cluster, *Crash Recovery* (amorçage depuis le nœud le plus avancé ; chapitre 10). https://galeracluster.com/library/documentation/crash-recovery.html
- Documentation de Galera Cluster, *Monitoring the Cluster* (chapitre 8). https://galeracluster.com/library/documentation/monitoring-cluster.html
- Documentation du Large Scale SIG, dont *The Scaling Journey* (chapitre 5). https://docs.openstack.org/large-scale/
- OpenStack Operations Guide. Dernière mise à jour substantielle en 2017 ; historiquement précieux, mais qui n’est plus à jour. https://docs.openstack.org/operations-guide/

## Mises à niveau et cycle de vie

- OpenStack Releases : statut des séries, désignation SLURP et dates (chapitre 14). https://releases.openstack.org/
- OpenStack Project Team Guide, *Stable Branches* (critères de backport, Maintained / Unmaintained / End of Life ; chapitre 14). https://docs.openstack.org/project-team-guide/stable-branches.html
- Nova, *Upgrades* (séquence de mise à niveau sans interruption, compatibilité des versions de services, migrations de données en ligne ; chapitre 14). https://docs.openstack.org/nova/latest/admin/upgrades.html
- Neutron, *Upgrade strategy* (phases d’expansion et de contraction ; chapitre 14). https://docs.openstack.org/neutron/latest/contributor/internals/upgrade.html
- `nova-status upgrade check`. https://docs.openstack.org/nova/latest/cli/nova-status.html
- `neutron-status upgrade check`. https://docs.openstack.org/neutron/latest/cli/neutron-status.html
- `cinder-status upgrade check`. https://docs.openstack.org/cinder/latest/cli/cinder-status.html
- `placement-status upgrade check`. https://docs.openstack.org/placement/latest/cli/placement-status.html
- Notes de version de Nova, Train (20.0.0) : migration à chaud tenant compte de la topologie NUMA (chapitre 15). https://docs.openstack.org/releasenotes/nova/train.html
- Index des notes de version des projets. https://docs.openstack.org/releasenotes/
- Statistiques de l’OpenStack User Survey, pour la répartition des versions réellement en production (chapitre 14). https://www.openstack.org/analytics

## Sécurité

- Avis de sécurité OpenStack (OSSA), publiés par la Vulnerability Management Team (chapitre 17). https://security.openstack.org/ossalist.html
- OpenStack Technical Committee, *Consistent and Secure Default RBAC* (personas, `enforce_new_defaults`, `enforce_scope`, phases ; chapitre 17). https://governance.openstack.org/tc/goals/selected/consistent-and-secure-rbac.html
- Keystone, *Fernet — Frequently Asked Questions* (rotation des clés ; chapitre 17). https://docs.openstack.org/keystone/latest/admin/fernet-token-faq.html
- OpenStack Security Guide. Le guide n’a pas été substantiellement mis à jour depuis plusieurs versions ; à utiliser pour les concepts, pas pour la configuration propre à une version. https://docs.openstack.org/security-guide/

## Filiation

- Google, *Site Reliability Engineering* (2016) et *The Site Reliability Workbook* (2018), pour les tests de reprise après sinistre, la culture du post-mortem et le traitement du travail d’exploitation comme de l’ingénierie. https://sre.google/books/
- Le cycle planifier–faire–vérifier–agir (Deming) et la boucle observer–s’orienter–décider–agir (Boyd), ancêtres de la boucle de contrôle du chapitre 4.

## Marques

- Informations sur la marque OpenStack. https://www.openstack.org/brand/

---

[← Annexe F — Glossaire](annexe-f-glossaire.md) · [Sommaire](../README.md)
