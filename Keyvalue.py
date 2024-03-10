from enum import Enum

class JsonKeys(Enum):
    ISSUE_ID = 'issue_id'
    URL = 'url'
    BRANCH = 'branch'
    COMMIT_HASH = 'commit_hash'
    PROJECT_NAME = 'project_name'
    BUILD_COMMAND = 'build_command'
    ROOT_DIR = 'root_dir'
    PACKAGE = 'package'
    TARGETS = 'targets'
    METHOD_NAME = 'method'
    FILE_NAME = 'file'
    CF_Version = 'cf_version'
    JAVA_VERSION = 'java_version'
    NOTE = 'note'
    INNER_CLASS = 'inner_class'
    NON_PRIMARY_CLASS = 'non_primary_class'
