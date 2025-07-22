from pytube import Playlist
playlist_url = "https://youtube.com/playlist?list=PLDzeHZWIZsTpukecmA2p5rhHM14bl2dHU" 
playlist = Playlist(playlist_url)
with open("dbms_ids.txt", "w") as f:
    for url in playlist.video_urls:
        video_id = url.split("v=")[-1].split("&")[0]
        f.write(video_id + "\n")