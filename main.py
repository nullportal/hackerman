import sys
import time

from req.github import Github

def main(args):

    # Strip away superfluous args
    args = args[1]

    gh    = Github()
    resp  = gh.search(args)
    items = resp["items"]

    for item in items:
        contents = gh.get_contents(item["contents_url"])
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
            print(raw_text)

        # XXX Keep from spamming GH
        break


if __name__ == "__main__": main(sys.argv)
