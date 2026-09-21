#!/usr/bin/env python3
"""DSOM Core Compaction Engine Utility (Step 2).

Executes token efficiency compaction, transforming raw instructions, log telemetry,
or workspace mutations into a compressed, high-density JSON state payload conforming to
the Deep State of Mind (DSOM) Protocol v0.2 specification.
"""

import argparse
import datetime
import json
from typing import Any


def create_compacted_payload(
    active_intent: str,
    constraints: list[str] | None = None,
    system_mutations: str = "No structural mutations recorded",
    telemetry_vectors: str = "Telemetry nominal",
    memory_keys: list[str] | None = None,
) -> dict[str, Any]:
    """Build a structured DSOM compaction payload.

    Args:
        active_intent: Primary high-level operational goal.
        constraints: List of technical dependencies or environment constraints.
        system_mutations: Summary of altered files or repository state steps.
        telemetry_vectors: Compressed log exceptions or operational alerts.
        memory_keys: Atomic reference points for episodic ledger persistence.

    Returns:
        A dictionary conforming to the DSOM v0.2 compaction JSON schema.

    """
    if constraints is None:
        constraints = ["Python 3.12 / Node.js v22", "Google Jules Container Compatibility"]

    if memory_keys is None:
        memory_keys = ["DSOM_STATE_SYNC_COMPLETE"]

    now_iso = datetime.datetime.now(datetime.timezone.utc).isoformat()

    return {
        "dsom_compaction_meta": {
            "protocol_version": "0.2",
            "timestamp": now_iso,
        },
        "active_intent": active_intent.strip(),
        "operational_constraints": constraints,
        "context_deltas": {
            "system_mutations": system_mutations.strip(),
            "telemetry_vectors": telemetry_vectors.strip(),
        },
        "episodic_memory_keys": memory_keys,
    }


def main() -> None:
    """Parse CLI arguments and print compacted DSOM JSON state payload."""
    parser = argparse.ArgumentParser(
        description="DSOM Core Compaction Engine - Token Efficiency Layer"
    )
    parser.add_argument(
        "--intent",
        type=str,
        default="Execute workspace maintenance and quality verification",
        help="Primary active operational intent",
    )
    parser.add_argument(
        "--constraints",
        type=str,
        default="",
        help="Comma-separated operational constraints",
    )
    parser.add_argument(
        "--mutations",
        type=str,
        default="State synchronization in progress",
        help="Summary of active system or file mutations",
    )
    parser.add_argument(
        "--telemetry",
        type=str,
        default="All quality guardrails nominal",
        help="Compressed telemetry or alert vectors",
    )
    parser.add_argument(
        "--keys",
        type=str,
        default="EPISODIC_SYNC",
        help="Comma-separated episodic memory keys",
    )

    args = parser.parse_args()

    constraints_list = (
        [c.strip() for c in args.constraints.split(",") if c.strip()]
        if args.constraints
        else ["Node22/Astro7.1", "DSOM OKF v0.2"]
    )

    keys_list = (
        [k.strip() for k in args.keys.split(",") if k.strip()]
        if args.keys
        else ["DSOM_PALACE_SYNC"]
    )

    payload = create_compacted_payload(
        active_intent=args.intent,
        constraints=constraints_list,
        system_mutations=args.mutations,
        telemetry_vectors=args.telemetry,
        memory_keys=keys_list,
    )

    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
