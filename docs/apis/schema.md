# `schema`

<!-- prettier-ignore-start -->
## Schema names

---

::: t4_devkit.schema.name
    options:
        show_docstring_attributes: true
        show_bases: false

## Schema tables

---

::: t4_devkit.schema.tables
    options:
        filters: ["!SchemaBase", "!FileFormat", "!SensorModality", "!VisibilityLevel", "!RLEMask"]
        show_root_toc_entry: false
        merge_init_into_class: false
        show_signature_annotations: false
        show_docstring_attributes: true

### Other items constructing schema table

---

::: t4_devkit.schema.tables
    options:
        members: ["FileFormat", "SensorModality", "VisibilityLevel", "RLEMask"]
        show_root_toc_entry: false
        merge_init_into_class: false
        show_signature_annotations: false
        show_docstring_attributes: true

## Schema registry

---

::: t4_devkit.schema.builder

::: t4_devkit.schema.tables.registry
    options:
        members: ["SCHEMAS", "SchemaRegistry"]
        show_root_toc_entry: false

## Schema serialization

---

::: t4_devkit.schema.serialize

<!-- prettier-ignore-end -->
