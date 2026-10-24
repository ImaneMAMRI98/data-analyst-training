--REQUETES D'INSERTIONS --



INSERT INTO Categorie (Categorie_id, Categorie_nom) VALUES
('CAT-FONT', 'Fontaine à eau'),
('CAT-PARK', 'Parking vélos'),
('CAT-TOIL', 'Toilettes publiques');


INSERT INTO Zone (Zone_id, Zone_nom) VALUES
('ZONE-CENTRE', 'Centre-Ville historique'),
('ZONE-GARE', 'Quartier de la Gare'),
('ZONE-PARC', 'Secteur Parc Floral');



INSERT INTO Citoyen (User_id, User_email, User_mdp, User_name) VALUES
('CIT-001', 'lucas.martin@email.fr', 'motdepasse99', 'Lucas Martin'),
('CIT-002', 'lea.r@email.fr', 'secretPass45', 'Léa Rouvière'),
('CIT-003', 'amine.d@email.fr', 'securite2026!', 'Amine Diallo'),
('CIT-004', 'sofia.b@email.fr', 'pass2026sofia', 'Sofia Benali'),
('CIT-005', 'thomas.k@email.fr', 'kT45secure', 'Thomas Kowalski'),
('CIT-006', 'nadia.f@email.fr', 'nadiaF!2026', 'Nadia Fontaine'),
('CIT-007', 'paul.m@email.fr', 'paulM_88', 'Paul Mercier'),
('CIT-008', 'chloe.v@email.fr', 'chloeV2026', 'Chloé Vasseur'),
('CIT-009', 'youssef.t@email.fr', 'yt_secure45', 'Youssef Tahiri'),
('CIT-010', 'emma.l@email.fr', 'emmaL_pass', 'Emma Lefèvre');



INSERT INTO Lieu (Lieu_id, Lieu_latitude, Lieu_longtitude, Zone_id, Categorie_id) VALUES
('LIEU-001', 44.558225, 4.750512, 'ZONE-GARE', 'CAT-PARK'),
('LIEU-002', 44.561100, 4.748900, 'ZONE-CENTRE', 'CAT-FONT'),
('LIEU-003', 44.555400, 4.752100, 'ZONE-PARC', 'CAT-TOIL'),
('LIEU-004', 44.559000, 4.751000, NULL, 'CAT-FONT'),
('LIEU-005', 44.560300, 4.747600, 'ZONE-CENTRE', 'CAT-TOIL'),
('LIEU-006', 44.557800, 4.753400, 'ZONE-PARC', 'CAT-PARK'),
('LIEU-007', 44.562500, 4.749800, 'ZONE-GARE', 'CAT-FONT'),
('LIEU-008', 44.556100, 4.750900, 'ZONE-PARC', 'CAT-FONT'),
('LIEU-009', 44.563200, 4.752700, 'ZONE-GARE', 'CAT-TOIL'),
('LIEU-010', 44.554900, 4.748300, NULL, 'CAT-PARK');



