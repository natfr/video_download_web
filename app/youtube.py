from pytube import YouTube


def youtube_info(url):
    """
    The function gets the info about a video by url
    """
    youtube = YouTube(url)
    youtube_info = {'title': youtube.title,
                    'author': youtube.author,
                    'length': youtube.length,
                    'views': youtube.views,
                    'rating': youtube.rating,
                    'description': youtube.description,
                    'image_url': youtube.thumbnail_url,
                    'youtube_link': url
                    }
    return youtube_info


def youtube_download(url):
    """
    The function returns links to video with different quality
    """
    youtube = YouTube(url)
    streams = youtube.streams.filter(progressive=True)  # progressive =audio+video

    video_download = []
    # print(streams)

    for i in streams:
        i = str(i).split()
        matching_res = [s for s in i if "res=" in s]
        res = matching_res[0].replace('"', '').replace('res=', '')

        matching_itag = [s for s in i if "itag=" in s]
        itag = matching_itag[0].replace('"', '').replace('itag=', '')

        link = youtube.streams.get_by_itag(itag=int(itag)).url
        size = round((youtube.streams.get_by_itag(itag=int(itag)).filesize_approx / 1000000), 2)

        video_info = [res, itag, link, size]
        video_download.append(video_info)

    return video_download


def youtube_download_local(url):
    """
    The function downloads a video from Youtube to a local computer
    """
    youtube = YouTube(url)
    streams = youtube.streams.filter(progressive=True)
    itags = []
    for i in streams:
        i = str(i).split()
        matching_itag = [s for s in i if "itag=" in s]
        itag = matching_itag[0].replace('"', '').replace('itag=', '')
        itags.append(itag)
    youtube.streams.get_by_itag(itag=int(itags[0])).download('video')

def get_embed(url):
    """
    The function returns an embed link for a video to show it on a webpage in iframe element
    """
    key=url.split('=')[1][0:11]
    link='https://www.youtube.com/embed/'+key
    return link


if __name__ == '__main__':
    url1 = 'https://www.youtube.com/watch?v=L3BUO3GJrj0'
    print(youtube_info(url1))
    print(youtube_download(url1))
    # youtube_download(url1)
    # youtube_download_local(url1)