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
- [x] GET /users : Récupérer tous les utilisateurs
- [x] GET /user/:id : Récupérer un utilisateur
- [x] POST /user : Créer un utilisateur
- [x] PUT /user/:id : Modifier un utilisateur
- [x] DELETE /user/:id : Supprimer un utilisateur
- [] GET /user/:id/plannings : Récupérer tous les plannings d'un utilisateur
- [] GET /user/:id/planning/:id : Récupérer un planning d'un utilisateur
- [] POST /user/:id/planning : Créer une tache pour un utilisateur
- [] PUT /user/:id/planning/:id : Modifier une tache d'un utilisateur
- [] DELETE /user/:id/planning/:id : Supprimer une tache d'un utilisateur
- [] GET /user/:id/entreprise : Récupérer l'entreprise d'un utilisateur
- [] PUT /user/:id/entreprise : Modifier l'entreprise d'un utilisateur
- [] GET /user/:id/entreprise/plannings : Récupérer tous les taches d'une entreprise d'un utilisateur
