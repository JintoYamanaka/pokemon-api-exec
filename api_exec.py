import requests
import json
import time

# APIのベースURL
BASE_URL = "https://pokeapi.co/api/v2/"

# エンドポイントとそのクエリパラメータ
endpoints_with_params = {
    'ability': '1',  # IDで指定
    'characteristic': '1',  # IDで指定
    'egg-group': '1',  # IDで指定
    'gender': '1',  # IDで指定
    'growth-rate': '1',  # IDで指定
    'nature': '1',  # IDで指定
    'pokeathlon-stat': '1',  # IDで指定
    'pokemon': '1',  # IDで指定、"bulbasaur"などの名前でもOK
    'pokemon-color': '1',  # IDで指定
    'pokemon-form': '1',  # IDで指定
    'pokemon-habitat': '1',  # IDで指定
    'pokemon-shape': '1',  # IDで指定
    'pokemon-species': '1',  # IDで指定
    'stat': '1',  # IDで指定
    'type': '1',  # IDで指定
}

# データ取得とファイル保存の関数
def fetch_and_save_data(endpoint, param):
    url = f"{BASE_URL}{endpoint}/{param}/"
    response = requests.get(url)
    if response.ok:
        data = response.json()
        filename = f"{endpoint}_{param}.json"
        with open(filename, 'w') as file:
            json.dump(data, file, indent=2)
        print(f"Saved {filename}")
    else:
        print(f"Failed to retrieve data for {endpoint} with param {param}")

# メイン処理
def main():
    for endpoint, param in endpoints_with_params.items():
        fetch_and_save_data(endpoint, param)
        time.sleep(1)  # APIのレートリミットに配慮して1秒待機

if __name__ == "__main__":
    main()
