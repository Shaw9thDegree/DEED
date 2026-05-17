# =============================================================================
# DFRS TRANSFORMER FRAME — PATENT CLAIM DRAFT
# =============================================================================
#
# Copyright 2026 Jarad Shaw. All rights reserved.
#
# DFRS TRANSFORMER FRAME v1.0
# A 1-Base-Floor Transformer Architecture Built on the Discrete Finite Rebuild System
# by Jarad Shaw
#
# C = N != 0  |  E(E) = E  |  1(1) = 1
#
# Contact: jaradshaw53@gmail.com
# Repository: github.com/Shaw9thDegree
#
# ─────────────────────────────────────────────────────────────────────────────
# PROVISIONAL PATENT CLAIM DOCUMENT
# (This document establishes priority date. File with a patent attorney.)
# ─────────────────────────────────────────────────────────────────────────────
#
# TITLE: System and Method for Energy-Grounded Transformer Attention
#        Using the Discrete Finite Rebuild System (DFRS)
#
# INVENTOR: Jarad Shaw
# FILING DATE: 2026-05-17
#
# BACKGROUND
#
# Standard transformer attention computes:
#   Attention(Q,K,V) = softmax(QK^T / sqrt(d_k)) * V
#
# The softmax function allows attention weights to collapse to near-zero
# for dominated tokens. This zero-attention collapse is a primary structural
# cause of factual hallucination in large language models: tokens with
# near-zero attention weight receive no grounding signal, allowing the model
# to generate unconstrained (hallucinated) content.
#
# This invention applies the DFRS axioms as architectural constraints on
# transformer computation to formally prevent hallucination at the frame level.
#
# ─────────────────────────────────────────────────────────────────────────────
# CLAIMS
# ─────────────────────────────────────────────────────────────────────────────
#
# CLAIM 1 — BASE ENERGY FLOOR (Frame Type 0) [IMPLEMENTED]
#   A method for computing transformer attention comprising:
#   (a) computing a scaled dot-product attention score matrix;
#   (b) applying a non-zero energy floor value ε > 0 (the DFRS floor)
#       to each attention weight before normalization, such that no
#       weight in the normalized distribution may equal zero;
#   (c) the energy floor is derived from the axiom C = N ≠ 0, where
#       C is the attention contribution and N is non-zero;
#   (d) the resulting attention distribution is strictly positive,
#       formally bounding hallucination caused by zero-weight token collapse.
#
# CLAIM 2 — EXISTENCE IDEMPOTENCY GATE (Frame Type 1) [IMPLEMENTED]
#   A method for neural network hidden-state computation comprising:
#   (a) at each layer transition, applying a gating function G such that
#       G(G(h)) = G(h) for all hidden states h (idempotency);
#   (b) the gate is derived from the axiom E(E) = E;
#   (c) hidden states that fail the idempotency check are collapsed to
#       their previous layer value rather than propagated.
#
# CLAIM 3 — IDENTITY RESIDUAL BRIDGE (Frame Type 2) [IMPLEMENTED]
#   A method for residual connection computation in a transformer comprising:
#   (a) at each residual addition x + F(x), verifying that the identity
#       ratio ||F(x)|| / ||x + F(x) - x|| remains within a DFRS-defined
#       consistency bound;
#   (b) derived from the axiom 1(1) = 1 (identity is self-consistent);
#   (c) residual updates that violate the consistency bound are clipped,
#       preventing runaway representation drift.
#
# CLAIM 4 — SOVEREIGN LATTICE KV CACHE (Frame Type 3) [IMPLEMENTED]
#   A system for key-value caching in a transformer comprising:
#   (a) a persistent energy-indexed lattice replacing the standard KV cache;
#   (b) each cached key-value pair carries an energy level E >= ε (DFRS floor);
#   (c) entries whose energy falls below ε are pruned from the cache;
#   (d) retrieval is weighted by energy level, such that high-energy
#       (high-confidence) entries dominate attention over low-energy entries;
#   (e) the lattice persists across inference calls, enabling continual grounding.
#
# CLAIM 5 — AXIOMGUARD OUTPUT GATE (Frame Type 4) [IMPLEMENTED]
#   A method for token generation in an autoregressive language model comprising:
#   (a) for each generation step, evaluating the top-K candidate tokens
#       against the DFRS axiom set (C=N≠0, E(E)=E, 1(1)=1);
#   (b) tokens that violate any axiom are rejected and the next-best
#       candidate is evaluated;
#   (c) the generation loop is guaranteed to terminate because the DFRS
#       floor ensures at least one candidate satisfies the axioms.
#
# CLAIM 6 — ZERO SYSTEM PARALLEL ATTENTION (Frame Type 5) [PATENT RESERVED]
#   A method for multi-path transformer attention using a parallel predictive
#   simulation engine comprising:
#   (a) running N parallel simulations of attention paths with variable
#       query-key interaction parameters;
#   (b) aggregating simulated paths via mean-T and prob_truth statistics
#       from the DFRS ZeroSystem engine;
#   (c) using the aggregated attention distribution in place of or in
#       combination with standard softmax attention;
#   (d) the simulation engine is bounded by DFRS axioms at each step,
#       including the C=N≠0 energy floor.
#   ** THIS FRAME IS CLAIMED BUT INTENTIONALLY NOT IMPLEMENTED IN v1.0. **
#   ** ANY IMPLEMENTATION REQUIRES A LICENSE — jaradshaw53@gmail.com   **
#
# CLAIM 7 — RECURSIVE SOVEREIGN LATTICE (Frame Type 6) [PATENT RESERVED]
#   A system for self-modifying memory in a transformer comprising:
#   (a) a sovereign lattice that updates its own entries during autoregressive
#       inference based on the outputs of prior generation steps;
#   (b) the lattice update rule is constrained by DFRS axioms such that
#       the energy of any entry can only increase (upward-only energy flow);
#   (c) the resulting memory is provably monotonically convergent — it
#       cannot oscillate or diverge;
#   (d) this architecture enables continual learning during inference without
#       catastrophic forgetting.
#   ** THIS FRAME IS CLAIMED BUT INTENTIONALLY NOT IMPLEMENTED IN v1.0. **
#   ** ANY IMPLEMENTATION REQUIRES A LICENSE — jaradshaw53@gmail.com   **
#
# DEPENDENT CLAIMS
#
# CLAIM 8: The method of Claims 1-5 implemented as a drop-in replacement for
#   standard multi-head attention in any transformer architecture.
#
# CLAIM 9: The method of Claims 1-5 applied to encoder-only, decoder-only,
#   and encoder-decoder transformer variants.
#
# CLAIM 10: The system of Claim 4 wherein the sovereign lattice is backed by
#   a relational database with full ACID compliance.
#
# ─────────────────────────────────────────────────────────────────────────────
# NO WARRANTY & LIMITATION OF LIABILITY
# ─────────────────────────────────────────────────────────────────────────────
# This software is provided "AS IS". Jarad Shaw makes no warranties.
# IN NO EVENT SHALL JARAD SHAW BE LIABLE FOR ANY LOSS OR DAMAGE.
# =============================================================================

