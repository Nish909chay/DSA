from pytube import Playlist
playlist_url = "https://youtube.com/playlist?list=PLDzeHZWIZsTr3nwuTegHLa2qlI81QweYG"
playlist = Playlist(playlist_url)
with open("ids.txt", "w") as f:
    for url in playlist.video_urls:
        video_id = url.split("v=")[-1].split("&")[0]
        f.write(video_id + "\n")