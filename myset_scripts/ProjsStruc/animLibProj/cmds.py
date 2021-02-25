#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = cmds.py
__author__ = zhangben 
__mtime__ = 2020/9/24 : 10:54
__description__: 

    code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""
import os,json
__all__ = ['write','write2json','relPath','normPath','realPath']

def write(path, data):
    """
    Write the given data to the given file on disc.

    :type path: str
    :type data: str
    :rtype: None
    """
    path = normPath(path)
    data = relPath(data, path)

    tmp = path + ".tmp"
    bak = path + ".bak"

    # Create the directory if it doesn't exists
    dirname = os.path.dirname(path)
    if not os.path.exists(dirname):
        os.makedirs(dirname)

    # Use the tmp file to check for concurrent writes
    if os.path.exists(tmp):
        msg = "The path is locked for writing and cannot be accessed {}"
        msg = msg.format(tmp)
        raise IOError(msg)

    # Safely write the data to a tmp file and then rename to the given path
    try:
        # Create and write the new data
        #  to the path.tmp file
        with open(tmp, "w") as f:
            f.write(data)
            f.flush()

        # Remove any existing path.bak files
        if os.path.exists(bak):
            os.remove(bak)

        # Rename the existing path to path.bak
        if os.path.exists(path):
            os.rename(path, bak)

        # Rename the tmp path to the given path
        if os.path.exists(tmp):
            os.rename(tmp, path)

        # Clean up the bak file only if the given path exists
        if os.path.exists(path) and os.path.exists(bak):
            os.remove(bak)

    except:
        # Remove the tmp file if there are any issues
        if os.path.exists(tmp):
            os.remove(tmp)

        # Restore the path from the current .bak file
        if not os.path.exists(path) and os.path.exists(bak):
            os.rename(bak, path)

        raise
def write2json(path,data):
    path = normPath(path)
    data = json.dumps(data, indent=4)
    write(path, data)
def realPath(path):
    """
    Return the given path eliminating any symbolic link.

    :type path: str
    :rtype: str
    """
    path = os.path.realpath(path)
    path = os.path.expanduser(path)
    return normPath(path)


def normPath(path):
    """
    Return a normalized path containing only forward slashes.

    :type path: str
    :rtype: str or unicode
    """
    return unicode(path.replace("\\", "/"))
def relPath(data, start):
    """
    Return a relative version of all the paths in data from the start path.

    :type data: str
    :type start: str
    :rtype: str
    """
    rpath = start

    for i in range(0, 3):

        rpath = os.path.dirname(rpath)
        token = os.path.relpath(rpath, start)

        rpath = normPath(rpath)
        token = normPath(token)

        if rpath.endswith("/"):
            rpath = rpath[:-1]

        data = data.replace(rpath, token)

    return data
