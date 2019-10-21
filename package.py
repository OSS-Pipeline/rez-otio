name = "otio"

version = "0.11.0"

authors = [
    "Pixar"
]

description = \
    """
    OpenTimelineIO is an interchange format and API for editorial cut information. OTIO is not a container format for
    media, rather it contains information about the order and length of cuts and references to external media.
    """

requires = [
    "cmake-3+",
    "pip-19+",
    "pyaaf2-1.2+",
    "pyside2-2+",
    "python-2.7+<3"
]

variants = [
    ["platform-linux"]
]

tools = [
    "otiocat",
    "otioconvert",
    "otiostat",
    "otioview"
]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

uuid = "otio-{version}".format(version=str(version))

def commands():
    env.PATH.prepend("{root}/bin")
    env.PYTHONPATH.prepend("{root}")

    # Helper environment variables.
    env.OTIO_BINARY_PATH.set("{root}/bin")
