from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.pycharm")
use_plugin("python.flake8")
use_plugin("python.distutils")


name = "PyLabDeviceIO"
default_task = "publish"


@init
def set_properties(project):
    pass


@init
def initialize(project):
    project.build_depends_on("mock")
