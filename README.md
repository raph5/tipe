
# Sujet de TIPE : Le rendu différentiel

**Problématique :** Comment le rendu différentiel peut aider les artistes 3d à recréer des materiaux du monde réel.


# Première Application

Pour prendre en main les sujet je vais créer un environnement où tester différentes techniques de rendu différentiel. Cet environnement consistera en un script go capable de rendre des objets simple comme des formes géométriques. L’objectif sera en suite de créer plusieurs algorithmes de rendu différentiel capables d’optimiser les paramètres de là scène pour atteindre un résultat souhaité.

Je vais maintenant passer en revue les principales composantes d'un algorithme de rendu différentiel.


## Le système de rendu et la scene

Je n'ai pas encore décidé comment j'allais implémenter précisément cette étape mais l'idée est de prendre un moteur de rendu minimaliste simple à configurer.


## L'optimisation des paramètres de la scène

Je vais utiliser un simple algorithme de descente de gradient :

$a_{n+1} = a_{n} - \lambda \operatorname{grad} f(a_{n})$

Il sera intéressant de tester différents algorithmes de descente de gradient
par la suite


## Différenciation

Je vais utiliser la différentiation automatique (cf cette [vidéo](https://www.youtube.com/watch?v=wG_nF1awSSY&list=PLqxYSyfpMvUKx_SQBFIBkKdLbbwBqi2Tp)).

## Mesures et documentation

A chaque itération du système de rendu il sera intéressant de garder une trace du rendu pour faire des timelapse. Il faudra aussi créer des metrics pour mesurer la performance de l'algorithme à chaque génération.


# Ressources

RGL [https://rgl.epfl.ch/publications/Loubet2019Reparameterizing](https://rgl.epfl.ch/publications/Loubet2019Reparameterizing)

État actuel de la recherche (2015) [https://arxiv.org/pdf/2006.12057.pdf](https://arxiv.org/pdf/2006.12057.pdf)

SoftRasterizer [https://vgl.ict.usc.edu/Software/SoftRasterizer/](https://vgl.ict.usc.edu/Software/SoftRasterizer/)

DIB-R [https://research.nvidia.com/labs/toronto-ai/DIB-R/](https://research.nvidia.com/labs/toronto-ai/DIB-R/)

[https://www.youtube.com/watch?v=T7w7QuYa4SQ](https://www.youtube.com/watch?v=T7w7QuYa4SQ)

[https://users.cg.tuwien.ac.at/zsolnai/gfx/gaussian-material-synthesis/](https://users.cg.tuwien.ac.at/zsolnai/gfx/gaussian-material-synthesis/)

[https://wandb.ai/wandb_fc/articles/reports/Part-I-Best-Practices-for-Picking-a-Machine-Learning-Model--Vmlldzo1NDU3NzY3](https://wandb.ai/wandb_fc/articles/reports/Part-I-Best-Practices-for-Picking-a-Machine-Learning-Model--Vmlldzo1NDU3NzY3)