INSERT INTO Demande (Demande_id, Demande_type, Demande_description, Demande_date, Lieu_id, User_id) VALUES
('DEM-001', 'Proposition', 'Nouveau parking vélo installé ce matin.', '2026-06-15 09:30:00', 'LIEU-001', 'CIT-001'),
('DEM-002', 'Modification', 'Signalement : la fontaine ne fonctionne plus.', '2026-06-16 14:15:00', 'LIEU-002', 'CIT-003'),
('DEM-003', 'Proposition', 'Demande d''ajout des sanitaires du parc.', '2026-06-18 11:00:00', 'LIEU-003', 'CIT-002'),
('DEM-004', 'Modification', 'Fontaine hors-zone difficile à localiser sur la carte.', '2026-06-19 08:45:00', 'LIEU-004', 'CIT-004'),
('DEM-005', 'Proposition', 'Suggestion d''un nouveau point d''eau près de la gare.', '2026-06-19 16:20:00', 'LIEU-007', 'CIT-005'),
('DEM-006', 'Modification', 'Toilettes fermées plus tôt que prévu le soir.', '2026-06-20 18:05:00', 'LIEU-005', 'CIT-006'),
('DEM-007', 'Proposition', 'Ajout d''un parking vélo supplémentaire au parc.', '2026-06-20 10:10:00', 'LIEU-006', 'CIT-007'),
('DEM-008', 'Modification', 'Fontaine de la gare avec faible débit d''eau.', '2026-06-21 07:50:00', 'LIEU-007', 'CIT-008'),
('DEM-009', 'Proposition', 'Demande de signalétique pour les toilettes du parc.', '2026-06-21 12:30:00', 'LIEU-003', 'CIT-009'),
('DEM-010', 'Modification', 'Parking vélo endommagé après les intempéries.', '2026-06-22 09:00:00', 'LIEU-001', 'CIT-010'),
('DEM-011', 'Proposition', 'Nouvelle fontaine à ajouter secteur Parc Floral.', '2026-06-22 15:40:00', 'LIEU-008', 'CIT-001'),
('DEM-012', 'Modification', 'Coordonnées GPS imprécises pour ce lieu.', '2026-06-23 10:25:00', 'LIEU-010', 'CIT-002'),
('DEM-013', 'Proposition', 'Demande de toilettes publiques côté gare.', '2026-06-23 13:55:00', 'LIEU-009', 'CIT-003'),
('DEM-014', 'Modification', 'Fontaine centre-ville tachée, nettoyage nécessaire.', '2026-06-24 08:15:00', 'LIEU-002', 'CIT-004'),
('DEM-015', 'Proposition', 'Ajout d''un parking vélo sécurisé hors-zone.', '2026-06-24 17:00:00', 'LIEU-010', 'CIT-005'),
('DEM-016', 'Modification', 'Toilettes du centre-ville à rouvrir le dimanche.', '2026-06-25 11:30:00', 'LIEU-005', 'CIT-006'),
('DEM-017', 'Proposition', 'Suggestion d''une fontaine supplémentaire au parc.', '2026-06-25 14:45:00', 'LIEU-008', 'CIT-007'),
('DEM-018', 'Modification', 'Parking vélo du parc trop petit aux heures de pointe.', '2026-06-26 09:10:00', 'LIEU-006', 'CIT-008'),
('DEM-019', 'Proposition', 'Demande de fontaine à hauteur réduite pour enfants.', '2026-06-26 16:35:00', 'LIEU-007', 'CIT-009'),
('DEM-020', 'Modification', 'Toilettes de la gare sans papier régulièrement.', '2026-06-27 10:00:00', 'LIEU-009', 'CIT-010'),
('DEM-021', 'Proposition', 'Ajout d''un éclairage près du parking vélo gare.', '2026-06-27 19:20:00', 'LIEU-001', 'CIT-001'),
('DEM-022', 'Modification', 'Fontaine hors-zone à raccorder au réseau principal.', '2026-06-28 08:40:00', 'LIEU-004', 'CIT-002');



--REQUETES DE SELECTION--

SELECT * FROM Citoyen;

SELECT User_email, User_name FROM Citoyen;


--REQUETES DE MISE A JOUR--

UPDATE citoyen 
SET  user_name = 'SOFIA BENALI' 
WHERE user_id = 'CIT-004';

--REQUETES DE SUPPRESSION--

DELETE FROM demande 
WHERE demande_id ='DEM-022';


--REQUETES DE JOUNTURES--

SELECT 
    D.Demande_id, 
    D.Demande_type, 
    D.Demande_description, 
    D.Demande_date,
    C.User_name AS Citoyen,
    C.User_email,
    L.Lieu_id,
    L.Lieu_latitude,
    L.Lieu_longtitude
FROM Demande D
JOIN Citoyen C ON D.User_id = C.User_id
JOIN Lieu L ON D.Lieu_id = L.Lieu_id
ORDER BY D.Demande_date DESC;

--REQUETES D'AGRÉGATION--

SELECT COUNT(demande_type)
FROM demande 
GROUP BY demande_type ;