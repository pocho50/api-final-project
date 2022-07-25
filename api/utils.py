import os, io, re, requests
import hashlib
import settings
from middleware import model_predict
from pytube import YouTube 

def allowed_file(filename):
    """
    Checks if the format for the file received is acceptable. For this
    particular case, we must accept only image files.

    Parameters
    ----------
    filename : str
        Filename from werkzeug.datastructures.FileStorage file.

    Returns
    -------
    bool
        True if the file is an image, False otherwise.
    """

    split_file = os.path.splitext(filename)
    return str(split_file[1]).lower() in [".mp4", ".webm", ".ogg"]

def allowed_url(url):
    """
    Checks if the url youtube format is valid.

    Parameters
    ----------
    url : str
        the youtube url.

    Returns
    -------
    bool
        True if the url is valid, False otherwise.
    """    
    youtube_regex = (r'(https?://)?(www\.)?'
                    '(youtube|youtu|youtube-nocookie)\.(com|be)/'
                    '(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')  
    
    youtube_regex_match = re.match(youtube_regex, url)
    #devolver youtube_regex_match

    if(youtube_regex_match):
        return True

    return False


def directory_file_hash(file):
    """
    Returns a new filename based on the file content using MD5 hashing.
    It uses hashlib.md5() function from Python standard library to get
    the hash.

    Parameters
    ----------
    file : werkzeug.datastructures.FileStorage
        File sent by user.

    Returns
    -------
    str
        The directory where the file must be saved.
    str
        New filename based in md5 file hash.
    """

    split_file = os.path.splitext(file.filename)
    data = file.read()
    md5hash = hashlib.md5(data).hexdigest()
    file.seek(0)

    return str(md5hash), str(md5hash) + str(split_file[1])

def process_youtube_url(url):
    """
    It process the youtube url video with the library pytube, it saves the video as mp4
    Returns a new filename based on the file content using MD5 hashing.
    It uses hashlib.md5() function from Python standard library to get
    the hash.

    Parameters
    ----------
    file : werkzeug.datastructures.FileStorage
        File sent by user.

    Returns
    -------
    str
        The directory where the file must be saved.
    str
        New filename based in md5 file hash.
    """    

    buf = io.BytesIO()
    
    yt = YouTube(url)

    # we get the mp4 from youtube 
    stream = yt.streams.filter(progressive=True, file_extension='mp4') \
                       .get_lowest_resolution()

    # we save the file in memory
    stream.stream_to_buffer(buf)
    buf.seek(0)
    # read the file
    data = buf.read()
    # get the md5
    md5hash = hashlib.md5(data).hexdigest()
    buf.seek(0)

    # generate the filename
    filename = str(md5hash) + '.mp4'

    # create directory for the file
    os.makedirs(os.path.join(settings.UPLOAD_FOLDER, md5hash), exist_ok = True)

    # save the file in the directory
    stream.download(output_path=os.path.join(settings.UPLOAD_FOLDER, md5hash), 
                    filename=filename)
                    
    return str(md5hash), filename


def get_prediction(video_name):

    # the directory of the movie is the hash
    directory_movie = os.path.splitext(video_name)[0]

    # get the video path
    video_path = os.path.join(settings.UPLOAD_FOLDER, directory_movie, video_name)

    assert os.path.exists(
        os.path.join(video_path)
    ), f"The file doesn't exists"

    # we call model_predict from middleware to predict each scene
    info_scenes = model_predict(video_name)

    return info_scenes

