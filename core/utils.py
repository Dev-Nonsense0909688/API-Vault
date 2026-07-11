import subprocess
import platform

system = platform.system()


def get_cpu_uuid():
    if system == "Windows":
        uuid = (
            subprocess.check_output(["wmic", "csproduct", "get", "UUID"], text=True)
            .strip()
            .splitlines()[2]
        )
    elif system == "Linux":
        uuid = open(
            "/sys/class/dmi/id/product_uuid"
        ).read()  # Did not test it bro my machine is broken the psu will arrive on 12 July 2026.

    return uuid
