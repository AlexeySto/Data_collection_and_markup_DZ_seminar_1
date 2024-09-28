import requests


def get_venues(category, client_id, client_secret, v):
    url = "https://api.foursquare.com/v2/venues/search"
    params = {
        "near": "Moscow", # Замените на нужный вам город
        "query": category,
        "client_id": client_id,
        "client_secret": client_secret,
        "v": v
    }
    response = requests.get(url, params=params)
    return response.json()

def main():
    client_id = "ВАШ_CLIENT_ID"
    client_secret = "ВАШ_CLIENT_SECRET"
    version = "20231001" # Дата версии API

    category = input("Введите интересующую вас категорию (например, кофейни, музеи): ")

    venues_data = get_venues(category, client_id, client_secret, version)
    if 'response' in venues_data and 'venues' in venues_data['response']:
        venues = venues_data['response']['venues']
        if venues:
            for venue in venues:
                name = venue['name']
                address = ', '.join(venue['location'].get('formattedAddress', 'Адрес не найден'))
                rating = venue.get('rating', 'Рейтинг не указан')
                print(f"Название: {name}, Адрес: {address}, Рейтинг: {rating}")
        else:
            print("Заведения не найдены.")
    else:
        print("Произошла ошибка при обработке запроса.")

if __name__ == "__main__":
    main()
