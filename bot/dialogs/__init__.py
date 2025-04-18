from .start.dialogs import start_dialog
from .convert.dialogs import convert_dialog


dialogs_list = [
    start_dialog,
    convert_dialog,
]

__all__ = ["dialogs_list"]