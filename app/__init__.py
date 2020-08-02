from flask import Flask, render_template, request
from flask_sitemap import Sitemap
from app.youtube import youtube_info, youtube_download, get_embed
from app.vk import get_vk_video

app = Flask(__name__)  # where __name__ is name of current file
#ext = Sitemap(app=app)
# http://127.0.0.1:5000/sitemap.xml for local host


@app.route('/')
def index():
    """
    The function returns a main page template to user
    """
    return render_template('index.html')

@app.route('/sitemap.xml')
def sitemap():
    """
    The function returns a sitemap page
    """
    return render_template('sitemap.xml')


# @app.route('/video_youtube', methods=['GET', 'POST'])
# def video_youtube():
#     """
#     The function collects user's request and returns a page with a result (Youtube video).
#     If the link is not related to youtube video, the function returns initial (blank) Video_youtube template.
#     """
#     try:
#         link = request.form['link']
#         info = youtube_info(link)
#         video_to_download = youtube_download(link)
#         embed = get_embed(link)
#         return render_template('video_youtube_download.html', info=info, video=video_to_download, embed=embed)
#     except:
#         return render_template('video_youtube.html')


@app.route('/video_youtube', methods=['GET', 'POST'])
def video_youtube():
    """
    The function collects user's request and returns a page with a result (Youtube video).
    If the link is not related to youtube video, the function returns initial (blank) Video_youtube template.
    """
    return render_template('video_youtube.html')

@app.route('/video_youtube_download', methods=['GET', 'POST'])
def video_youtube_download():
    """
    The function collects user's request and returns a page with a result (Youtube video).
    If the link is not related to youtube video, the function returns initial (blank) Video_youtube template.
    """
    link = request.form['link']
    print(link)
    info = youtube_info(link)
    print(info)
    video_to_download = youtube_download(link)
    print(video_to_download)
    embed = get_embed(link)
    print(embed)
    return render_template('video_youtube_download.html', info=info, video=video_to_download, embed=embed)







@app.route('/video_vk', methods=['GET', 'POST'])
def video_vk():
    """
    The function collects user's request and returns a page with a result (VK video).
    If the link is not related to VK video, the function returns initial (blank) Video_vk template.
    """
    try:
        link = request.form['link']
        vk_video = get_vk_video(link)
        return render_template('video_vk_download.html', vk_video=vk_video)
    except:
        vk_video = None
        return render_template('video_vk.html', vk_video=vk_video)


# if __name__ == '__main__':
#     app.run(debug=True)  # Flask втоматически незаметно рестартует сервер при изменении файлов