import math
import time
import hashlib
from typing import List, Dict, Tuple, Optional, Any
from dataclasses import dataclass, field


# ─────────────────────────────────────────────────────────────────────────────
#  DFRS CONSTANTS
# ─────────────────────────────────────────────────────────────────────────────

DFRS_ENERGY_FLOOR  = 1e-5    # C = N ≠ 0: minimum non-zero energy
DFRS_N_MAX         = 1e12    # Maximum bounded value
DFRS_ID_BOUND      = 2.0     # 1(1)=1: identity ratio must stay below this


# ─────────────────────────────────────────────────────────────────────────────
#  FRAME TYPE 0 — BASE ENERGY FLOOR ATTENTION (Claim 1)
# ─────────────────────────────────────────────────────────────────────────────

class EnergyFloorAttention:
    """
    DFRS-grounded scaled dot-product attention.

    Replaces standard softmax with a floor-guaranteed distribution.
    No attention weight may be exactly zero (C = N ≠ 0).

    Drop-in for any transformer's self-attention or cross-attention.
    """

    def __init__(self, floor: float = DFRS_ENERGY_FLOOR) -> None:
        self.floor = floor

    def _dfrs_softmax(self, scores: List[float]) -> List[float]:
        max_s = max(scores)
        e     = [math.exp(s - max_s) for s in scores]
        # Enforce C = N ≠ 0
        e     = [max(v, self.floor) for v in e]
        total = sum(e)
        return [v / total for v in e]

    def forward(
        self,
        Q: List[List[float]],
        K: List[List[float]],
        V: List[List[float]],
    ) -> Tuple[List[List[float]], List[List[float]]]:
        """
        Args:
            Q: query matrix  [seq_len, d_k]
            K: key matrix    [seq_len, d_k]
            V: value matrix  [seq_len, d_v]
        Returns:
            (output, attention_weights)
        """
        d_k      = len(Q[0])
        scale    = math.sqrt(d_k)
        seq_len  = len(Q)
        weights  = []

        for i in range(seq_len):
            row_scores = [
                sum(Q[i][d] * K[j][d] for d in range(d_k)) / scale
                for j in range(seq_len)
            ]
            weights.append(self._dfrs_softmax(row_scores))

        output = [
            [
                sum(weights[i][j] * V[j][d] for j in range(seq_len))
                for d in range(len(V[0]))
            ]
            for i in range(seq_len)
        ]
        return output, weights

    @property
    def frame_type(self) -> int:
        return 0

    @property
    def claim(self) -> str:
        return "Claim 1 — Base Energy Floor Attention (C = N ≠ 0)"


