from uuid import uuid1

import requests


def download_file(file_url: str):
    response = requests.get(file_url)
    
    path = f'images/{uuid1()}.webp'
    with open(path, 'wb') as f:
        f.write(response.content)

    return path


def main() -> None:
    api_url = "https://dummyjson.com/products?limit=20"
    response = requests.get(api_url)
    response.raise_for_status()

    products_data = response.json()["products"]
    products = []
    for product in products_data:
        name = product["title"]
        image_url = product["thumbnail"]
        path = download_file(image_url)

        products.append({
            'name': name,
            'image': path
        })
    
    print(products)

main()
