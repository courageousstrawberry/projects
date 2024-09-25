from instagrapi import Client

username, password = "courageousstrawberry", "elenibetty"

client = Client()
client.login(username, password)

hashtag = "programming"

medias = client.hashtag_medias_recent(hashtag, 20)