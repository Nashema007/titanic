import os
from kaggle.api.kaggle_api_extended import KaggleApi
import logging

def main(poject_dir):
    logger = logging.getLogger(__name__)
    logger.info('getting raw data')
    #imports
    os.system("kaggle competitions download -c titanic -p ../../data/raw") 

    from zipfile import ZipFile
    raw_data_path = os.path.join(project_dir, 'data', 'raw')
    titanic_zip = os.path.join(raw_data_path, 'titanic.zip')
    with ZipFile(titanic_zip, 'r') as zf:
        zf.extractall(raw_data_path)
    logger.info('downloaded raw data and extracted')
    
if __name__ == '__main__':
    #getting root directory
    project_dir = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)
    
    #setup logger
    log_format = '%(asctime)s -%(name)s - %(levelname)s %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_format)
    
    #call the main
    main(project_dir)
