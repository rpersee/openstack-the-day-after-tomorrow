# Édition française : méthode et conventions

Ce document fixe la méthode de travail de l’édition française d’*OpenStack, the Day After Tomorrow*. Il s’applique à tout fichier de `fr/`. L’édition anglaise reste le texte de référence : l’édition française la suit chapitre par chapitre, section par section, encadré par encadré, et toute correction de fond est faite d’abord dans l’édition anglaise puis reportée ici (voir [`CONTRIBUTING.md`](../CONTRIBUTING.md)).

## Principes

1. **Même structure, même méthode.** Un fichier Markdown par chapitre, la même organisation de sections, les mêmes encadrés, les mêmes figures et tableaux, le même pied de page de navigation. Le PDF français est généré par la même chaîne (`tools/pdf/build.sh fr`) et vérifié par les mêmes contrôles ; la parité des deux éditions est vérifiée par `tools/check_editions.py`.
2. **Une édition, pas une traduction littérale.** Le sens, les arguments, les exemples, les nuances et la voix de l’auteur sont conservés intégralement ; la phrase française est reconstruite quand le calque serait lourd. Rien n’est résumé, rien n’est omis, rien n’est ajouté sur le fond.
3. **Terminologie stable.** Les noms officiels des projets, services, commandes, options et statuts restent en anglais. Les concepts du livre ont une traduction unique, listée ci-dessous.
4. **Registre.** Français professionnel, naturel, accessible ; vouvoiement implicite (le texte s’adresse au lecteur à la deuxième personne du pluriel quand l’original dit *you*) ; première personne conservée là où l’auteur la prend.

## Correspondance des fichiers

| Édition anglaise | Édition française |
| --- | --- |
| `chapters/00-front-matter.md` | `fr/chapters/00-pages-liminaires.md` |
| `chapters/00-how-to-read-this-book.md` | `fr/chapters/00-comment-lire-ce-livre.md` |
| `chapters/00-introduction.md` | `fr/chapters/00-introduction.md` |
| `chapters/NN-<slug>.md` (1 à 21) | `fr/chapters/NN-<slug-français>.md` (même numéro) |
| `appendices/appendix-X-<slug>.md` | `fr/appendices/annexe-X-<slug-français>.md` (même lettre) |
| `appendices/references-and-further-reading.md` | `fr/appendices/references-et-lectures-complementaires.md` |
| `assets/figures/figure-N-M.svg` | `assets/figures/fr/figure-N-M.svg` (même géométrie, libellés traduits) |
| `README.md` | `fr/README.md` |

## Marqueurs structurels (reconnus par le filtre de build)

| Anglais | Français |
| --- | --- |
| `*Part I — Understanding the Problem*` | `*Partie I — Comprendre le problème*` |
| `# Chapter 4 — The Control Loop` | `# Chapitre 4 — La boucle de contrôle` |
| `*Appendices*` / `# Appendix A — …` | `*Annexes*` / `# Annexe A — …` |
| `# References and Further Reading` | `# Références et lectures complémentaires` |
| `> **Technical note.**` / `> **Technical note — titre.**` | `> **Note technique.**` / `> **Note technique — titre.**` |
| `> **Principle.**` | `> **Principe.**` |
| `> **From the field.**` | `> **Sur le terrain.**` |
| `![Figure 4.1](../assets/figures/figure-4-1.svg)` | `![Figure 4.1](../../assets/figures/fr/figure-4-1.svg)` |
| `*Figure 4.1: légende.*` | `*Figure 4.1 : légende.*` (espace fine insécable avant le deux-points) |
| `[← Chapter 3 — …](03-….md) · [Contents](../README.md) · [Chapter 5 — … →](05-….md)` | `[← Chapitre 3 — …](03-….md) · [Sommaire](../README.md) · [Chapitre 5 — … →](05-….md)` |

Le tiret des titres est le tiret cadratin (—), comme dans l’original. Les titres de chapitres et de sections prennent la capitale initiale seulement (usage français), sauf noms propres.

## Typographie française

- Guillemets français « … » avec espace fine insécable (U+202F) à l’intérieur ; guillemets anglais “ ” uniquement pour une citation imbriquée.
- Espace fine insécable (U+202F) avant `:` `;` `!` `?` ; espace insécable (U+00A0) avant `%` et entre un nombre et son unité ; les nombres s’écrivent « 25 % », « 17 × 24 cm ».
- Apostrophe typographique (’), comme dans l’original.
- Les listes à puces se terminent par un point-virgule et la dernière par un point lorsque l’original le fait ; sinon on suit l’original.
- Les termes anglais conservés ne sont pas mis en italique quand ils sont d’usage courant dans le métier (Day 2, backport, upstream, runbook, control plane). L’italique de l’original est conservé là où il marque une insistance.
- Les noms de commandes, options et fichiers restent en `code`, à l’identique.

## Terminologie

