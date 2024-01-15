from argparse import ArgumentParser, RawDescriptionHelpFormatter
import textwrap

parser = ArgumentParser(
    prog = "python3 -m main.py",
    formatter_class = RawDescriptionHelpFormatter,
    description = textwrap.dedent('''Use this script to extract the ID of a YouTube channel and to generate a RSS feed URL. 
    For this, you need to pass any of the following:
    1. a YouTube video URL ('https://www.youtube.com/watch?v=LMNopqrs')
    2. a channel name with a prefix '@' ('@abcxyz')
    3. a channel name without a prefix '@' ('abcxyz')
    4. a complete channel URL ('https://www.youtube.com/@abcxyz)
    '''),
    epilog = textwrap.dedent('''Examples:
    1. python3 -m main.py https://www.youtube.com/watch?v=LMNopqrs
    2. python3 -m main.py @abcxyz
    3. python3 -m main.py abcxyz
    4. python3 -m main.py https://www.youtube.com/@abcxyz
    
    To add @BBC YouTube channel to your RSS feed, executing the line below:
    $ python3 -m main.py https://www.youtube.com/@BBC
    will return this url that can be used in RSS feed: "https://www.youtube.com/feeds/videos.xml?channel_id=UCCj956IF62FbT7Gouszaj9w"
    ''')
)

parser.add_argument(dest = 'text',
                    type = str,
                    help = "text to parse")
