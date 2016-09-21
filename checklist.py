"""
**********PROJET API WEB**********

Page = Fenêtre où on retrouve les articles d'un site Internet
Article = Un seul élément qui se retrouve sur une page Ex. un thread de Reddit

1. Fenêtre resizable
2. Menu en haut 
	a. Fichier : {À propos, Gestion des sites internet, Préférences, Quitter}
3. Gestion des site Internet
	a. Quels site internet présenter (ex. quel subreddit, quel partie de telle site)
	b. Afficher une liste des sites supportés quelque part
4. Interface graphique (regarder pour alternative à tkInter)
	a. Menu sur le haut du frame principal avec toutes les pages (MenuPages)
	b. Menu en haut (MenuHeading)
	c. Pas de boutons pour ajouter/supprimer/modifier : tout se fait par le MenuHeading
	d. Scrollable (si possible infini)
	e. Filtres disponibles sous forme de Combobox
	f. Boutons précédent
	g. Bouton Accueil
5. Features par rapport aux articles
	a. Dès qu'on click, l'article devient "Lu"
	b. Filtres (Tous / Lu / Non-lu / Dernières 24h)
	c. Montre un petit thumbnail
	d. Si le site l'offre, mettre des articles qui pourraient m'intéresser
6. Base de données
	a. Pour les sites inscrits dans l'application
7. Distribution de l'application
	a. Icone
	b. Permettre d'utiliser la base de donnée sur plusieurs ordinateurs (AWS? - voir free products)
	c. Le plus stand-alone possible
	d. Pas de console
8. Code
	a. Garder ca le plus rapide possible (limiter les for loop)
9. Sites internet compatibles
	a. Reddit
	b. Lapresse
	c. Sites de pharmacie
	d. Site de nouvelles américaines (économie, politique internationale)
	e. RDS


1. Trouver comment gérer la base de donnée pour pouvoir la distribuer avec le code
2. Trouver un nouveau module de GUI à la place tk
3. Faire un dessin de l'interface