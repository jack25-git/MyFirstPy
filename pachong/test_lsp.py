import requests

target_url="https://www.pearvideo.com/video_1798742"
cont_id=target_url.split("_")[1]
sub_target_url=f"https://www.pearvideo.com/videoStatus.jsp?contId={cont_id}&mrd=0.9503192593839522"
header={
    "referer":"https://www.pearvideo.com/video_1798742",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
}

res=requests.get(sub_target_url,headers=header)
print(res.text)
dic=res.json()
src_utl=dic["videoInfo"]["videos"]["srcUrl"]
systime=dic["systemTime"]
video_url=src_utl.replace(systime,f"cont-{cont_id}")
print(video_url)

with open(f"{cont_id}.mp4","wb") as f:
    f.write(requests.get(video_url).content)

res.close()