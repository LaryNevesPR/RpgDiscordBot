import json
import os


async def Ler_Players():
    if os.path.exists('Recursos\Players.json'):
        with open('Recursos\Players.json', 'r', encoding='utf-8') as f:
            ilayers=json.load(f)
    return ilayers


async def salve_json(Player):
    with open('Recursos\Players.json','w', encoding='utf-8')as f:
        json.dump(Player, f, indent=2, ensure_ascii=False)