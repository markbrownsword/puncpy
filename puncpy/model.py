import collections
from typing import List

ApostropheItem = collections.namedtuple("ApostropheItem", ["word", "validRuleId"])
ApostropheItemCollection = List[ApostropheItem]
