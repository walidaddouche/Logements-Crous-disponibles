import json

data = [
  {
    "id": "00dea68c-12d8-11e8-89ed-005056940822",
    "name": "Sainte-Clotilde"
  },
  {
    "id": "02af10bb-082d-11e8-89ed-005056940822",
    "name": "Aubière- Campus des Cézeaux (63)"
  },
  {
    "id": "05bb29c3-12d8-11e8-89ed-005056940822",
    "name": "Saint-Pierre"
  },
  {
    "id": "05c9f258-f139-11e7-89ed-005056940822",
    "name": "Toulouse Sud-Est"
  },
  {
    "id": "0a6d6de8-12d8-11e8-89ed-005056940822",
    "name": "Tampon"
  },
  {
    "id": "0b4d6860-f139-11e7-89ed-005056940822",
    "name": "Albi"
  },
  {
    "id": "0d8c4849-ff82-11e7-89ed-005056940822",
    "name": "Paris"
  },
  {
    "id": "0e624bb9-f139-11e7-89ed-005056940822",
    "name": "Castres"
  },
  {
    "id": "0ee94faa-082d-11e8-89ed-005056940822",
    "name": "Montluçon (03)"
  },
  {
    "id": "0f0d4f26-fac2-11e7-89ed-005056940822",
    "name": "Amiens nord"
  },
  {
    "id": "117bea25-c285-11ea-b2a6-005056941f86",
    "name": "KREMLIN BICETRE"
  },
  {
    "id": "11a051df-f139-11e7-89ed-005056940822",
    "name": "Figeac"
  },
  {
    "id": "120d6a33-0059-11e8-89ed-005056940822",
    "name": "CRETEIL"
  },
  {
    "id": "13aaf9a0-06a4-11e8-89ed-005056940822",
    "name": "ORSAY"
  },
  {
    "id": "149bc9d4-027c-11e8-89ed-005056940822",
    "name": "POITIERS"
  },
  {
    "id": "149f3985-f6d3-11e7-89ed-005056940822",
    "name": "Rouen"
  },
  {
    "id": "14c2fabd-f139-11e7-89ed-005056940822",
    "name": "Millau"
  },
  {
    "id": "193fc8a0-f139-11e7-89ed-005056940822",
    "name": "Tarbes"
  },
  {
    "id": "1ad46486-7328-11e9-a02d-005056941f86",
    "name": "Rouen"
  },
  {
    "id": "1b7ff80f-01d0-11e8-89ed-005056940822",
    "name": "Nancy - Centre"
  },
  {
    "id": "1be96d42-76de-11e9-a02d-005056941f86",
    "name": "Montbéliard"
  },
  {
    "id": "1f691dd4-fac2-11e7-89ed-005056940822",
    "name": "Amiens centre"
  },
  {
    "id": "2123483b-7328-11e9-a02d-005056941f86",
    "name": "Le Havre"
  },
  {
    "id": "223d9d02-ff55-11e7-89ed-005056940822",
    "name": "Boulogne-sur-Mer"
  },
  {
    "id": "22b88d60-01d0-11e8-89ed-005056940822",
    "name": "Nancy - Sciences et Technologies / Artem"
  },
  {
    "id": "2476e510-f16a-11e7-89ed-005056940822",
    "name": "Saint-Etienne"
  },
  {
    "id": "2627c0c1-ff55-11e7-89ed-005056940822",
    "name": "Dunkerque"
  },
  {
    "id": "272b6a44-22f0-11e8-89ed-005056940822",
    "name": "Rodez"
  },
  {
    "id": "27c516f7-7328-11e9-a02d-005056941f86",
    "name": "Evreux"
  },
  {
    "id": "28aede91-f9e8-11e7-89ed-005056940822",
    "name": "Agglomération Niçoise et Cagnes/Mer"
  },
  {
    "id": "2a1da2ca-07f1-11e8-89ed-005056940822",
    "name": "SITE DU FUTUROSCOPE"
  },
  {
    "id": "2bd2092b-fac2-11e7-89ed-005056940822",
    "name": "Amiens sud"
  },
  {
    "id": "2c30b63c-f16a-11e7-89ed-005056940822",
    "name": "Roanne"
  },
  {
    "id": "2f007457-1153-11e8-89ed-005056940822",
    "name": "Montpellier Nord"
  },
  {
    "id": "2f9306a7-3bfe-11e8-89ed-005056940822",
    "name": "Site Auxerre"
  },
  {
    "id": "3109e773-3bfd-11e8-89ed-005056940822",
    "name": "Service Appartements Dijon"
  },
  {
    "id": "3243ae5b-fac2-11e7-89ed-005056940822",
    "name": "Beauvais"
  },
  {
    "id": "32804f06-ff55-11e7-89ed-005056940822",
    "name": "Longuenesse - Saint Omer"
  },
  {
    "id": "32afce9d-f16a-11e7-89ed-005056940822",
    "name": "Bourg-en-Bresse"
  },
  {
    "id": "35256054-ff55-11e7-89ed-005056940822",
    "name": "Arras"
  },
  {
    "id": "35773249-f9e8-11e7-89ed-005056940822",
    "name": "Antibes et Valbonne"
  },
  {
    "id": "38e8c458-ff55-11e7-89ed-005056940822",
    "name": "Lens"
  },
  {
    "id": "3bd247ee-ff55-11e7-89ed-005056940822",
    "name": "Béthune"
  },
  {
    "id": "3dfe7f36-116b-11e8-89ed-005056940822",
    "name": "Perpignan sud"
  },
  {
    "id": "41b4a6fb-0111-11e8-89ed-005056940822",
    "name": "FONTAINEBLEAU"
  },
  {
    "id": "4435ee81-ff55-11e7-89ed-005056940822",
    "name": "Valenciennes"
  },
  {
    "id": "46fe05f9-ff55-11e7-89ed-005056940822",
    "name": "Cambrai"
  },
  {
    "id": "491488ab-116b-11e8-89ed-005056940822",
    "name": "Perpignan"
  },
  {
    "id": "4aa431b0-f5e5-11e7-89ed-005056940822",
    "name": "Rennes"
  },
  {
    "id": "4c278f8d-0cd9-11e8-89ed-005056940822",
    "name": "Tulle"
  },
  {
    "id": "4cc59d1f-fac3-11e7-89ed-005056940822",
    "name": "Compiègne"
  },
  {
    "id": "4e30f5b2-1b01-11e8-89ed-005056940822",
    "name": "COTE BASQUE"
  },
  {
    "id": "4f7c4598-ff55-11e7-89ed-005056940822",
    "name": "Roubaix - Tourcoing"
  },
  {
    "id": "50635d12-0cd9-11e8-89ed-005056940822",
    "name": "Felletin"
  },
  {
    "id": "514ff66b-fad1-11e7-89ed-005056940822",
    "name": "Limoges"
  },
  {
    "id": "517abd45-07f1-11e8-89ed-005056940822",
    "name": "LA ROCHELLE"
  },
  {
    "id": "5181aba4-fac3-11e7-89ed-005056940822",
    "name": "Creil"
  },
  {
    "id": "52fd4227-f9e8-11e7-89ed-005056940822",
    "name": "Toulon et Alentours"
  },
  {
    "id": "55736b54-01b9-11e8-89ed-005056940822",
    "name": "Metz -  Technopole / Bridoux"
  },
  {
    "id": "5606a5a7-e590-11e7-89a3-005056940822",
    "name": "Toulouse Centre - Ouest"
  },
  {
    "id": "560ba45b-fad1-11e7-89ed-005056940822",
    "name": "Egletons"
  },
  {
    "id": "56dff816-0c34-11e8-89ed-005056940822",
    "name": "Cannes"
  },
  {
    "id": "57f5e1d3-fac3-11e7-89ed-005056940822",
    "name": "Saint-Quentin"
  },
  {
    "id": "589389fa-0c1c-11e8-89ed-005056940822",
    "name": "Pointe-à-Pitre - Bergevin"
  },
  {
    "id": "59037108-fad1-11e7-89ed-005056940822",
    "name": "Brive"
  },
  {
    "id": "5a1af6f5-f5e5-11e7-89ed-005056940822",
    "name": "Saint-Brieuc"
  },
  {
    "id": "5bb5d550-34ed-11e9-a02d-005056941f86",
    "name": "Aurillac (15)"
  },
  {
    "id": "5ce2151c-faa5-11e7-89ed-005056940822",
    "name": "Troyes"
  },
  {
    "id": "5d989218-f5e5-11e7-89ed-005056940822",
    "name": "Lannion"
  },
  {
    "id": "61415017-010d-11e8-89ed-005056940822",
    "name": "CACHAN"
  },
  {
    "id": "6156d06d-f73a-11e7-89ed-005056940822",
    "name": "Pointe-à-Pitre - Fouillole"
  },
  {
    "id": "61f09426-0111-11e8-89ed-005056940822",
    "name": "MARNE-LA-VALLEE_77"
  },
  {
    "id": "648f5f48-faa5-11e7-89ed-005056940822",
    "name": "Reims"
  },
  {
    "id": "675180dc-07f1-11e8-89ed-005056940822",
    "name": "ANGOULEME"
  },
  {
    "id": "697691c1-f73a-11e7-89ed-005056940822",
    "name": "Saint-Claude - Morne Houël"
  },
  {
    "id": "70c094e8-07f1-11e8-89ed-005056940822",
    "name": "NIORT"
  },
  {
    "id": "72020832-f0a1-11e7-89ed-005056940822",
    "name": "ISERE - Grenoble et agglomération grenobloise"
  },
  {
    "id": "7680063c-ff57-11e7-89ed-005056940822",
    "name": "SENART_77"
  },
  {
    "id": "7753bdbb-ff54-11e7-89ed-005056940822",
    "name": "Calais"
  },
  {
    "id": "7895821e-0757-11e8-89ed-005056940822",
    "name": "ORLEANS"
  },
  {
    "id": "7ba4d6f2-f73a-11e7-89ed-005056940822",
    "name": "Schoelcher - Campus de Schœlcher"
  },
  {
    "id": "7f172f65-f5e5-11e7-89ed-005056940822",
    "name": "Brest"
  },
  {
    "id": "803f809d-211e-11e8-89ed-005056940822",
    "name": "SAVOIE - Le bourget du Lac"
  },
  {
    "id": "8080c10b-116f-11e8-89ed-005056940822",
    "name": "Nîmes"
  },
  {
    "id": "824cec9a-f5e5-11e7-89ed-005056940822",
    "name": "Quimper"
  },
  {
    "id": "8310f1cc-0757-11e8-89ed-005056940822",
    "name": "TOURS"
  },
  {
    "id": "8648d62f-f73a-11e7-89ed-005056940822",
    "name": "Cayenne - Baduel"
  },
  {
    "id": "87b6c875-0757-11e8-89ed-005056940822",
    "name": "BLOIS"
  },
  {
    "id": "89f92c77-116f-11e8-89ed-005056940822",
    "name": "Nîmes Ouest"
  },
  {
    "id": "8b081b40-072d-11e8-89ed-005056940822",
    "name": "Strasbourg"
  },
  {
    "id": "8d889f42-f73a-11e7-89ed-005056940822",
    "name": "Kourou - Branly"
  },
  {
    "id": "8e901881-072d-11e8-89ed-005056940822",
    "name": "Mulhouse"
  },
  {
    "id": "8ea53d0f-0757-11e8-89ed-005056940822",
    "name": "CHATEAUROUX"
  },
  {
    "id": "8f74c338-0c1d-11e8-89ed-005056940822",
    "name": "Cayenne - Troubiran"
  },
  {
    "id": "91694c6d-f5e5-11e7-89ed-005056940822",
    "name": "Lorient"
  },
  {
    "id": "91b1ebc4-116f-11e8-89ed-005056940822",
    "name": "Nîmes Sud"
  },
  {
    "id": "91dbeb0f-e72d-11e7-89a3-005056940822",
    "name": "Chalons"
  },
  {
    "id": "93a3b915-0757-11e8-89ed-005056940822",
    "name": "BOURGES"
  },
  {
    "id": "94ffba8b-01cf-11e8-89ed-005056940822",
    "name": "Metz -  Saulcy"
  },
  {
    "id": "9507496c-f5e5-11e7-89ed-005056940822",
    "name": "Vannes"
  },
  {
    "id": "961050a0-23a2-11e8-89ed-005056940822",
    "name": "Le Puy et environs (43)"
  },
  {
    "id": "9798285d-1197-11e8-89ed-005056940822",
    "name": "Marseille Etoile"
  },
  {
    "id": "98860955-0757-11e8-89ed-005056940822",
    "name": "ISSOUDUN"
  },
  {
    "id": "98a2b6c6-f0a1-11e7-89ed-005056940822",
    "name": "HAUTE SAVOIE - Annecy"
  },
  {
    "id": "99be1f67-f6d4-11e7-89ed-005056940822",
    "name": "SAVOIE - Chambéry"
  },
  {
    "id": "9b177074-fad3-11e7-89ed-005056940822",
    "name": "PAU"
  },
  {
    "id": "a25dd862-0757-11e8-89ed-005056940822",
    "name": "CHARTRES"
  },
  {
    "id": "a2b67860-f6d4-11e7-89ed-005056940822",
    "name": "DROME - Valence"
  },
  {
    "id": "a33d5c23-acc1-11eb-9dc0-005056941f86",
    "name": "Campus Cité Scientifique"
  },
  {
    "id": "a53a9bac-3d52-11e8-89ed-005056940822",
    "name": "Thiers (63)"
  },
  {
    "id": "a712e586-e72d-11e7-89a3-005056940822",
    "name": "Charleville Mézières"
  },
  {
    "id": "a7da2a94-fc69-11e7-89ed-005056940822",
    "name": "EVRY"
  },
  {
    "id": "ab74a306-fbc1-11e7-89ed-005056940822",
    "name": "Aix-en-Provence"
  },
  {
    "id": "abbaba78-1153-11e8-89ed-005056940822",
    "name": "Montpellier"
  },
  {
    "id": "acce37aa-1197-11e8-89ed-005056940822",
    "name": "Marseille Timone"
  },
  {
    "id": "aeefa371-76dd-11e9-a02d-005056941f86",
    "name": "Besançon"
  },
  {
    "id": "afef4b26-1646-11e8-89ed-005056940822",
    "name": "BORDEAUX METROPOLE"
  },
  {
    "id": "b0d3a59d-3bfd-11e8-89ed-005056940822",
    "name": "Site LE CREUSOT"
  },
  {
    "id": "b0f5e091-fbc1-11e7-89ed-005056940822",
    "name": "Marseille Centre"
  },
  {
    "id": "b40e9291-76dd-11e9-a02d-005056941f86",
    "name": "Belfort"
  },
  {
    "id": "b42ab758-f9f9-11e7-89ed-005056940822",
    "name": "Angers"
  },
  {
    "id": "b4a95b1e-1197-11e8-89ed-005056940822",
    "name": "Marseille Luminy"
  },
  {
    "id": "b5dd6fa1-fd31-11e7-89ed-005056940822",
    "name": "Besançon"
  },
  {
    "id": "b7c4824c-fbc1-11e7-89ed-005056940822",
    "name": "Avignon"
  },
  {
    "id": "b9690902-76dd-11e9-a02d-005056941f86",
    "name": "Le Creusot"
  },
  {
    "id": "b98779b2-f606-11e7-89ed-005056940822",
    "name": "DAX"
  },
  {
    "id": "ba11d7a4-acc1-11eb-9dc0-005056941f86",
    "name": "Campus Pont de Bois"
  },
  {
    "id": "baf63695-7327-11e9-a02d-005056941f86",
    "name": "Caen"
  },
  {
    "id": "bd1dd869-f606-11e7-89ed-005056940822",
    "name": "MONT DE MARSAN"
  },
  {
    "id": "bd4b3bdf-76dd-11e9-a02d-005056941f86",
    "name": "Dijon"
  },
  {
    "id": "bf531da4-fd31-11e7-89ed-005056940822",
    "name": "Belfort"
  },
  {
    "id": "c0f8411e-acc1-11eb-9dc0-005056941f86",
    "name": "Campus Santé"
  },
  {
    "id": "c19e4e07-388b-11ec-b5ad-005056941f86",
    "name": "Mende"
  },
  {
    "id": "c207ffd2-f9f9-11e7-89ed-005056940822",
    "name": "Nantes"
  },
  {
    "id": "c26f5b65-39db-11e9-a02d-005056941f86",
    "name": "Marcy l'Etoile"
  },
  {
    "id": "c43db84f-fd31-11e7-89ed-005056940822",
    "name": "Montbéliard"
  },
  {
    "id": "c6990496-f606-11e7-89ed-005056940822",
    "name": "AGEN"
  },
  {
    "id": "c7b5bd33-0a87-11e8-89ed-005056940822",
    "name": "HAUTS-DE-BIEVRE"
  },
  {
    "id": "c8584134-f9f9-11e7-89ed-005056940822",
    "name": "Le Mans"
  },
  {
    "id": "c9ebe70c-22be-11e8-89ed-005056940822",
    "name": "Blagnac"
  },
  {
    "id": "ca8898ff-f606-11e7-89ed-005056940822",
    "name": "PERIGUEUX"
  },
  {
    "id": "cad2f243-00e5-11e8-89ed-005056940822",
    "name": "Campus Moulins-Ronchin"
  },
  {
    "id": "caff0075-1153-11e8-89ed-005056940822",
    "name": "Montpellier Sud"
  },
  {
    "id": "cb21592d-0111-11e8-89ed-005056940822",
    "name": "SEINE-SAINT-DENIS_93"
  },
  {
    "id": "cf9c3121-f9f9-11e7-89ed-005056940822",
    "name": "Saint Nazaire"
  },
  {
    "id": "d0665de1-f453-11e7-89ed-005056940822",
    "name": "Caen"
  },
  {
    "id": "d5961472-7327-11e9-a02d-005056941f86",
    "name": "Hérouville - périphérie de Caen"
  },
  {
    "id": "d70034eb-f9f9-11e7-89ed-005056940822",
    "name": "Laval"
  },
  {
    "id": "d7ef6d57-f9d6-11e7-89ed-005056940822",
    "name": "Le Havre"
  },
  {
    "id": "d9cd1191-01cf-11e8-89ed-005056940822",
    "name": "Longwy"
  },
  {
    "id": "dae708ae-f9d6-11e7-89ed-005056940822",
    "name": "Evreux"
  },
  {
    "id": "dbe1133a-f9f9-11e7-89ed-005056940822",
    "name": "La Roche Sur Yon"
  },
  {
    "id": "de48e07b-01cf-11e8-89ed-005056940822",
    "name": "Yutz"
  },
  {
    "id": "de54af71-0b40-11e8-89ed-005056940822",
    "name": "Mariani"
  },
  {
    "id": "e46e91c6-0a87-11e8-89ed-005056940822",
    "name": "VERSAILLES -ST-QUENTIN"
  },
  {
    "id": "e4fe5048-fe1e-11e7-89ed-005056940822",
    "name": "Saint-claude - Desmarais"
  },
  {
    "id": "e6db45b5-01cf-11e8-89ed-005056940822",
    "name": "Sarreguemines"
  },
  {
    "id": "e889d1f4-0a87-11e8-89ed-005056940822",
    "name": "CERGY"
  },
  {
    "id": "ed66968b-3bfd-11e8-89ed-005056940822",
    "name": "Pôle Hébergement Dijon"
  },
  {
    "id": "ed7f0ce6-0a87-11e8-89ed-005056940822",
    "name": "NANTERRE"
  },
  {
    "id": "eda935f8-f453-11e7-89ed-005056940822",
    "name": "Hérouville - périphérie de Caen"
  },
  {
    "id": "eee37f63-082c-11e8-89ed-005056940822",
    "name": "Clermont-Ferrand (63)"
  },
  {
    "id": "f02ef2cc-0b40-11e8-89ed-005056940822",
    "name": "Grimaldi"
  },
  {
    "id": "f832702a-01cf-11e8-89ed-005056940822",
    "name": "Nancy - Lettres / Droit"
  },
  {
    "id": "fa305212-f154-11e7-89ed-005056940822",
    "name": "Lyon - Villeurbanne et Saint-Priest"
  },
  {
    "id": "fc63c78a-76dd-11e9-a02d-005056941f86",
    "name": "Auxerre"
  }
]

for ele in data:
    print(ele.get("id") + " -> " + ele.get("name"))
