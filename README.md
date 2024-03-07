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
- [x] GET /user/{user_id}/usertask pour récupérer tous les user_task d'un utilisateur.
- [x] GET /user/{user_id}/usertask/{user_task} pour récupérer un user_task spécifique d'un utilisateur.
- [x] POST /user/{user_id}/planning/{task_id} pour créer un nouveau user_task pour un utilisateur et une tâche donnés.
- [x] DELETE /user/{user_id}/planning/{task_id} pour supprimer un user_task existant pour un utilisateur et une tâche donnés.
