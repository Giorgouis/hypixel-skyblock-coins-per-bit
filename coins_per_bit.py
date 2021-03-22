import asyncio
import requests
import sys
import argparse


bins = []
finished = False


async def find_in_page(page__: int, key: str, item_name: str, print_page: bool):
    global finished
    global currently_running
    try:
        page = requests.get(f'https://api.hypixel.net/skyblock/auctions?key={key}&page={page__}').json()
    except Exception:
        finished = True
    for auction_ in page['auctions']:
        try:
            if auction_['claimed']:
                continue
            else:
                if auction_['item_name'].lower() == item_name.lower():
                    try:
                        if auction_['bin']:
                            bins.append(int(auction_['starting_bid']))
                    except KeyError:
                        continue
        except KeyError:
            continue
    if print_page:
        if page__ % 10 == 0:
            print(f'Finished searching page {page__}')
    currently_running -= 1


something = 0
page_ = -1
currently_running = 0


def main():
    global page_
    try:
        loop = asyncio.get_event_loop()
        while not finished:
            page_ += 1
            a_func = loop.create_task(find_in_page(page_, args.key, args.name.replace('-', ' ').replace('_', '-'), args.output))
            h = loop.run_until_complete(a_func)

            if finished:
                loop.close()

    except Exception:
        pass
    except KeyboardInterrupt:
        print(f'Results so far: {round(min(bins) / args.bits, 3)} coins per bit for {args.name.replace("-", " ").replace("_", "-")}'
              f' if sold for {min(bins):,}')
        try:
            loop.close()
            sys.exit()
        except:
            pass

    finally:
        loop.close()

    print(f'Results: {round(min(bins) / args.bits, 3)} coins per bit for {args.name.replace("-", " ").replace("_", "-")}'
          f' if sold for {min(bins):,}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get coins per bit you\'ll earn if you sell something.'
                                                 ' This script searches in all'
                                                 'pages of the auction house so this proccess might take a while.')
    parser.add_argument('-n', '--name', type=str, help='Item name to find lowest bin for(instead of space use -'
                                                       ' and instead of - use _)')
    parser.add_argument('-k', '--key', type=str, help='Your Hypiel API key')
    parser.add_argument('-b', '--bits', type=int, help='Bits required to buy item')
    parser.add_argument('-o', '--output', help='Whether or not "Finshed searching page.." will be displayed.',
                        action='store_true')
    args = parser.parse_args()
    print(f'Started searching for lowest bin for {args.name.replace("-", " ").replace("_", "-")}')
    main()
