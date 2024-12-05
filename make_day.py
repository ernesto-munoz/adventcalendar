import os
import argparse
import requests
from pathlib import Path

COOKIE_KEY = "ADVENT_OF_CODE_COOKIE"

def download_input(input_path:Path, year:int, day:int) -> None:
    if COOKIE_KEY not in os.environ.keys():
        print(f"No cookie {COOKIE_KEY} found in the environment settings. It will not downlaod the input.")
        return
    
    try:
        url = f"https://adventofcode.com/{year}/day/{day}/input"
        print(f"Downloading input file from {url}")
        cookie = os.environ[COOKIE_KEY]  # easiest way

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            'Cookie': f'session={cookie}'
        }
        session = requests.Session()
        response = session.get(url, headers=headers)
        response.raise_for_status()
            
        with open(input_path, "wb") as f:
            f.write(response.content)
            
        print(f"Downloaded input file in {input_path}")
    except Exception as e:
        print(f"Failed to download file: {e}")

def create_contest_day(year:int, day:int) -> None:
    folder:Path = Path().resolve() / str(year) / f"day{day}"
    if folder.exists() is False:
        print(f"Create folder {folder}")
        folder.mkdir(parents=True)  # create the strcuture if needed
    
    code_path: Path = folder / f"day{day}.py"
    test_path: Path = folder / f"test.txt"
    input_path: Path = folder / f"input.txt"
    if code_path.exists() is False:
        code_path.touch()
        print(f"Created file {code_path}")
    if test_path.exists() is False:
        test_path.touch()
        print(f"Created file {test_path}")
    download_input(input_path, year, day)

def main() -> None:
    parser = argparse.ArgumentParser(description="Create year and day for the Advent of Code.")
    parser.add_argument("-year", type=int, help="Year of the contest")
    parser.add_argument("-day", type=int, help="Day of the contest")
    args = parser.parse_args()
    create_contest_day(year=args.year, day=args.day)
    
if __name__ == "__main__":
    main()
    # Usage: python make_day.py -year 2024 -day 1