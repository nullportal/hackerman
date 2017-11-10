import sys
import time
import signal
import argparse

from req.github import Github
from document import Document

# Don't spam terminal on <C-c>
class GracefulExit():
    def sigint_listen():
        """ For external use without import """
        signal.signal(signal.SIGINT, GracefulExit._graceful_exit)

    def _graceful_exit(signal, frame):
        """ Graceful exit on <C-c> """

        # Drain anything still in stdout buf
        sys.stdout.flush()

        # Print notice and exit
        print("\n -- ABORTING (reason: SIGINT) -- \n")
        sys.exit(0)
GracefulExit.sigint_listen()

def main(args):

    args  = _parse_args(args)
    gh    = Github(args.client_credentials)  # Init with client_id:client_secret, if present
    resp  = gh.search(args.query_str, args.query_lang)

    try:
        items = resp["items"]

    except Exception as e:
        print("Error querying Github:")
        for k,v in resp.items():
            print('\t', k+":", v)
        exit(1)


    for item in items:
        contents = gh.get_contents(item["contents_url"])
        #
        # TODO Handle {'message': 'This repository is empty.',
        #   'documentation_url': 'https://developer.github.com/v3/repos/contents/#get-contents'}
        #
        for content in contents:

            # TODO Just build a dict off of this outside of loop
            name         = content["name"]
            download_url = content["download_url"]  # Raw text

            # Don't dump lacunas
            if download_url is None:
                continue

            # Dump file name, path to file
            print(f"{name}: {download_url}")

            if _file_is_boring(name):
                continue

            # Dump raw text from each file in repo
            raw_text = gh.get_raw(download_url)

            try:
                doc = Document(raw_text)
                doc.type(args.typing_speed)
            except Exception:
                print("Whoa there!")

def _file_is_boring(f):
    """ Return whether a file looks boring or not """
    is_boring = False
    if   f.startswith('.'):
        is_boring = True
    elif f.endswith('.md'):
        is_boring = True
    elif "GEM" in f.upper():
        is_boring = True
    return is_boring

def _parse_args(argv):
    """ Parse and Validate arguments
    :param argv: argument(s) from init
    :return args: parsed, validated argument(s)
    """

    def positive(n):
        """ Ensure we receive a :n:umber equal to, or greater than, 1 """
        n = int(n)
        if n < 1:
            raise argparse.ArgumentTypeError(f"'{n}' invalid - must be a positive integer")
        return n

    parser = argparse.ArgumentParser(prog="hackerman",
                                     usage="%(prog)s [OPTS]")
    parser.add_argument("-q", "--query-str",
                        help="general string to search for using Github API",
                        default="mooo",
                        type=str)
    parser.add_argument("-l", "--query-lang",
                        help="programming language to filter results by (eg: cpp)",
                        default="oink",
                        type=str)
    parser.add_argument("-s", "--typing-speed",
                        help="typing",
                        default=1,
                        type=positive)
    parser.add_argument("-S", "--client-credentials",
                        help="string matching 'CLIENT_ID:CLIENT_SECRET', with proper id and secret",
                        default=None,
                        type=str)

    return parser.parse_args()


if __name__ == "__main__": main(sys.argv)

