import pyarrow.csv as pv
import pyarrow as pa
from pathlib import Path

class Catalog:
    """In memory catalog.
    """
    def __init__(self):
        self._tables: dict[str, dict] = {}
        
    def add_table(self, path: str, table_name: str):
        p = Path(p)
        if not p.exists():
            raise FileNotFoundError(f"CSV file not exists: {path}")
        
        table: pa.Table = pv.read_csv(path)
        schema: pa.Schema = table.schema
        
        self._tables[table_name] = {"table": table, "schema": schema}
        return schema
        
    def get_schema(self, table_name: str):
        if table_name not in self._tables:
            raise KeyError(f"No table in the catalog {table_name}")
        return self._tables[table_name]["schema"]
    
    def list_tables(self):
        return self._tables.keys()
        
catalog = Catalog()
