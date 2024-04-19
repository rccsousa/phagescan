import requests
import time
from typing import List, Dict, Union

def fetcher(url: str, json: bool = False) -> Union[Dict, requests.Response]:
    """
    Fetches data from the specified URL.
    
    Args:
        url (str): The URL from which to fetch the data.
        json (bool, optional): Whether to parse the response as JSON. Defaults to True.
    
    Returns:
        Union[Dict, requests.Response]: The fetched data, either as a dictionary (if json=True)
        or as a requests.Response object.
        
    Raises:
        ValueError: If the response status code is not 200.
    """
    resp = requests.get(url)
    if resp.status_code == 200:
        if json:
            return resp.json()
        else:
            return resp
    else:
        raise ValueError('Not found or forbidden')

def save_file(filename: str, data: bytes) -> None:
    """
    Saves data to a file.
    
    Args:
        filename (str): The name of the file to save the data to.
        data (bytes): The data to be saved.
    
    Returns:
        None
    """
    with open(filename, 'wb') as f:
        f.write(data)   

def downloader(url: str) -> None:
    """
    Downloads data from the specified URL and saves it to a file.
    
    Args:
        url (str): The URL from which to download the data.
    
    Returns:
        None
    """
    resp = fetcher(url)
    data = resp.content
    filename = url.split("/")[-1]
    save_file(filename, data)

def phage_catchr(phage_list: List[Dict[str, str]]) -> None:
    """
    Downloads files specified in a list of phage dictionaries.
    
    Args:
        phage_list (List[Dict[str, str]]): A list of dictionaries containing information about phages.
            Each dictionary should have keys 'em_file' and 'plaque_file' containing URLs of the files to download.
    
    Returns:
        None
    """
    for phage in phage_list:
        downloader(phage['em_file'])
        time.sleep(2)  # Wait for 2 seconds
        if phage['plaque_file']:
            downloader(phage['plaque_file'])
        time.sleep(2)  # Wait for 2 seconds





"""
Progress bar snippet

from tqdm import tqdm

uri = "https://phagesdb.org/api/phages/"

respo = requests.get(uri, stream = True)

size = int(respo.headers.get('content-length',0))
progress_bar = tqdm(total=size, unit='B', unit_scale=True, unit_divisor=1024)

for chunk in respo.iter_content(1024):
    progress_bar.update(len(chunk))

progress_bar.close()

"""
