Title: Key signing party au Capitole du Libre
Date: 2016-11-05
Summary: Comment participer la fête de signature de clef gpg/pgp au cdl

Cette année la Key signing party pour clef gpg/pgp se deroulera comme pour le [FOSDEM](http://fosdem.org). C'est à dire qu'il faudra s'inscrire à l'avance, mais que cela simplifera considérablement la partie administrative d'un tel évènement.

La ksp aura lieu le **dimanche 20 Novembre 2016 à 12:30** ; Rdv dans l'amphithéatre  B00.

La méthode du FOSDEM permet de se débarasser des empreintes de clef individuelles et donc de la possibilité de perdre les petits bouts de papier.

## Inscription

Après avoir créé une clef comme indiqué à [https://keyring.debian.org/creating-key.html], il suffit d'envoyer la clef comme ceci:

```
[ludo@Oulanl ~]$ gpg --keyserver ksp.capitoledulibre.org --send-key 6B17EA1E
gpg: sending key 6B17EA1E to hkp server ksp.capitoledulibre.org
[ludo@Oulanl ~]$
```

en prenant soin d'envoyer votre clef et pas la mienne (6B17EA1E).

On peut s'inscrire jusqu'au mercredi 16 novembre 2016. Cela donne un peu de temps aux administrateurs pour générer les fichiers nécessaires à la KSP.

### Pour ceux qui n'ont pas de clef

Le **mardi 8 novembre à 18:30** au [centre culturel Bellegarde](http://bellegarde.toulouse.fr/) aura lieu un
**[atelier](http://blog.capitoledulibre.org/2016/11-07-introduction-a-la-cryptographie-avant-le-capitole-du-libre.html)
pour créer une clef et prendre en main gpg**.

## Avant de venir au Capitole du Libre

Se connecter à [http://ksp.capitoledulibre.org/files] pour y télécharger le fichiers des participants et leurs clefs.  Il faudra vérifier le fichier en utilisant les commandes fournies et les noter dans ledit fichiers. Après on peut soit l'imprimer, soit venir avec son portable et assez de temps de batterie (il faut compter 1 heure par 100 participants).

## Le jour même

Venir à 12:30 dans l'amphithéatre B00. Nous lirons les CRC des fichiers et vous pourrez vérfifer que vos fichiers sont les bons. Puis nous expliquerons la marche à suivre pour la suite. Merci de venir avec un justificatif d'identité officiel.
