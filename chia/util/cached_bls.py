from __future__ import annotations

import chia_rs

BLSCache = chia_rs.BLSCache

# Increasing this number will increase RAM usage, but decrease BLS validation time for blocks and unfinished blocks.
LOCAL_CACHE = BLSCache(50000)
