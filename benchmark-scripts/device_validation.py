"""
Utilities for validating benchmark target device arguments.
"""

import argparse
import re


_GPU_INDEX_PATTERN = re.compile(r"^GPU\.(\d+)$", re.IGNORECASE)


def validate_target_device(value: str) -> str:
    """Validate and normalize target device values.

    Accepted values:
    - CPU
    - GPU
    - GPU.<index> where index is a non-negative integer
    - NPU
    """
    normalized = value.strip()
    upper_value = normalized.upper()

    if upper_value in {"CPU", "GPU", "NPU"}:
        return upper_value

    gpu_match = _GPU_INDEX_PATTERN.fullmatch(normalized)
    if gpu_match:
        return f"GPU.{gpu_match.group(1)}"

    raise argparse.ArgumentTypeError(
        "invalid target device '%s'. Expected one of: CPU, GPU, NPU, GPU.<index>"
        % value
    )
