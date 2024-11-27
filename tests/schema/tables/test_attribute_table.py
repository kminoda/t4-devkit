from t4_devkit.schema import Attribute, serialize_schema, serialize_schemas


def test_attribute_json(attribute_json) -> None:
    """Test loading attribute from a json file."""
    schemas = Attribute.from_json(attribute_json)
    serialized = serialize_schemas(schemas)
    assert isinstance(serialized, list)


def test_attribute(attribute_dict) -> None:
    """Test loading attribute from a dictionary."""
    schema = Attribute.from_dict(attribute_dict)
    serialized = serialize_schema(schema)
    assert serialized == attribute_dict


def test_new_attribute(attribute_dict) -> None:
    """Test generating attribute with a new token."""
    without_token = {k: v for k, v in attribute_dict.items() if k != "token"}
    ret = Attribute.new(without_token)
    # check the new token is not the same with the token in input data
    assert ret.token != attribute_dict["token"]
