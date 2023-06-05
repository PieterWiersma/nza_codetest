
import os

def check_tables(db_connector: 'class', dataset_def_dir: str):
    """
    Checks whether the tables in the dataset_definitions folder exist in 
     the SQL database, if not will create them.
     
    """

    tables = db_connector.run_query('show tables;', expect_result=True)
    tables = [set(x.values()) for x in tables][0] # transform to set
    dataset_files = os.listdir(dataset_def_dir)
    tables_to_create = set([x[:-4] for x in dataset_files]).difference(tables)

    for table_to_create in tables_to_create:
        print(f"creating new table: {table_to_create}")
        db_connector.run_query(open(f"{dataset_def_dir}{table_to_create}.sql").read())


def extract_values(response: dict, fields: list):
    """
    extract fields from response

    """

    l = []
    for field in fields:
        l.append(clean_str(response[field]))
    return tuple(l)


def clean_str(s: str):
    s = s.replace('Å', 'A')
    return bytes(s, 'utf-8')
