import os
import requests

def fetch_and_save(url, filename):
    response = requests.get(url)
    response.raise_for_status()
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(response.text)

def main():
    base_url = 'https://www.santaisabel.cl'
    output_dir = 'files'
    os.makedirs(output_dir, exist_ok=True)

    # Descargar y guardar robots.txt
    robots_url = f'{base_url}/robots.txt'
    robots_file = os.path.join(output_dir, 'robots.txt')
    fetch_and_save(robots_url, robots_file)

    # Descargar y guardar home.html
    home_url = base_url
    home_file = os.path.join(output_dir, 'home.html')
    fetch_and_save(home_url, home_file)

if __name__ == '__main__':
    main()
