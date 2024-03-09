pip install google
from googlesearch import search

def find_song(lyrics):
    query = f"{lyrics} site:genius.com"  # searching specifically on Genius.com
    search_results = search(query, num_results=5, stop=5, pause=2)

    if search_results:
        print("Here are some search results for the song lyrics:")
        for result in search_results:
            print(result)
    else:
        print("No results found for the given lyrics.")

def main():
    lyrics = input("Enter the lyrics of the song: ")
    find_song(lyrics)

if __name__ == "__main__":
    main()
