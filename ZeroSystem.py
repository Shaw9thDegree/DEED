# =============================================================================
# ZERO SYSTEM v1.0 — DFRS Parallel Predictive Simulation Engine
# =============================================================================
# Copyright 2026 Jarad Shaw. All rights reserved.
# C = N != 0  |  E(E) = E  |  1(1) = 1
# Contact: jaradshaw53@gmail.com  |  github.com/Shaw9thDegree
#
# Commercial License: $49/month or $389/year per installation
# Non-commercial use free under AGPL v3.
# THIS SOFTWARE IS PROVIDED "AS IS" — NO WARRANTIES.
# =============================================================================

import asyncio
import hashlib
import json
import threading
import time
import zlib
import base64
import marshal
from collections import OrderedDict
from concurrent.futures import ThreadPoolExecutor
from typing import Any, Dict, List, Optional, Tuple


# ─────────────────────────────────────────────────────────────────────────────
#  PROTECTED CORE
# ─────────────────────────────────────────────────────────────────────────────

_CORE = (
    "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"
    "vtN/qBGM+g=="
)
_SEAL = "c93beaf2836bae5eb10497634e1337efd962cb83ba932309e5ae098a5f8d3834"
_loaded = False


class LicenseError(RuntimeError): pass
class TamperError(RuntimeError): pass


class PyriteLock:
    """Key: 48300921 — Commercial | 11111111 — Education"""
    _KEYS = {"48300921": "commercial", "11111111": "education"}
    active_key:   Optional[str] = None
    is_licensed:  bool          = False
    license_type: str           = "unlicensed"

    @classmethod
    def set_key(cls, key: str) -> bool:
        c = str(key).strip()
        if c in cls._KEYS:
            cls.active_key = c; cls.license_type = cls._KEYS[c]; cls.is_licensed = True
            print(f"[PyriteLock/ZeroSystem] ✓ {cls.license_type} license activated.")
            return True
        return False

    @classmethod
    def start_timer(cls) -> None:
        def _judge():
            if not cls.is_licensed:
                print("[PyriteLock/ZeroSystem] ⚠  No license — core is LOCKED.")
        t = threading.Timer(540, _judge); t.daemon = True; t.start()


def _load() -> None:
    global _loaded
    if _loaded: return
    if not PyriteLock.is_licensed:
        raise LicenseError("ZeroSystem requires a license. Commercial: $49/mo. github.com/Shaw9thDegree")
    if hashlib.sha256(_CORE.encode()).hexdigest() != _SEAL:
        raise TamperError("ZeroSystem core tampered. Reinstall from github.com/Shaw9thDegree")
    exec(marshal.loads(zlib.decompress(base64.b64decode(_CORE.encode()))), globals())
    _loaded = True


# ─────────────────────────────────────────────────────────────────────────────
#  ZERO SYSTEM — MAIN CLASS
# ─────────────────────────────────────────────────────────────────────────────

class ZeroSystem:
    """
    Parallel Predictive Simulation Engine.

    Runs up to max_sims combinations of variable parameters, aggregates
    results via mean-T and prob_truth, and caches for reuse.

    Usage:
        zs = ZeroSystem(license_key="48300921")
        result = await zs.simulate(
            claim="The market will rise if rates fall.",
            variable_ranges={"rate_delta": [-0.25, -0.5, -0.75]},
            horizon=100,
        )
    """

    def __init__(self, max_sims: int = 10_000, max_workers: int = 4,
                 cache_size: int = 1000, license_key: Optional[str] = None) -> None:
        if license_key:
            PyriteLock.set_key(license_key)
        PyriteLock.start_timer()
        _load()
        self.max_sims    = max_sims
        self.cache       = OrderedDict()
        self.cache_size  = cache_size
        self.executor    = ThreadPoolExecutor(max_workers=max_workers)
        self.stats       = {"simulations_run": 0, "cache_hits": 0, "avg_ms": 0.0}

    async def simulate(self, claim: str, variable_ranges: Dict[str, List[Any]],
                       shadow: Optional[Dict[str, float]] = None,
                       horizon: int = 100) -> Dict:
        """Run parallel predictive simulation. Returns mean_T, T_std, prob_truth."""
        _load()
        combos = self._combos(variable_ranges)
        if not combos:
            return {"error": "No combinations generated"}
        shadow_data = shadow or {}
        tasks = []
        for combo in combos:
            key = self._cache_key(claim, combo, horizon, shadow_data)
            if key in self.cache:
                self.stats["cache_hits"] += 1
                tasks.append(self.cache[key])
            else:
                tasks.append(await self._run(claim, combo, shadow_data, horizon, key))
        return _aggregate(tasks)  # noqa: F821

    async def _run(self, claim, combo, shadow_data, horizon, cache_key) -> Dict:
        loop = asyncio.get_event_loop()
        t0   = time.perf_counter()
        result = await loop.run_in_executor(
            self.executor, _simulate_one, claim, combo, shadow_data, horizon  # noqa: F821
        )
        ms = (time.perf_counter() - t0) * 1000
        n  = self.stats["simulations_run"] + 1
        self.stats["avg_ms"] = (self.stats["avg_ms"] * (n - 1) + ms) / n
        self.stats["simulations_run"] = n
        self.cache[cache_key] = result
        if len(self.cache) > self.cache_size:
            self.cache.popitem(last=False)
        return result

    def _combos(self, ranges: Dict) -> List[Dict]:
        from itertools import product
        keys, vals = list(ranges.keys()), list(ranges.values())
        return [dict(zip(keys, c)) for c in list(product(*vals))[: self.max_sims]]

    @staticmethod
    def _cache_key(claim, combo, horizon, shadow) -> str:
        data = json.dumps([claim, combo, horizon, list(shadow.items())[:5]], sort_keys=True)
        return hashlib.sha256(data.encode()).hexdigest()[:32]


# ─────────────────────────────────────────────────────────────────────────────
#  DEMO
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    async def _demo():
        zs = ZeroSystem(license_key="48300921", max_sims=100)
        result = await zs.simulate(
            claim="Interest rates will fall.",
            variable_ranges={"rate_delta": [-0.25, -0.5, -0.75, -1.0]},
            shadow={"interest_rate": 5.25, "inflation": 3.1},
            horizon=20,
        )
        print("ZeroSystem simulation result:")
        for k, v in result.items():
            print(f"  {k}: {v}")
        print(f"  engine stats: {zs.stats}")
    asyncio.run(_demo())
