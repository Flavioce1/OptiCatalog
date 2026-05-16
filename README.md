# OptiCatalog

> Un agent conseiller multicritère pour opticiens.

*Document de vision produit — projet en cours de développement.*

---

## Le problème

Choisir le bon verre pour un client est un acte technique qui mobilise simultanément plusieurs dimensions : la correction prescrite, les caractéristiques de la monture retenue, les besoins réels du client (sport, conduite, écran, lecture), le catalogue du fabricant avec ses gammes et ses traitements, et enfin la mutuelle du client avec les partenariats du magasin.

Un seul catalogue fabricant peut atteindre 80 pages. Un magasin travaille en général avec plusieurs fabricants et doit composer avec des dizaines de mutuelles différentes. La combinatoire est telle qu'aucun professionnel — même expérimenté — ne la maîtrise mentalement dans son intégralité.

Conséquences observées au quotidien : recommandations sous-optimales, ventes ratées par méconnaissance d'une gamme pourtant adaptée, temps perdu à feuilleter des catalogues PDF au comptoir devant le client.

## La solution

OptiCatalog est un agent qui automatise ce raisonnement multicritère. À partir d'un brief client structuré — correction, monture choisie, usage et préférences, mutuelle — l'agent recommande la combinaison verre + traitements + gamme la mieux adaptée.

Chaque recommandation est argumentée et sourcée : pour chaque option proposée, l'agent cite la page exacte du catalogue fabricant qui justifie son choix. Quand la mutuelle est renseignée, le reste à charge est calculé précisément.

L'outil ne remplace pas l'opticien diplômé. Il l'assiste sur la partie combinatoire, lui rendant disponible le temps de la relation client et de la validation experte.

## Pour qui

| Profil | Bénéfice principal |
|---|---|
| Vendeur en magasin sans diplôme | Un guide qui propose les bonnes options sans devoir maîtriser toute la technique des verres |
| Opticien junior diplômé | Validation rapide de l'intuition et apprentissage continu des subtilités par gamme |
| Opticien senior | Comparaison rapide entre gammes et entre fabricants pour argumenter efficacement face au client |
| Gérant de magasin | Meilleur taux de transformation, panier moyen plus élevé, montée en compétence de l'équipe |

## Cas d'usage concrets

### Recommandation après essayage de la monture

> Au comptoir : le vendeur a saisi la correction et choisi la monture avec la cliente. Il décrit son profil — *femme 45 ans, myope -2.50 avec addition 1.50, monture nylor moyen format, conduite urbaine et 7h par jour d'écran*. En quelques secondes, OptiCatalog propose 3 options classées, avec un argumentaire sourcé pour chacune.

### Comparaison rapide entre deux gammes

> L'opticien hésite entre deux gammes premium pour un client sportif qui pratique le trail en montagne. Il demande la comparaison fine. OptiCatalog produit une réponse différenciée en citant pour chaque argument la page du catalogue fabricant.

### Calcul du reste à charge

> Le client demande combien il paie réellement après remboursement. L'agent croise la recommandation avec la mutuelle déclarée et le partenariat de tiers payant actif dans le magasin, et retourne le reste à charge exact.

## Comment ça marche

OptiCatalog repose sur quatre principes.

**Premièrement**, l'outil lit les catalogues fabricants une fois pour toutes et en construit une bibliothèque interrogeable par sens, pas seulement par mots-clés. Demander *"verre adapté à un sportif en montagne"* retrouve les gammes pertinentes même si le catalogue n'emploie pas exactement ces mots.

**Deuxièmement**, l'outil vérifie systématiquement la compatibilité physique entre le verre envisagé et la monture choisie. Ces règles sont encodées explicitement, à partir du savoir métier d'un opticien, et non devinées par un modèle.

**Troisièmement**, l'outil croise chaque candidat avec la mutuelle du client et la grille de remboursement applicable. Le calcul est exact à l'euro, pas une estimation.

**Quatrièmement**, l'agent classe les options finales selon un score multicritère explicite : adéquation à la correction, adéquation à l'usage, reste à charge, préférences du client. Les pondérations sont configurables par le gérant du magasin selon sa stratégie commerciale.

## Ce qui rend OptiCatalog différent

**Sources citées systématiquement.** Chaque argument renvoie à une page exacte d'un catalogue identifié. Aucune recommandation à l'aveugle.

**Scoring explicite et configurable.** Les critères de classement et leurs poids sont lisibles dans un fichier de configuration, pas cachés dans une boîte noire. Le gérant peut ajuster selon sa stratégie commerciale.

**Règles métier vérifiées, pas devinées.** La compatibilité monture/verre s'appuie sur des règles encodées explicitement par un opticien et testées une par une.

**Calcul de reste à charge exact.** Pas d'estimation. La grille de remboursement de chaque mutuelle est explicitement renseignée et croisée avec le partenariat de tiers payant actif.

## Approche légale et confidentialité

OptiCatalog adopte une posture prudente sur deux points sensibles.

**Copyright des catalogues fabricants.** Aucun catalogue réel n'est redistribué avec l'outil. Les démonstrations publiques utilisent des catalogues entièrement synthétiques d'un fabricant fictif. L'utilisateur professionnel dépose ses propres catalogues localement, dans un espace privé qui ne quitte jamais le magasin.

**Données client et RGPD.** Aucune donnée client n'est conservée par défaut. La correction visuelle est une donnée de santé et traitée comme telle. Un mode de sauvegarde locale chiffrée est prévu pour les magasins qui souhaitent conserver l'historique des recommandations à fin d'audit.

**Statut de l'outil.** OptiCatalog assiste l'opticien diplômé. Il ne produit pas un devis légal et ne remplace pas la validation experte. La signature finale reste celle du professionnel diplômé.

## À propos

Je suis Flavien Hue, opticien diplômé en exercice et en reconversion vers les métiers de l'ingénierie logicielle appliquée aux modèles de langue. OptiCatalog est né du constat répété, au comptoir, qu'une part significative de la valeur de l'opticien se joue dans cette combinatoire que les outils existants ne soutiennent pas.

Le projet sert à la fois de portfolio technique pour ma reconversion et de contribution potentielle à la profession. Il est développé en évolution continue.
