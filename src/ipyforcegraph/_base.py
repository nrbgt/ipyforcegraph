"""Base widget identification for ``ipyforcegraph``."""

# Copyright (c) 2023 ipyforcegraph contributors.
# Distributed under the terms of the Modified BSD License.

import ipywidgets as W
import traitlets as T

from . import _types as _t
from .constants import EXTENSION_NAME, EXTENSION_SPEC_VERSION


class ForceBase(W.Widget):
    """The base class for all ``IPyForceGraph`` widgets."""

    _model_name: _t.Tstr = T.Unicode("ForceBaseModel").tag(sync=True)
    _model_module: _t.Tstr = T.Unicode(EXTENSION_NAME).tag(sync=True)
    _model_module_version: _t.Tstr = T.Unicode(EXTENSION_SPEC_VERSION).tag(sync=True)
    _view_module: _t.Tstr = T.Unicode(EXTENSION_NAME).tag(sync=True)
    _view_module_version: _t.Tstr = T.Unicode(EXTENSION_SPEC_VERSION).tag(sync=True)
