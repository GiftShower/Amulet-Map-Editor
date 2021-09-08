import wx
from ...base.base_identifier_select import BaseIDChangeEvent

_BlockIDChangeEventType = wx.NewEventType()
EVT_BLOCK_ID_CHANGE = wx.PyEventBinder(_BlockIDChangeEventType)


class BlockIDChangeEvent(BaseIDChangeEvent):
    """
    Run when the block resource identifier changes.
    """

    def __init__(
        self,
        namespace: str,
        base_name: str,
        old_namespace: str,
        old_base_name: str,
    ):
        super().__init__(namespace, base_name, old_namespace, old_base_name)
        self.SetEventType(_BlockIDChangeEventType)