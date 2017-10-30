import sys
import time
import argparse

from req.github import Github
from document import Document

def main(args):

    args = _parse_args(args)
    print(args)

    """ TODO Replace below with proper argument parser
    # Check for query param
    if len(args) < 2:
        print("Error: Run hackerman with a query parameter")
        print("  eg: ./bin/hackerman hackhackhack")
        exit(1)

    # Strip away superfluous args
    args = args[1]
    """

    exit(1)

    gh    = Github()
    resp  = gh.search(args)

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

            # Dump raw text from each file in repo
            raw_text = gh.get_raw(download_url)
            doc = Document(raw_text)
            doc.type()

def _parse_args(argv):
    """ Parse and Validate arguments
    :param argv: argument(s) from init
    :return args: parsed, validated argument(s)
    """

    parser = argparse.ArgumentParser(prog="hackerman",
                                     usage="%(prog)s [options]")
    parser.add_argument("-q", "--query",
                        help="general string to search for using Github API",
                        type=str)
    parser.add_argument("-l", "--query-language",
                        help="programming language to filter results by (eg: cpp)",
                        type=str)
    parser.add_argument("-w", "--wpm",
                        help="typing speed in words per minute",
                        type=int)

    return parser.parse_args()


if __name__ == "__main__": main(sys.argv)
