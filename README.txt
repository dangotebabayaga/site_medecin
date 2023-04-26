POUR ACTIVER MON ENVIRONNEMENT VIRTUEL
conda activate myenv

<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2932.8767668943233!2d2.9019792758681273!3d42.68515267116459!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x12b06fced1c65913%3A0xcd7000245b6a4307!2s19%20Pl.%20de%20Montbolo%2C%2066100%20Perpignan!5e0!3m2!1sfr!2sfr!4v1682358878499!5m2!1sfr!2sfr" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>

https://doctolibpatient.zendesk.com/hc/fr?#section=1&article=3&content&source=internal_link

Pour installer ce package, exécutez l'une des actions suivantes postgresql :

>conda install -c anaconda postgresql
>conda install -c anaconda psycop2

- CREER LA BASE DE DONNEE pour le super User
>initdb -D bd_info_medecin
Nom de la base de donnée :  bd_info_medecin
Pass : toto

- CREER UN SUPER UTILISATEUR
>createuser --encrypted --pwprompt toto
pass toto

- DEMARRER LA BASE DE DONNEE
>pg_ctl -D bd_info_medecin -l logfile start

CREATION D4UNE BASE DE DONNEE EN INTERNE AVEC LE SUPERUNSER

>createdb --owner=toto bd_medecin
---------------------------------------------------------------
UTILISATEUR DJANGO
superuser : admin
mail: admin@gmail.com
pass: admin