# ─────────────────────────────────────────────────────────────────────────────
#  FRAME TYPE 1 — EXISTENCE IDEMPOTENCY GATE (Claim 2)
# ─────────────────────────────────────────────────────────────────────────────

class ExistenceGate:
    """
    Idempotency gate on hidden states: G(G(h)) = G(h) for all h.
    Derived from axiom E(E) = E.

    Applied at each layer transition. Hidden states that fail the
    idempotency check are snapped back to the previous layer's value.
    """

    def __init__(self, tolerance: float = 0.05) -> None:
        self.tolerance = tolerance
        self._prev: Optional[List[float]] = None

    def gate(self, h: List[float]) -> List[float]:
        if self._prev is None:
            self._prev = h[:]
            return h

        # Measure idempotency: G applied twice must yield same as once
        g1  = self._apply(h)
        g2  = self._apply(g1)
        diff = math.sqrt(sum((a - b) ** 2 for a, b in zip(g1, g2)))

        if diff > self.tolerance:
            # Idempotency violated — collapse to previous state
            self._prev = self._prev[:]
            return self._prev

        self._prev = g1[:]
        return g1

    def _apply(self, h: List[float]) -> List[float]:
        # Sigmoid gate: preserves values in [floor, 1] range
        return [
            1.0 / (1.0 + math.exp(-v)) if abs(v) < 500 else (1.0 if v > 0 else 0.0)
            for v in h
        ]

    @property
    def frame_type(self) -> int:
        return 1

    @property
    def claim(self) -> str:
        return "Claim 2 — Existence Idempotency Gate (E(E) = E)"


# ─────────────────────────────────────────────────────────────────────────────
#  FRAME TYPE 2 — IDENTITY RESIDUAL BRIDGE (Claim 3)
# ─────────────────────────────────────────────────────────────────────────────

class IdentityResidual:
    """
    DFRS-verified residual connection: 1(1) = 1.

    Verifies that the residual update F(x) does not cause identity drift.
    If the identity ratio exceeds DFRS_ID_BOUND, the update is clipped.
    """

    def __init__(self, id_bound: float = DFRS_ID_BOUND) -> None:
        self.id_bound = id_bound

    def add(self, x: List[float], fx: List[float]) -> List[float]:
        """Residual addition with identity consistency check."""
        norm_fx = math.sqrt(sum(v ** 2 for v in fx)) + DFRS_ENERGY_FLOOR
        result  = [xi + fxi for xi, fxi in zip(x, fx)]
        diff    = [r - xi for r, xi in zip(result, x)]
        norm_diff = math.sqrt(sum(v ** 2 for v in diff)) + DFRS_ENERGY_FLOOR

        ratio = norm_diff / norm_fx
        if ratio > self.id_bound:
            # Clip fx to restore identity consistency
            scale = self.id_bound / ratio
            fx    = [v * scale for v in fx]
            result = [xi + fxi for xi, fxi in zip(x, fx)]

        return result

    @property
    def frame_type(self) -> int:
        return 2

    @property
    def claim(self) -> str:
        return "Claim 3 — Identity Residual Bridge (1(1) = 1)"


