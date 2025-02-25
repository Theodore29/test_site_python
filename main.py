import requests

nom_commune = input(str('quelle est le nom de la commune'))

url ="https://geo.api.gouv.fr/communes"

parm={
    'nom' : nom_commune
}

reponse = requests.get(url,params=parm)

if reponse.status_code == 200: 
    rep_json=reponse.json()
    all_cp_lists = [entry['codesPostaux'] for entry in rep_json]
    max_list = max(all_cp_lists, key=len)

    # Afficher le résultat
    print(max_list)