import os
import pytest
import re
import subprocess


def pytest_collection_modifyitems(config, items):
    if os.environ.get("CIF"):
        aspectator_path = os.environ.get("CIF")[:-3] + "aspectator"
    else:
        aspectator_path = os.path.join(
            os.path.dirname(__file__), "..", "inst", "bin", "aspectator"
        )

    arch = get_arch(aspectator_path)

    skip_arm = pytest.mark.skipif(
        "arm" not in arch, reason="arm cif is not available"
    )

    skip_not_arm = pytest.mark.skipif(
        "arm" in arch, reason="arm cif is available"
    )

    skip_aarch64 = pytest.mark.skipif(
        "aarch64" not in arch, reason="aarch64 cif is not available"
    )

    skip_x86_64 = pytest.mark.skipif(
        "x86_64" not in arch, reason="x86_64 cif is not available"
    )

    for item in items:
        if "arm" in item.keywords:
            item.add_marker(skip_arm)

        if "not_arm" in item.keywords:
            item.add_marker(skip_not_arm)

        if "aarch64" in item.keywords:
            item.add_marker(skip_aarch64)

        if "x86_64" in item.keywords:
            item.add_marker(skip_x86_64)


def get_arch(gcc_path):
    r = subprocess.run(
        gcc_path + " -v",
        shell=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )

    m = re.search(r"Target: (.*?)-", r.stdout)

    if not m:
        raise RuntimeError("Can't determine CIF arch: " + gcc_path)

    return m.group(1)
