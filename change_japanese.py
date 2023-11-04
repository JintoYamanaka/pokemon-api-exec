import requests

# ポケモンAPIのベースURL
BASE_URL = "https://pokeapi.co/api/v2/"

def get_pokemon_japanese_name(english_name):
    # ポケモン種（Species）のエンドポイントを叩く
    response = requests.get(BASE_URL + f'pokemon-species/{english_name.lower()}')
    if response.ok:
        data = response.json()
        
        # 日本語名を検索
        for name_info in data['names']:
            if name_info['language']['name'] == 'ja-Hrkt':  # 日本語名を探す
                return name_info['name']
        # 日本語名が見つからない場合
        return "日本語名が見つかりません。"
    else:
        # APIリクエストが失敗した場合
        return "ポケモンの情報を取得できませんでした。"

# 使用例
english_name = "Bulbasaur"  # 英語名を入力
japanese_name = get_pokemon_japanese_name(english_name)
print(f"{english_name}の日本語名: {japanese_name}")
