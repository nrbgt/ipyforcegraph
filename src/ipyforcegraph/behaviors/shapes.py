"""Configurable shapes."""

# Copyright (c) 2023 ipyforcegraph contributors.
# Distributed under the terms of the Modified BSD License.

from typing import Any, Optional, Union

import ipywidgets as W
import traitlets as T

from ..trait_utils import JSON_TYPES, coerce
from ._base import Column, Nunjucks, ShapeBase

TFeature = Optional[Union[Column, Nunjucks, str]]
TNumFeature = Optional[Union[Column, Nunjucks, str, int, float]]
TBoolFeature = Optional[Union[Column, Nunjucks, str, bool]]


def _make_trait(
    help: str, numeric: Optional[bool] = None, boolish: Optional[bool] = None
) -> Any:
    if numeric:
        extra_types = [T.Int(), T.Float()]
    elif boolish:
        extra_types = [T.Bool()]
    else:
        extra_types = []

    return T.Union(
        [T.Instance(Column), T.Instance(Nunjucks), T.Unicode(), *extra_types],
        help=help,
        allow_none=True,
    ).tag(sync=True, **W.widget_serialization)


class HasFillAndStroke(ShapeBase):
    _model_name: str = T.Unicode("HasFillModel").tag(sync=True)
    fill: TFeature = _make_trait("the fill color of a shape")
    stroke: TFeature = _make_trait("the stroke color of a shape")
    stroke_width: TNumFeature = _make_trait("the stroke width of a shape", numeric=True)

    @T.validate("stroke_width")
    def _validate_has_fill_and_stroke_numerics(self, proposal: T.Bunch) -> Any:
        return coerce(proposal, JSON_TYPES.number)


@W.register
class Text(HasFillAndStroke):
    """Draw a text shape."""

    _model_name: str = T.Unicode("TextShapeModel").tag(sync=True)

    text: TFeature = _make_trait("the text of a shape")
    font: TFeature = _make_trait("the font face of a shape")
    size: TNumFeature = _make_trait("the font size of a shape in ``px``", numeric=True)
    background: TFeature = _make_trait("the background of a shape")
    padding: TNumFeature = _make_trait(
        "the padding around the shape in ``px``", numeric=True
    )
    scale_on_zoom: TBoolFeature = _make_trait(
        "whether font size/stroke respects the global scale", boolish=True
    )

    def __init__(self, text: TFeature, **kwargs: Any):
        if text is not None:
            kwargs["text"] = text
        super().__init__(**kwargs)

    @T.validate("size", "padding")
    def _validate_text_numerics(self, proposal: T.Bunch) -> Any:
        return coerce(proposal, JSON_TYPES.number)

    @T.validate("scale_on_zoom")
    def _validate_text_bools(self, proposal: T.Bunch) -> Any:
        return coerce(proposal, JSON_TYPES.boolean)


@W.register
class Rectangle(HasFillAndStroke):
    """Draw a rectangle shape."""

    _model_name: str = T.Unicode("RectangleShapeModel").tag(sync=True)
    width: TNumFeature = _make_trait("the width of a shape in ``px``", numeric=True)
    height: TNumFeature = _make_trait("the height of a shape in ``px``", numeric=True)

    @T.validate("width", "height")
    def _validate_rect_numerics(self, proposal: T.Bunch) -> Any:
        return coerce(proposal, JSON_TYPES.number)
