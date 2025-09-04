import tempfile
import pyarrow as pa
from miniql.catalog import Catalog

def test_register_and_get_schema(tmp_path):
    p = tmp_path / "sample.csv"
    p.write_text("id,price,city\n1,10.0,LA\n2,20.5,NY")
    cat = Catalog()
    schema = cat.add_table(p, "sample")
    
    assert isinstance(schema, pa.Schema)
    
    assert schema.names == ["id", "price", "city"]
    
    assert "sample" in cat.list_tables()