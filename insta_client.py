from insta_client import Client

username, password = "testingg", "hi3333"

client = Client()
client.login(username, password)

hashtag = "programming"

medias = client.hashtag_medias_recent(hashtag, 20)

for i, media in enumerate(medias):
    client.media_like(media.id)
    print(f"Liked post number {i+1} of hashtag {hashtag}")