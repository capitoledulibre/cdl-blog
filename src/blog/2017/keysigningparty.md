Title: Key signing party au Capitole du Libre
Date: 2017-10-16
Summary: Signature de clef PGP au Capitole du Libre

Comme l’année dernière, une *Key Signing Party* sur le modèle de celle du [FOSDEM](https://fosdem.org/2018/keysigning/)
se déroulera le **dimanche midi** en B00.

Cette année, ne ratez pas une chance de faire signer vos clefs RSA 4096 (minimum) par plusieurs développeurs Debian !

## Inscription

**NB: Le serveur d’inscription n’est pas encore ouvert !**

Après avoir créé une clef comme indiqué à [https://keyring.debian.org/creating-key.html], il suffit d'envoyer la clef
comme ceci:

```
[ludo@Oulanl ~]$ gpg --keyserver ksp.capitoledulibre.org --send-key 6B17EA1E
gpg: sending key 6B17EA1E to hkp server ksp.capitoledulibre.org
[ludo@Oulanl ~]$
```

En prenant soin d'envoyer votre clef et pas la mienne (6B17EA1E).

## Avant de venir au Capitole du Libre

**NB: Il faudra attendre la fermeture du serveur d’inscription, 3 jours avant l’évènement**

Télécharger le fichiers des participants et leurs clefs, le vérifier en utilisant les commandes fournies à l’intérieur
et noter le résultat. Ensuite, le jour J, on peut soit l'imprimer, soit venir avec portable et assez de batterie.

Si votre clef n’est pas dans ce fichier, vous pouvez tout de même vérifier les clefs des autres participants.
Cependant, pour qu’ils vérifient la votre, il vous faudra venir avec suffisamment de papier où sera imprimé la
sortie de `gpg --fingerprint <votre key-ID>`.

**NB: N’oubliez pas une pièce d’identité valide !**

## Statistiques sur la KSP de l’année dernière

Une [matrice de signatures](https://saurel.me/PGP/CdL16) est disponible. Si vous étiez présent, vérifiez que vos
signatures ont été prises en compte !
