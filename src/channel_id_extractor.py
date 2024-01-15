import re
from typing import Optional

import requests
from bs4 import BeautifulSoup


def http_request(url: str) -> Optional[requests.models.Response]:
    """
    This function makes a http request to the URL provided.
    
    Parameters
    ----------
    url: str

    Returns
    -------
    requests.models.Response or None
    """
    try:
        resp = requests.get(url = url)
    except Exception as args:
        print(f"Error: requests.get returned an error: \n{args.args}")
        return None
    else:
        wrong_url = "This video isn\'t available any more"
        not_found = "404 Not Found"
        if wrong_url in resp.text:
            print(
                f'Error: Please check the URL/text provided. It returned "'
                f'{wrong_url}"')
            return None
        elif not_found in resp.text:
            print(
                f'Error: Please check the URL/text provided. It returned "'
                f'{not_found}"')
            return None
        else:
            return resp


def channel_id_frm_video_url(video_url: str) -> Optional[str]:
    """
    This function extracts the YouTube channel ID from a given YouTube video
    URL.

    Parameters
    ----------
    video_url: str
        Example: "https://www.youtube.com/watch?v=5U0BwH5WefU"

    Returns
    -------
    str or None
    
    Examples
    --------
    >>> video_url = "https://www.youtube.com/watch?v=r2wBcCIlMGw"
    >>> channel_id_frm_video_url(video_url = video_url)
    'UCCj956IF62FbT7Gouszaj9w'
    >>> video_url = "https://www.youtube.com/watch?v=VideoDontExist"
    >>> channel_id_frm_video_url(video_url = video_url)
    None
    """
    resp = http_request(url = video_url)
    if not resp:
        return None
    channel_id = re.search('"channelIds":\[".+"\]', resp.text)
    channel_id = re.findall('\["(.+)"\]', str(channel_id))
    return channel_id[0]


def channel_id_frm_other_than_video_url(user_text: str) -> Optional[str]:
    """
    This function extracts the YouTube channel ID from a given YouTube
    channel name or channel homepage URL.

    Parameters
    ----------
    user_text: str
        Example: "@BBC"
                 "BBC"
                 "https://www.youtube.com/@BBC"
                 "https://www.youtube.com/@BBC/videos"

    Returns
    -------
    str or None
    
    Examples
    --------
    >>> user_text = "@BBC"
    >>> channel_id_frm_other_than_video_url(user_text = user_text)
    'UCCj956IF62FbT7Gouszaj9w'
    >>> user_text = "BBC"
    >>> channel_id_frm_other_than_video_url(user_text = user_text)
    'UCCj956IF62FbT7Gouszaj9w'
    >>> user_text = "https://www.youtube.com/@BBC"
    >>> channel_id_frm_other_than_video_url(user_text = user_text)
    'UCCj956IF62FbT7Gouszaj9w'
    >>> user_text = "https://www.youtube.com/@BBC/videos"
    >>> channel_id_frm_other_than_video_url(user_text = user_text)
    'UCCj956IF62FbT7Gouszaj9w'
    >>> user_text = "Channel Don't Exist"
    >>> channel_id_frm_other_than_video_url(user_text = user_text)
    None
    
    """
    try:
        user_text = [w for w in user_text.split('/') if "@" in w][0]
    except IndexError as _:
        user_text = f'@{user_text}'
    finally:
        url = f'https://www.youtube.com/{user_text}/videos'

    resp = http_request(url = url)

    if not resp:
        return None

    soup = BeautifulSoup(resp.text, 'html.parser')
    channel_id = soup.find_all('meta', {'itemprop': 'identifier'})
    channel_id = channel_id[0].get('content')

    return channel_id
