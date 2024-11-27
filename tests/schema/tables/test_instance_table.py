from t4_devkit.schema import Instance, serialize_schema, serialize_schemas


def test_instance_json(instance_json) -> None:
    """Test loading instance from a json file."""
    schemas = Instance.from_json(instance_json)
    serialized = serialize_schemas(schemas)
    assert isinstance(serialized, list)


def test_instance(instance_dict) -> None:
    """Test loading instance from a dictionary."""
    schema = Instance.from_dict(instance_dict)
    serialized = serialize_schema(schema)
    assert serialized == instance_dict


def test_new_instance(instance_dict) -> None:
    """Test generating instance with a new token."""
    without_token = {k: v for k, v in instance_dict.items() if k != "token"}
    ret = Instance.new(without_token)
    # check the new token is not the same with the token in input data
    assert ret.token != instance_dict["token"]
