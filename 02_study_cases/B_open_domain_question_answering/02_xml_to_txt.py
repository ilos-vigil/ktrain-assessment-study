import re
import os
import sys
import logging
import platform
import multiprocessing
import bs4
from glob import glob

def get_environment():
    logging.debug(f'Python version: {platform.python_version()}')
    logging.debug(f'BeautifulSoup4 verison: {bs4.__version__}')

def get_filepaths(path):
    filepaths = glob(path)
    logging.info(f'Total XML files is {len(filepaths)}')

    return filepaths

def check_path(path):
    if not os.path.exists(path):
        logging.warning(f'Path {path} isn\'t exist, creating now')
        os.mkdir(path)

def check_total_txt(path):
    filepaths = glob(path)
    logging.info(f'Total TXT files is {len(filepaths)}')

def save_to_txt(id, title, content):
    global dest_path
    try:
        # split article every 10K
        sub_directory = int(id) // 10000 * 10000
        sub_directory = f'{sub_directory:07d}'
        check_path(f'{dest_path}/{sub_directory}')

        with open(f'{dest_path}/{sub_directory}/{id:07d}_{title}.txt', 'w') as f:
            f.write(content)
    except Exception as ex:
        logging.error(f'Error while saving article with ID {id}')
        logging.error(ex)

def process_xml(filepath):
    logging.info(f'Processing XML file at {filepath}')

    try:
        with open(filepath, 'r') as f:
            soup = bs4.BeautifulSoup(f.read(), 'html.parser')
    except Exception as ex:
        logging.error(f'Error while opening XML file at {filepath}')
        logging.error(ex)
        return

    for doc in soup.find_all('doc'):
        try:
            id = int(doc['id'])
            title = doc['title']
            title = re.sub(r'[ ]', '_', title)
            title = re.sub(r'[^A-Za-z0-9_]', '', title)
            content = doc.text
        except Exception as ex:
            logging.error(f'Error while parsing article from XML file at {filepath}')
            logging.error(ex)
            return
            
        save_to_txt(id, title, content)

def batch_process(filepaths):
    cores = multiprocessing.cpu_count() - 1
    logging.debug(f'Uses {cores} core/thread')

    with multiprocessing.Pool(cores) as pool:
        pool.map(process_xml, filepaths)


if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s', filename='./dataset/debug_totxt.log',level=logging.DEBUG, )

    if len(sys.argv) < 4:
        logging.warning('Total argument less than 4, use default value')
        src_glob = './dataset/xml/**/*'
        dest_path = './dataset/txt'
        dest_glob = './dataset/txt/**/*'
    else:
        src_glob = sys.argv[1]
        dest_path = sys.argv[2]
        dest_glob = sys.argv[3]

    get_environment()
    check_path(dest_path)

    filepaths = get_filepaths(src_glob)
    batch_process(filepaths)

    check_total_txt(dest_glob)
