import requests

url ="https://geo.api.gouv.fr/communes"


def recherche(nom_commune):
    parm={
        'nom' : nom_commune
    }

    reponse = requests.get(url,params=parm)

    if reponse.status_code == 200: 
        rep_json=reponse.json()
        all_cp_lists = [entry['codesPostaux'] for entry in rep_json]
        max_list = max(all_cp_lists, key=len)

    return(max_list)