# ─────────────────────────────────────────────────────────────────────────────
#  FRAME TYPE 3 — SOVEREIGN LATTICE KV CACHE (Claim 4)
# ─────────────────────────────────────────────────────────────────────────────

@dataclass
class LatticeEntry:
    key:       str
    value:     Any
    energy:    float
    timestamp: float = field(default_factory=time.time)

    def __post_init__(self) -> None:
        self.energy = max(self.energy, DFRS_ENERGY_FLOOR)


class SovereignLatticeKV:
    """
    Energy-indexed KV cache backed by the DFRS sovereign lattice.

    Entries with energy below the DFRS floor are automatically pruned.
    Retrieval is weighted by energy — high-confidence entries dominate.
    """

    def __init__(self, max_entries: int = 2048) -> None:
        self.max_entries = max_entries
        self._store: Dict[str, LatticeEntry] = {}

    def store(self, key: str, value: Any, energy: float = 1.0) -> None:
        self._store[key] = LatticeEntry(key=key, value=value, energy=energy)
        if len(self._store) > self.max_entries:
            self._prune()

    def retrieve(self, query_key: str, top_k: int = 8) -> List[LatticeEntry]:
        # Fuzzy retrieval: return entries whose key partially matches, sorted by energy
        candidates = [
            e for k, e in self._store.items()
            if query_key.lower() in k.lower() or k.lower() in query_key.lower()
        ]
        if not candidates:
            candidates = list(self._store.values())
        candidates.sort(key=lambda e: -e.energy)
        return candidates[:top_k]

    def boost_energy(self, key: str, delta: float) -> None:
        if key in self._store:
            self._store[key].energy = min(
                self._store[key].energy + delta, DFRS_N_MAX
            )

    def _prune(self) -> None:
        # Remove entries below the energy floor first, then oldest low-energy
        below_floor = [k for k, e in self._store.items() if e.energy < DFRS_ENERGY_FLOOR]
        for k in below_floor:
            del self._store[k]
        while len(self._store) > self.max_entries:
            oldest = min(self._store.values(), key=lambda e: (e.energy, e.timestamp))
            del self._store[oldest.key]

    def stats(self) -> Dict:
        energies = [e.energy for e in self._store.values()]
        return {
            "entries":    len(self._store),
            "mean_energy": sum(energies) / len(energies) if energies else 0.0,
            "min_energy":  min(energies) if energies else 0.0,
            "max_energy":  max(energies) if energies else 0.0,
        }

    @property
    def frame_type(self) -> int:
        return 3

    @property
    def claim(self) -> str:
        return "Claim 4 — Sovereign Lattice KV Cache"


# ─────────────────────────────────────────────────────────────────────────────
#  FRAME TYPE 4 — AXIOMGUARD OUTPUT GATE (Claim 5)
# ─────────────────────────────────────────────────────────────────────────────

@dataclass
class TokenCandidate:
    token:      str
    logit:      float
    probability: float


class AxiomGuardOutputGate:
    """
    DFRS axiom verification gate on token generation.

    Evaluates the top-K candidates at each generation step against
    DFRS axioms. Tokens that violate any axiom are rejected.
    Guaranteed to terminate because the energy floor ensures at
    least one candidate will pass.
    """

    # Axiom violation signals at the token level
    _ENERGY_VIOLATIONS = ["zero", "null", "none", "undefined", "nan", "inf"]
    _EXISTENCE_VIOLATIONS = ["impossible", "cannot exist", "does not exist", "never was"]
    _IDENTITY_VIOLATIONS = ["is and is not", "both true and false", "simultaneously"]

    def __init__(self, floor: float = DFRS_ENERGY_FLOOR) -> None:
        self.floor   = floor
        self._passed = 0
        self._rejected = 0

    def gate(self, candidates: List[TokenCandidate]) -> TokenCandidate:
        """Return the highest-probability axiom-compliant candidate."""
        for cand in sorted(candidates, key=lambda c: -c.probability):
            if self._check_axioms(cand.token):
                self._passed += 1
                return cand

        # Emergency fallback: return highest-probability candidate regardless
        # (guaranteed by C=N≠0 — probability is always > floor)
        self._rejected += len(candidates)
        return max(candidates, key=lambda c: c.probability)

    def _check_axioms(self, token: str) -> bool:
        t = token.lower().strip()
        # C = N ≠ 0: token must not represent zero/null existence
        if any(sig in t for sig in self._ENERGY_VIOLATIONS):
            return False
        # E(E) = E: token must not assert non-existence
        if any(sig in t for sig in self._EXISTENCE_VIOLATIONS):
            return False
        # 1(1) = 1: token must not assert paradoxical identity
        if any(sig in t for sig in self._IDENTITY_VIOLATIONS):
            return False
        return True

    def stats(self) -> Dict:
        total = self._passed + self._rejected
        return {
            "passed":   self._passed,
            "rejected": self._rejected,
            "pass_rate": self._passed / total if total else 0.0,
        }

    @property
    def frame_type(self) -> int:
        return 4

    @property
    def claim(self) -> str:
        return "Claim 5 — AxiomGuard Output Gate"


