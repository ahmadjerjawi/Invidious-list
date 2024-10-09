import requests
import os

# Fetch URIs from the provided URL
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

# Filter out URIs ending with .onion or .i2p
def filter_uris(uris):
    return [uri for uri in uris if not (uri.endswith('.onion') or uri.endswith('.i2p'))]

# Save the filtered URIs to a file
def save_uris(filename, uris):
    with open(filename, 'w') as file:
        for uri in uris:
            # Clean URL: remove `https://` and `/api/v1/stats`
            clean_url = uri.replace('https://', '').replace('/api/v1/stats', '')
            file.write(f"{clean_url}\n")

# Fetch the latest version of the YouTube app from iTunes Search API
def fetch_youtube_version():
    youtube_api_url = "https://itunes.apple.com/lookup?id=544007664"
    try:
        response = requests.get(youtube_api_url)
        response.raise_for_status()
        data = response.json()
        if data["resultCount"] > 0:
            version = data["results"][0]["version"]
            return version
        else:
            print("No data found for YouTube app.")
            return None
    except requests.RequestException as e:
        print(f"Failed to fetch YouTube version: {e}")
        return None

# Save YouTube version to the output file
def save_youtube_version(filename, version):
    with open(filename, 'w') as file:
        file.write(version)

# Main function to fetch and save URIs and YouTube version
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

    # Fetch the latest YouTube app version
    print("Fetching YouTube version...")
    youtube_version = fetch_youtube_version()
    if youtube_version:
        youtube_version_file = os.path.join(output_dir, "youtube-version")
        save_youtube_version(youtube_version_file, youtube_version)
        print(f"Saved YouTube version {youtube_version} to {youtube_version_file}")

if __name__ == "__main__":
    main()
