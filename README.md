# OnionScraper
                                                                                                
<h3> Description: </h3> 

OnionScraper est un script Python conçu pour récupérer le contenu des sites Web '.onion' sur le réseau Tor tout en utilisant le proxy Tor. Le script utilise la bibliothèque `requests` de python ainsi que le réseau Tor pour accéder aux sites web '.onion' et récupérer leur contenu. Il capture et enregistre également les cookies reçus du site Web pour une analyse plus approfondie.

<h3> Motivation: </h3> 

La motivation derrière OnionScraper est de fournir un moyen simple et automatisé d'accéder et de récupérer le contenu des sites Web '.onion' sur le réseau Tor. Cela peut être utile à diverses fins, y compris l'exploration du Web, la collecte de données et la recherche, tout en préservant l'anonymat et la confidentialité.

<h3> Caractéristiques: </h3>

  - Accédez aux sites web '.onion' sur le réseau Tor en utilisant le 'proxy' Tor.

  - Récupérez et enregistrez le contenu du site web dans un fichier.

  - Capturez et affichez les cookies reçus du site web.

<h3> Exigences essentielles: </h3>

  - Python 3.x
  - Bibliothèque Requests
  - Service Tor (en cours d'exécution sur localhost:9050)

<h3> Explication: </h3>

Le script `OnionScraper` commence par l'importation de la bibliothèque de requêtes nécessaire et définit une fonction nommée `access_onion_site(url, output_folder)` pour accéder et récupérer le contenu de l'URL '.onion' donnée. La fonction utilise le proxy Tor pour établir une connexion au réseau Tor et au site web .onion fourni.

Le script utilise ensuite une `request.Session()` pour faire une requête `GET` à l'URL .onion en utilisant le proxy Tor. Le contenu récupéré est enregistré dans un fichier nommé website_content.txt dans le dossier `output_folder` spécifié. De plus, les cookies reçus du site Web sont capturés à l'aide de l'attribut session.cookies et affichés sur le terminal.

<h3> Utilisation: </h3>

Cloner le dépôt: 

```bash
git clone https://github.com/Ferrerkomi/onion_scraper.git
```

Accéder au répertoire du projet:

```bash
cd onion_scraper
```

Installer les dépendances: 

installez les paquets Python requis en utilisant pip

```bash
pip install requests
```

Exécuter Onion Scraper: 

```bash
python3 onion_scraper.py http://example.onion/
```

_OnionScraper ouvre la porte à l'exploration du monde des sites web .onion sur le réseau Tor. Il vous permet de récupérer le contenu tout en préservant l'anonymat et la confidentialité. Que vous fassiez des recherches ou que vous soyez simplement curieux, OnionScraper vous permet d'accéder à du contenu caché sur le dark web en toute sécurité._

<h3> Contributions: </h3>

Les contributions au projet OnionScraper sont les bienvenues ! N'hésitez pas à bifurquer le référentiel, à apporter des améliorations et à soumettre des demandes.

<h3> Clause de non-responsabilité: </h3>

Veuillez noter que l'accès à certains sites web .onion peut être illégal ou contraire aux conditions d'utilisation. Utilisez ce script de manière responsable et conformément à toutes les lois et réglementations applicables.
