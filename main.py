from src.argument_parser import parser
from src.channel_id_extractor import channel_id_frm_video_url, \
    channel_id_frm_other_than_video_url


def main(user_input: str) -> None:
    """

    Parameters
    ----------
    user_input: str

    Returns
    -------
    None

    """
    channel_id = (
        channel_id_frm_video_url(video_url = user_input)
        if 'watch?v=' in user_input
        else channel_id_frm_other_than_video_url(user_text = user_input)
    )
    if channel_id:
        print(
            f"https://www.youtube.com/feeds/videos.xml?channel_id="
            f"{channel_id}")
    return None


if __name__ == '__main__':
    args = parser.parse_args()
    main(user_input = args.text)