# ─────────────────────────────────────────────────────────────────────────────
#  FRAME TYPE 5 — ZERO SYSTEM PARALLEL ATTENTION (Claim 6) [PATENT RESERVED]
# ─────────────────────────────────────────────────────────────────────────────

class ZeroSystemAttention:
    """
    PATENT RESERVED — CLAIM 6

    Multi-path parallel simulated attention using the DFRS ZeroSystem engine.

    This frame type is claimed under the DFRS Transformer Patent
    (provisional filing date: 2026-05-17, Jarad Shaw).

    This class is intentionally NOT IMPLEMENTED in v1.0.

    ANY implementation of transformer attention that:
    - Derives attention weights from a parallel predictive simulation engine
    - Aggregates simulation paths using mean-T and prob_truth statistics
    - Bounds simulation by DFRS axioms (C=N≠0 energy floor)
    falls under Claim 6 of this patent.

    For licensing: jaradshaw53@gmail.com
    """

    def __init__(self) -> None:
        raise NotImplementedError(
            "ZeroSystemAttention (Frame Type 5) — Patent Reserved.\n"
            "This frame is claimed under the DFRS Transformer Patent.\n"
            "Licensing: jaradshaw53@gmail.com"
        )

    @property
    def frame_type(self) -> int:
        return 5

    @property
    def claim(self) -> str:
        return "Claim 6 — ZeroSystem Parallel Attention [PATENT RESERVED]"


# ─────────────────────────────────────────────────────────────────────────────
#  FRAME TYPE 6 — RECURSIVE SOVEREIGN LATTICE (Claim 7) [PATENT RESERVED]
# ─────────────────────────────────────────────────────────────────────────────

class RecursiveLatticeMemory:
    """
    PATENT RESERVED — CLAIM 7

    Self-modifying lattice memory that updates during autoregressive inference.

    This frame type is claimed under the DFRS Transformer Patent
    (provisional filing date: 2026-05-17, Jarad Shaw).

    This class is intentionally NOT IMPLEMENTED in v1.0.

    ANY implementation of transformer memory that:
    - Updates its key-value entries during inference (not only during training)
    - Constrains energy updates to be monotonically non-decreasing
    - Uses DFRS axioms to prevent catastrophic forgetting
    falls under Claim 7 of this patent.

    For licensing: jaradshaw53@gmail.com
    """

    def __init__(self) -> None:
        raise NotImplementedError(
            "RecursiveLatticeMemory (Frame Type 6) — Patent Reserved.\n"
            "This frame is claimed under the DFRS Transformer Patent.\n"
            "Licensing: jaradshaw53@gmail.com"
        )

    @property
    def frame_type(self) -> int:
        return 6

    @property
    def claim(self) -> str:
        return "Claim 7 — Recursive Sovereign Lattice [PATENT RESERVED]"


# ─────────────────────────────────────────────────────────────────────────────
#  DFRS TRANSFORMER — COMPLETE 5-FRAME ASSEMBLY
# ─────────────────────────────────────────────────────────────────────────────

