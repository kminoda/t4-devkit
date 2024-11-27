from t4_devkit.schema import SampleAnnotation, serialize_schema, serialize_schemas


def test_sample_annotation_json(sample_annotation_json) -> None:
    """Test loading sample annotation from a json file."""
    schemas = SampleAnnotation.from_json(sample_annotation_json)
    serialized = serialize_schemas(schemas)
    assert isinstance(serialized, list)


def test_sample_annotation(sample_annotation_dict) -> None:
    """Test loading sample annotation from a dictionary."""
    schema = SampleAnnotation.from_dict(sample_annotation_dict)
    serialized = serialize_schema(schema)
    assert serialized == sample_annotation_dict


def test_new_sample_annotation(sample_annotation_dict) -> None:
    """Test generating sample annotation with a new token."""
    without_token = {k: v for k, v in sample_annotation_dict.items() if k != "token"}
    ret = SampleAnnotation.new(without_token)
    # check the new token is not the same with the token in input data
    assert ret.token != sample_annotation_dict["token"]
