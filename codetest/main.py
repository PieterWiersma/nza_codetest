
import argparse
import configparser

import yaml

from db_connector import SqlConnector
from soap import read_soap
from helpers import check_tables, extract_values


def cli():
    """
    Reads command line arguments.

    """

    parser = argparse.ArgumentParser()
    parser.add_argument("--config", help="location of config file",
                         type=str, default="CONFIG.ini")
    parser.add_argument("--dataset-definitions-dir", help="directory where the dataset definitions reside.",
                         type=str, default="dataset_definitions/")
    parser.add_argument("--country-info-instr-file", help="location of country info instruction file",
                         type=str, default="instructions/CountryInfoService.yaml")
    parser.add_argument("--show_data", help="If given shows data in countries table, skips rest.",
                         action="store_true")
    
    return parser.parse_args()


def read_config(file_location: str):
    """
    read and return config file.

    """

    config = configparser.ConfigParser()
    config.read(file_location)
    return config 


def read_instruction(file_location: str):
    """
    Reads and return yaml file as dict.

    """

    return yaml.load(open(file_location), Loader=yaml.FullLoader)


def main():
    """
    Main orchestration function

    """

    # get commandline arguments
    arguments = cli()

    # get config
    config = read_config(arguments.config)
    
    # read instruction
    country_info_instruction = read_instruction(arguments.country_info_instr_file)

    # get_db_connector
    db_connector = SqlConnector(config['sql']['user'], 
                                config['sql']['password'], 
                                config['sql']['database'], 
                                config['sql']['host'])
    if not arguments.show_data:
        # check if table exists, if not create
        check_tables(db_connector, arguments.dataset_definitions_dir)

        # get cities
        for response in read_soap(country_info_instruction):
            values = extract_values(response, country_info_instruction['fields'])
            db_connector.insert_data(country_info_instruction['dataset_table'], values, country_info_instruction['columns'])

    print(db_connector.run_query("select * from countries", expect_result=True))


if __name__ == "__main__":
    main()
