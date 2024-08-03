import requests
import os

def fetch_uris(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        # Extract URIs from the data
        uris = [item[1]['uri'] for item in data if len(item) > 1]
        return uris
    except requests.RequestException as e:
        print(f"Failed to fetch data from {url}: {e}")
        return []

def filter_uris(uris):
    # Filter out URIs ending with .onion or .i2p
    return [uri for uri in uris if not (uri.endswith('.onion') or uri.endswith('.i2p'))]

def save_uris(filename, uris):
    with open(filename, 'w') as file:
        for uri in uris:
            # Clean URL: remove `https://` and `/api/v1/stats`
            clean_url = uri.replace('https://', '').replace('/api/v1/stats', '')
            file.write(f"{clean_url}\n")

def main():
    # Define URLs for different sorting criteria
    urls = {
        "Health": "https://api.invidious.io/instances.json?pretty=1&sort_by=health",
        "Ratio_api": "https://api.invidious.io/instances.json?pretty=1&sort_by=api",
        "Most_users": "https://api.invidious.io/instances.json?pretty=1&sort_by=users",
        "Cors": "https://api.invidious.io/instances.json?pretty=1&sort_by=cors"
    }

    output_dir = "output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Fetch and save URIs for each sorting criterion
    for key, url in urls.items():
        print(f"Fetching URIs from {url}...")
        uris = fetch_uris(url)
        filtered_uris = filter_uris(uris)
        if filtered_uris:
            filename = os.path.join(output_dir, f"{key}_uris.txt")
            save_uris(filename, filtered_uris)
            print(f"Saved {len(filtered_uris)} URIs to {filename}")
        else:
            print(f"No URIs fetched for {key}")

if __name__ == "__main__":
    main()
