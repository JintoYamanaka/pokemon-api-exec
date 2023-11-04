import os
import requests
import json
import time

# APIのベースURL
BASE_URL = "https://pokeapi.co/api/v2/"

# エンドポイント
endpoints = [
    'ability', 'characteristic', 'egg-group', 'gender', 'growth-rate',
    'nature', 'pokeathlon-stat', 'pokemon', 'pokemon-color', 'pokemon-form',
    'pokemon-habitat', 'pokemon-shape', 'pokemon-species', 'stat', 'type'
]

# JSONを保存するディレクトリ
JSON_DIR = 'result'

# ディレクトリが存在しない場合は作成
os.makedirs(JSON_DIR, exist_ok=True)

# データ取得関数
def fetch_data(endpoint, param):
    url = f"{BASE_URL}{endpoint}/{param}/"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as errh:
        print(f"Http Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"OOps: Something Else: {err}")

# データ保存関数
def save_data(data, filename):
    file_path = os.path.join(JSON_DIR, filename)
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)
    print(f"Saved {file_path}")

# メイン処理
def main():
    for endpoint in endpoints:
        data = fetch_data(endpoint, '1')
        if data:
            filename = f"{endpoint}_1.json"
            save_data(data, filename)
            time.sleep(1)  # APIのレートリミットに配慮

if __name__ == "__main__":
    main()
