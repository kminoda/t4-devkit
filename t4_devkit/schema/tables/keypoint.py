from __future__ import annotations

from typing import TYPE_CHECKING

import numpy as np
from attrs import define, field

from ..name import SchemaName
from .base import SchemaBase
from .registry import SCHEMAS

if TYPE_CHECKING:
    from t4_devkit.typing import KeypointType

__all__ = ["Keypoint"]


@define(slots=False)
@SCHEMAS.register(SchemaName.KEYPOINT)
class Keypoint(SchemaBase):
    """A dataclass to represent schema table of `keypoint.json`.

    Attributes:
        token (str): Unique record identifier.
        sample_data_token (str): Foreign key pointing to the sample data, which must be a keyframe image.
        instance_token (str): Foreign key pointing to the instance.
        category_tokens (list[str]): Foreign key pointing to keypoints categories.
        keypoints (KeypointType): Annotated keypoints. Given as a list of [x, y].
        num_keypoints (int): The number of keypoints to be annotated.
    """

    sample_data_token: str
    instance_token: str
    category_tokens: list[str]
    keypoints: KeypointType = field(converter=np.asarray)
    num_keypoints: int
