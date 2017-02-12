"""Usage:
  control add <url>
  control remove <url>
"""

from docopt import docopt
from control import add_website_to_block_list, remove_website_from_block_list, add_website_to_block_list_for_duration

def run():
    args = docopt(__doc__)

    if args.get("add"):
        add_website_to_block_list(args.get("<url>"))
    elif args.get("remove"):
        remove_website_from_block_list(args.get("<url>"))
    else:
        print("Invalid query.")
