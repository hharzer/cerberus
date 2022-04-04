""" Platform-dependent objects """

import sys


if sys.version_info < (3, 7):
    from typing import _ForwardRef as ForwardRef, GenericMeta as GenericAlias
    from typing import _Union, Union

    def get_type_args(tp):
        return tp.__args__ if isinstance(tp, (GenericAlias, _Union)) else ()

    def get_type_origin(tp):
        if isinstance(tp, GenericAlias):
            return tp.__extra__
        if isinstance(tp, _Union):
            return Union
        return None

    def has_concrete_args(tp):
        return not tp.__parameters__


elif sys.version_info < (3, 8):
    from typing import ForwardRef, _GenericAlias as GenericAlias

    def get_type_args(tp):
        return tp.__args__ if isinstance(tp, GenericAlias) else ()

    def get_type_origin(tp):
        return tp.__origin__ if isinstance(tp, GenericAlias) else None

    def has_concrete_args(tp):
        return not tp.__parameters__


elif sys.version_info < (3, 9):
    from typing import ForwardRef, _GenericAlias as GenericAlias  # type: ignore
    from typing import get_args as get_type_args
    from typing import get_origin as get_type_origin

    def has_concrete_args(tp):
        return bool(get_type_args(tp))


else:
    from typing import ForwardRef, _BaseGenericAlias as GenericAlias
    from typing import get_args as get_type_args
    from typing import get_origin as get_type_origin

    def has_concrete_args(tp):
        return bool(get_type_args(tp))


__all__ = (
    "ForwardRef",
    "GenericAlias",
    get_type_args.__name__,
    get_type_origin.__name__,
    has_concrete_args.__name__,
)