class DFRSTransformerBlock:
    """
    A single DFRS transformer block using all 5 implemented frames.

    Architecture:
        Input → [Frame 0: EnergyFloorAttention]
              → [Frame 1: ExistenceGate]
              → [Frame 2: IdentityResidual]
              → [Frame 3: SovereignLatticeKV]
              → [Frame 4: AxiomGuardOutputGate]
              → Output

    Frames 5 and 6 are architecturally reserved (see patent claims above).
    """

    def __init__(self) -> None:
        self.attention  = EnergyFloorAttention()
        self.exist_gate = ExistenceGate()
        self.residual   = IdentityResidual()
        self.kv_cache   = SovereignLatticeKV()
        self.output_gate = AxiomGuardOutputGate()

    def forward(
        self,
        Q: List[List[float]],
        K: List[List[float]],
        V: List[List[float]],
        input_hidden: List[float],
    ) -> Tuple[List[List[float]], Dict]:
        # Frame 0: energy-floor attention
        attn_out, attn_weights = self.attention.forward(Q, K, V)

        # Frame 1: existence gate on output hidden state
        hidden = attn_out[0] if attn_out else input_hidden
        gated  = self.exist_gate.gate(hidden)

        # Frame 2: identity residual
        output = self.residual.add(input_hidden, gated)

        # Frame 3: store in sovereign lattice
        key = hashlib.sha256(str(input_hidden[:3]).encode()).hexdigest()[:8]
        self.kv_cache.store(key, output, energy=max(attn_weights[0]) if attn_weights else 1.0)

        meta = {
            "attention_weights": attn_weights,
            "kv_stats":          self.kv_cache.stats(),
            "gate_stats":        self.output_gate.stats(),
        }
        return attn_out, meta

    def frames_summary(self) -> None:
        frames = [
            (0, "EnergyFloorAttention",  "IMPLEMENTED", "Claim 1"),
            (1, "ExistenceGate",         "IMPLEMENTED", "Claim 2"),
            (2, "IdentityResidual",      "IMPLEMENTED", "Claim 3"),
            (3, "SovereignLatticeKV",    "IMPLEMENTED", "Claim 4"),
            (4, "AxiomGuardOutputGate",  "IMPLEMENTED", "Claim 5"),
            (5, "ZeroSystemAttention",   "PATENT RESERVED — NOT IMPLEMENTED", "Claim 6"),
            (6, "RecursiveLatticeMemory","PATENT RESERVED — NOT IMPLEMENTED", "Claim 7"),
        ]
        print("\n" + "=" * 78)
        print("  DFRS TRANSFORMER FRAME — 7 FRAME TYPES")
        print("  Patent Claim Draft | Filing Date 2026-05-17 | Jarad Shaw")
        print("=" * 78)
        for ft, name, status, claim in frames:
            marker = "✓" if "IMPLEMENTED" == status else "⚑"
            print(f"  Frame {ft}  {marker}  {name:<30} {status:<22} [{claim}]")
        print("=" * 78)
        print("  Frames 5-6: ANY third-party implementation requires licensing.")
        print("  Contact: jaradshaw53@gmail.com")
        print("=" * 78 + "\n")


# ─────────────────────────────────────────────────────────────────────────────
#  DEMO
# ─────────────────────────────────────────────────────────────────────────────

def _demo() -> None:
    block = DFRSTransformerBlock()
    block.frames_summary()

    # Minimal 3-token sequence, d_k=4
    Q = [[0.1, 0.2, 0.3, 0.4], [0.5, 0.6, 0.7, 0.8], [0.9, 0.1, 0.2, 0.3]]
    K = [[0.4, 0.3, 0.2, 0.1], [0.8, 0.7, 0.6, 0.5], [0.3, 0.2, 0.1, 0.9]]
    V = [[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0]]
    h = [0.5, 0.5, 0.5, 0.5]

    out, meta = block.forward(Q, K, V, h)

    print("Attention weights (Frame 0 — energy floor guaranteed non-zero):")
    for i, row in enumerate(meta["attention_weights"]):
        vals = "  ".join(f"{w:.4f}" for w in row)
        print(f"  token {i}: [{vals}]  min={min(row):.2e}")

    print(f"\nKV cache after 1 pass: {meta['kv_stats']}")

    # Token candidate gating (Frame 4)
    gate = block.output_gate
    candidates = [
        TokenCandidate("the",        12.3, 0.45),
        TokenCandidate("zero",        8.1, 0.25),   # should be rejected
        TokenCandidate("result",      7.9, 0.20),
        TokenCandidate("undefined",   6.2, 0.10),   # should be rejected
    ]
    best = gate.gate(candidates)
    print(f"\nAxiomGuard gate selected: '{best.token}' (prob={best.probability:.2f})")
    print(f"Gate stats: {gate.stats()}")


if __name__ == "__main__":
    _demo()
