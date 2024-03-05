ReadME

## Découpage du projet
- [x] Création du projet
- [x] Création de la base de données
- [x] Création des interfaces
- [x] Création des routes

## Routes du planning avec sa description
- [x] GET /planning : Récupérer tous les plannings
- [x] GET /planning/:id : Récupérer un planning
- [x] POST /planning : Créer un planning
- [x] PUT /planning/:id : Modifier un planning
- [x] DELETE /planning/:id : Supprimer un planning
- [x] GET /planning/:id/creneaux : Récupérer tous les créneaux d'un planning
- [x] GET /planning/:id/creneaux/:id : Récupérer un créneau d'un planning
- [x] POST /planning/:id/creneaux : Créer un créneau dans un planning
- [x] PUT /planning/:id/creneaux/:id : Modifier un créneau dans un planning
- [x] DELETE /planning/:id/creneaux/:id : Supprimer un créneau dans un planning

## Routes des entreprises avec sa description
- [x] GET /entreprises : Récupérer toutes les entreprises
- [x] GET /entreprise/:id : Récupérer une entreprise
- [x] POST /entreprise : Créer une entreprise
- [x] PUT /entreprise/:id : Modifier une entreprise
- [x] DELETE /entreprise/:id : Supprimer une entreprise

## Routes des utilisateurs avec sa description
- [x] GET /utilisateurs : Récupérer tous les utilisateurs
- [x] GET /utilisateur/:id : Récupérer un utilisateur
- [x] POST /utilisateur : Créer un utilisateur
- [x] PUT /utilisateur/:id : Modifier un utilisateur
- [x] DELETE /utilisateur/:id : Supprimer un utilisateur
- [x] GET /utilisateur/:id/planning : Récupérer tous les plannings d'un utilisateur
- [x] GET /utilisateur/:id/planning/:id : Récupérer un planning d'un utilisateur
- [x] POST /utilisateur/:id/planning : Créer une tache pour un utilisateur
- [x] PUT /utilisateur/:id/planning/:id : Modifier une tache d'un utilisateur
- [x] DELETE /utilisateur/:id/planning/:id : Supprimer une tache d'un utilisateur
- [x] GET /utilisateur/:id/entreprise : Récupérer l'entreprise d'un utilisateur
- [x] PUT /utilisateur/:id/entreprise : Modifier l'entreprise d'un utilisateur
- [x] DELETE /utilisateur/:id/entreprise : Supprimer l'entreprise d'un utilisateur
- [x] GET /utilisateur/:id/entreprise/planning : Récupérer tous les taches d'une entreprise d'un utilisateur