Les noms de services et de composants sont invariables : Keystone, Nova, Neutron, Cinder, Glance, Placement, RabbitMQ, MariaDB Galera, memcached, OVN, ML2/OVS, libvirt, QEMU, oslo.messaging, Fernet, Placement. Les rôles internes à Nova (scheduler, conductor) sont conservés en anglais avec l’article français (« le scheduler », « le conductor »). Les statuts upstream (**Maintained**, **Unmaintained**, **End of Life**, SLURP) sont conservés tels quels, avec une glose française à la première occurrence.

| Anglais | Français retenu | Remarques |
| --- | --- | --- |
| the day after tomorrow | après-demain | Titre : *OpenStack, après-demain* |
| mission-critical | critique (pour l’activité) | « plateforme critique », « plateforme OpenStack critique » |
| Day 1 / Day 2 | Day 1 / Day 2 | Terme de métier, conservé ; glosé « le jour 2 » à la première occurrence |
| Day-2 operations | exploitation Day 2 | |
| control / loss of control / under control | contrôle / perte de contrôle / sous contrôle | Concept central ; jamais « maîtrise » |
| control loop | boucle de contrôle | |
| control debt / technical debt | dette de contrôle / dette technique | |
| control theatre / documentation theatre | théâtre du contrôle / théâtre documentaire | |
| capability (four capabilities, business capability) | capacité (les quatre capacités, capacité métier) | |
| capacity (compute, change, operational) | capacité (de calcul, de changement, opérationnelle) | Homonymie assumée ; quand *capability* et *capacity* se côtoient, *capacity* devient « ressources » ou « marge de capacité » |
| Visibility / Stability / Organization / Governance | Visibilité / Stabilité / Organisation / Gouvernance | |
| Observe → Understand → Prioritize → Decide → Act → Verify → Learn | Observer → Comprendre → Prioriser → Décider → Agir → Vérifier → Apprendre | |
| Discover → Protect → Assess → Stabilize → Recover Knowledge → Simplify → Establish Control → Evolve | Découvrir → Protéger → Évaluer → Stabiliser → Reconstituer la connaissance → Simplifier → Établir le contrôle → Faire évoluer | Chapitre 7 |
| Unknown → Visible → Understood → Controlled → Recoverable → Sustainable | Inconnu → Visible → Compris → Contrôlé → Récupérable → Durable | Chapitre 5 |
| Context / Signal / Uncertainty / Business risk / Options / Decision / Trade-off / Outcome / Lesson | Contexte / Signal / Incertitude / Risque métier / Options / Décision / Compromis / Résultat / Leçon | Chapitres 19 et 20 |
| control plane / data plane | plan de contrôle / plan de données | |
| trusted state | état de confiance | |
| controlled degradation | dégradation contrôlée | |
| blast radius | rayon d’impact | |
| stop condition / exit condition / review condition | condition d’arrêt / condition de sortie / condition de revue | |
| guardrail | garde-fou | |
| recovery / to recover / recoverable / recoverability | reprise / rétablir / récupérable / capacité de reprise | « reprise » au sens des plans de reprise ; « reconstituer » pour la connaissance |
| recovery exercise | exercice de reprise | |
| rebuild | reconstruction / reconstruire | |
| incident / incident review / postmortem | incident / revue d’incident / post-mortem | |
| runbook | runbook | Conservé ; « procédure » pour *procedure* |
| workaround | contournement | |
| backport / to backport | backport (masc.) / rétroporter | Nom conservé, verbe français |
| upstream / upstream alignment | upstream / alignement upstream | « rester aussi proche d’upstream que possible » |
| distribution / vendor | distribution / éditeur | « fournisseur » pour *supplier* |
| release / release series / series | version / série de versions / série | |
| maintained / unmaintained / end of life | Maintained / Unmaintained / End of Life | Statuts upstream conservés |
| upgrade / rolling upgrade | mise à niveau / mise à niveau progressive sans interruption | « montée de version » accepté dans le corps du texte |
| patch / patching | correctif / application des correctifs | « patch » conservé pour un *local patch* porté par la plateforme |
| live migration / cold migration / evacuation / to evacuate | migration à chaud / migration à froid / évacuation / évacuer | |
| fencing / to fence | fencing / isoler (par fencing) | Glosé « mise hors circuit forcée » à la première occurrence |
| compute host / compute node / hypervisor | hôte de calcul / nœud de calcul / hyperviseur | |
| compute service | service compute | `nova-compute` |
| message bus | bus de messages | |
| database cluster / quorum | cluster de bases de données / quorum | |
| port binding | binding du port | |
| scheduling / to schedule | ordonnancement / ordonnancer | « placer » accepté pour *to place* |
| allocation / resource provider / inventory | allocation / resource provider / inventaire | Placement |
| workload / instance / VM | charge de travail / instance / VM | |
| tenant / consumer / consuming team | tenant / consommateur / équipe consommatrice | |
| user / operator / engineer / platform engineer | utilisateur / opérateur / ingénieur / ingénieur plateforme | |
| platform team / platform lead / sponsor | équipe plateforme / responsable de plateforme / sponsor | |
| first-line operations / escalation | exploitation de premier niveau / escalade | |
| incident leader | responsable d’incident | |
| ownership / owner | propriété / propriétaire | « responsable » quand « propriétaire » serait ambigu |
| accountability / accountable | responsabilité / responsable (de rendre compte) | Ch. 12 : *ownership* = propriété, *accountability* = responsabilité |
| operational / capability / platform technical accountability | responsabilité opérationnelle / responsabilité d’une capacité / responsabilité technique de la plateforme | |
| decision rights / decision authority / decision owner | droits de décision / autorité de décision / décideur | |
| decision record / change decision record | fiche de décision / fiche de décision de changement | |
| debt register | registre de dette | |
| weighted scoring model / weighted decision model | modèle de notation pondérée / modèle de décision pondéré | |
| decision gate | porte de décision | |
| business impact / risk / criticality / owner / value | impact métier / risque métier / criticité métier / propriétaire métier / valeur métier | |
| business continuity | continuité d’activité | |
| maintenance window / change window | fenêtre de maintenance / fenêtre de changement | |
| change capacity / operational capacity / spare capacity | capacité de changement / capacité opérationnelle / capacité de réserve | |
| handover / onboarding / knowledge transfer | passation / intégration / transfert de connaissances | |
| single-expert dependency / single point of failure | dépendance à un expert unique / point de défaillance unique | |
| redundancy of knowledge | redondance de la connaissance | |
| heroics | héroïsme | |
| observability / signal / baseline / threshold | observabilité / signal / référence (baseline) / seuil | |
| dashboard / monitoring stack | tableau de bord / pile de supervision | |
| health check / "everything is green" | contrôle de santé / « tout est au vert » | |
| request id | identifiant de requête | |
| security advisory (OSSA) | avis de sécurité (OSSA) | |
| policy (RBAC) / persona | politique d’autorisation (policy) / persona | |
| certificate rotation / key rotation | rotation des certificats / rotation des clés | |
| steal time / CPU pinning / pinned CPU | steal time / épinglage des CPU (pinning) / CPU dédié | « steal » conservé, glosé « temps volé » |
| roadmap / horizon / target state | feuille de route / horizon / état cible | |
| transition / lifecycle event / lifecycle | transition / événement de cycle de vie / cycle de vie | |
| simplification / divergence | simplification / divergence | |
| automation / semi-automation / dry run | automatisation / semi-automatisation / exécution à blanc (*dry run*) | |
| evidence / assumption / hypothesis | preuve (élément de preuve) / hypothèse non vérifiée / hypothèse | « preuve » au sens de *evidence* : ce qui est observé |
| the field / from the field | le terrain / sur le terrain | |
| control gap | lacune de contrôle | Jamais « faille » ni « manque » |
| operator / operations team / RUN | opérateur / équipe d’exploitation / RUN | |
| disruptive (action, decision, recovery) | perturbateur, perturbatrice | |
| liveness | signal de vie (liveness) | |
| resumption / to resume (a stopped change) | redémarrage / reprendre | Distinct de *recovery* = reprise |
| sustainable workload (of a team) | charge de travail de l’équipe soutenable | Distinct de *workload* = charge de travail hébergée |
| network fabric | réseau physique (fabric) | |
| to discard (transactions, messages) | écarter | |
| endpoint | endpoint | Conservé |
| key / certificate rotation | rotation (renouvellement) des clés / des certificats | Jamais « faire tourner » |
| load balancer / virtual IP (VIP) | répartiteur de charge / IP virtuelle (VIP) | |
| rollback | retour arrière | |
| heartbeat (lost heartbeat) | battement de cœur (heartbeat) | |
| primary / secondary (knowledge) | titulaire / suppléant | Chapitre 12 |
| fact / hypothesis / assumption | fait / hypothèse / présupposé | Chapitre 9 |
| bootstrap (Galera) | bootstrap / bootstraper | Conservé |
| quorum queue / classic mirrored queue | file quorum (*quorum queue*) / file classique en miroir | |
| mechanism driver / resource provider / scaling journey | conservés en anglais | Noms de concepts OpenStack |
| credentials | secrets (identifiants, clés) | Chapitre 17 |
| failure domain | domaine de défaillance | |
| capacity planning | planification de capacité | |
| cherry-pick | *cherry-pick* | Conservé, en italique |
| the business | le métier / l’entreprise | selon le contexte |
| Contents (navigation) | Sommaire | |
| Front matter | Pages liminaires | |

## Processus de traduction d’un chapitre

1. Partir du fichier anglais à jour (`git log -1 -- chapters/NN-….md`) ; le fichier français mentionne en tête de commit la révision anglaise suivie.
2. Traduire paragraphe par paragraphe, sans fusionner ni scinder les paragraphes, en gardant chaque encadré, chaque liste, chaque tableau et chaque figure à sa place.
3. Appliquer la terminologie et la typographie ci-dessus.
4. Exécuter `python3 tools/check_editions.py` (parité de structure, liens, typographie) puis `bash tools/pdf/build.sh fr` et `python3 tools/pdf/verify_pdf.py build/openstack-the-day-after-tomorrow-fr.pdf build/openstack-the-day-after-tomorrow-fr.log`.
5. Relire le chapitre en français seul, sans l’original, pour la fluidité.
