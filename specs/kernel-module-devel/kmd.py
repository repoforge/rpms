#!/usr/bin/python

# vi:si:et:sw=4:sts=4:ts=4

import sys
import os
import commands
import string
import getopt


usage = '''Usage: kmd.py -l (libdir) -u (uname -r) (list of rpms)
'''

help = '''kmd.py 0.0.1

Unpack and compare rpms, and create a symlink/copy forest
That is the smallest one recreating the different package lists

'''


def error (message):
    sys.stderr.write ("ERROR: %s\n" % message)
    sys.exit (1)

# set up directories for comparison
# given the starting set of rpm files,
# - unpack them
# - move lib/modules/*/build to $arch.$type
# - return a list of paths to directories that contain all build files
#   relative to ./unpack

def setup (rpms):
    ret = []
    print rpms
    tmpdir = os.tempnam ('.')
    os.system ("mkdir unpack")
    for rpm in rpms:
        print "Unpacking %s" % rpm
        rpmpath = os.path.realpath (rpm)
        rpmname = os.path.split (rpm)[1]
        unpack = os.path.join ('unpack', rpmname)
        if os.path.exists (unpack):
            print "%s already exists, keeping" % unpack
        else:
            os.system ("rm -rf %s" % tmpdir)
            os.system ("mkdir %s" % tmpdir)
            cmd = "cd %s && rpm2cpio %s | cpio -id" % (tmpdir, rpmpath)
            if os.system (cmd) != 0:
                error ("Could not unpack %s" % rpmpath)
                return
            cmd = "mv %s/lib/modules/*/build %s" % (tmpdir, unpack)
            os.system (cmd)
        ret.append (rpmname)

    os.system ("rm -rf %s" % tmpdir)
    return ret

# run find on the unpack dir, with the given options
# return the result, but with . and all starting ./ removed
def find_unpack (dir, options):
    ret = []
    cmd = "cd unpack/%s && find %s" % (dir, options)
    list = commands.getoutput (cmd).split ('\n')
    for line in list:
        # remove "./"
        if len(line) > 1:
            ret.append (line[2:])
    return ret
 
# given a directory under unpack/
# return a list of all file and directory paths under it
def get_path_names (dir):
    return find_unpack (dir, '')
 
# given a list of directories under unpack/
# return a dict of lists of directory paths under that directory
#        indexed on directory
# -> dict A
def get_dict_path_names (dirs):
    result = {}
    for dir in dirs:
        result[dir] = get_path_names (dir)
    return result
 
# given a list of directories under unpack/
# return a list of all the file and directory paths under it
#        that are common to all given dirs
# -> set B
def get_common_path_names (dirs):
    print "Getting a list of common path names"
    number = len (dirs)
    paths = {}
    ret = []
    for dir in dirs:
        list = get_path_names (dir)
        for path in list:
            if paths.has_key (path):
                paths[path] += 1
            else:
                paths[path] = 1
    for path in paths.keys():
        if paths[path] != number:
            print "Path %s has count of %d" % (path, paths[path])
        else:
            ret.append (path)

    print "Got a list of common path names"
    return ret

# given a list of directories under unpack/
# return a list of all files that are different in any of the four
# (skipping of course the first path, which is the specific subdir)
# -> set C
def get_any_difference_list (dirs):
    print "Getting a list of all files different in any of the given dirs"
    result = []
    for dir in dirs[1:]:
        cmd = "cd unpack && diff -Naur %s %s| grep \"^diff -Naur \"" % (dirs[0], dir)
        list = commands.getoutput (cmd).split ('\n')
        symlinks = find_unpack (dir, "-type l")
        # each line in list looks like
        # diff -Naur kernel-2.6.5-1.358.i586.rpm/arch/i386/kernel/asm-offsets.s kernel-smp-2.6.5-1.358.i686.rpm/arch/i386/kernel/asm-offsets.s
        for line in list:
            file = line.split ()[2]
            # remove dir and trailing slash
            if file.startswith (dirs[0]):
                file = file[len (dirs[0]) + 1:]
            # if it's a file with a symlink as parent, skip it
            symlink_parent = 0
            for symlink in symlinks:
                # we don't want include/asm to throw out include/asm-i386
                if file.startswith (symlink + '/'):
                    print "DEBUG: file %s starts with orig symlink %s, skipping" % (file, symlink)
                    symlink_parent = 1
                    break
            if symlink_parent == 1:
                # jump out of for loop and don't append this file
                continue
            
            # append if not yet there
            if not file in result:
                result.append (file)
    return result
 
# given a path, construct a list of all its parents
def get_parents (path):
        paths = []
        dirname = os.path.dirname (path)
        while dirname:
            paths.append (dirname)
            dirname = os.path.dirname (dirname)
        return paths
 
# given a list of files that could be symlinked
#       and a list of files that are different
# return a list with all the unlinkable paths removed from it
def remove_unlinkable_paths (symlink_list, different_files):
    for file in different_files:
        paths = get_parents (file)
        paths.append (file)
        for path in paths:
            try:
                symlink_list.remove (path)
                print "removed path %s from symlink_list" % path
            except ValueError:
                print "path %s was not in symlink_list" % path
    return symlink_list

# given a list of paths, remove all paths that are a child of another one
# in the given list
def remove_children (paths):
    result = []
    for path in paths:
        parent_in_list = 0
        parents = get_parents (path)
        for parent in parents:
            if parent in paths:
                parent_in_list = 1
        if parent_in_list == 0:
            result.append (path)
    return result
    
# main
libdir = ''
uname = ''
opts, args = getopt.getopt (sys.argv[1:], "vhl:u:", [ "version", "help", "libdir=", "uname=" ])
for opt, arg in opts:
    if opt in ('-l', '--libdir'):
        libdir = arg
    elif opt in ('-u', '--uname'):
        uname = arg
    elif opt in ('-v', '--version'):
        print "kmd.py 0.0.1"
        sys.exit (0)
    elif opt in ('-h', '--help'):
        print usage
        sys.exit (0)

if not args:
    sys.stderr.write (help)
    sys.stderr.write (usage)
    sys.exit (0)

if not libdir:
    sys.stderr.write ("Please supply a lib directory (eg. /usr/libdir) using -l.\n")
    sys.stderr.write (usage)
    sys.exit (1)

if not uname:
    sys.stderr.write ("Please supply a uname -r value using -u.\n")
    sys.stderr.write (usage)
    sys.exit (1)

dirs = setup (args)
# dict A
paths = get_dict_path_names (dirs)
# set B
common_pathnames = get_common_path_names (dirs)
# set C
different_files = get_any_difference_list (dirs)

# set D
symlink_list = common_pathnames[:]
symlink_list.sort ()
symlink_list = remove_unlinkable_paths (symlink_list, different_files)
symlink_list = remove_children (symlink_list)
symlink_list.sort ()


for rpm in paths.keys ():
    # store resulting dirs under kernel-module-devel-(release)/(rpm name)
    targetdir = os.path.join ('kernel-module-devel-' + uname, rpm)
    print "Creating targetdir %s" % targetdir
    cmd = 'rm -rf %s' % (targetdir)
    os.system (cmd)
    cmd = 'mkdir -p %s' % (targetdir)
    os.system (cmd)
    # first create dirs and copy files from the list of different files
    for path in paths[rpm]:
        if not path in different_files:
            continue
        source = os.path.join ('unpack', rpm, path)
        if os.path.isdir (source):
            print "Creating directory %s" % path
            cmd = 'mkdir -p %s/%s' % (targetdir, path)
            print "DEBUG: %s" % cmd
            if os.system (cmd) != 0:
                sys.stderr.write ('Could not execute %s' % cmd)
                sys.exit (1)
        else:
            print "Copying file %s" % path
            # create parent dir if necessary
            dir = os.path.join (targetdir, os.path.dirname (path))
            if not os.path.exists (dir):
                cmd = 'mkdir -p %s' % dir
                print "DEBUG: %s" % cmd
                if os.system (cmd) != 0:
                    sys.stderr.write ('Could not execute %s' % cmd)
                    sys.exit (1)
            cmd = 'cp -p %s %s/%s' % (source, targetdir, path)
            print "DEBUG: %s" % cmd
            if os.system (cmd) != 0:
                sys.stderr.write ('ERROR: Could not execute %s' % cmd)
                sys.exit (1)

    # then symlink all files from symlink_list
    for path in symlink_list:
        source = os.path.join (libdir, 'kernel-module-devel-' + uname, 'common', path)
        # create parent dir if necessary
        dir = os.path.join (targetdir, os.path.dirname (path))
        if not os.path.exists (dir):
            cmd = 'mkdir -p %s' % dir
            print "DEBUG: %s" % cmd
            if os.system (cmd) != 0:
                sys.stderr.write ('Could not execute %s\n' % cmd)
                sys.exit (1)
        # now symlink
        cmd = "ln -sf %s %s/%s" % (source, targetdir, path)
        print "DEBUG: ln: %s" % cmd
        if os.system (cmd) != 0:
            sys.stderr.write ('Could not execute %s\n' % cmd)
            sys.exit (1)

    # now copy over all original symlinks
    symlinks = find_unpack (rpm, "-type l")
    print "DEBUG: copy original symlinks:\n%s\nendoflist\n" % symlinks
    for path in symlinks:
        source = os.path.join ('unpack', rpm, path)
        target = os.path.join (targetdir, path)
        print "Copying symlink file %s" % path
        # create parent dir if necessary
        dir = os.path.join (targetdir, os.path.dirname (path))
        if not os.path.exists (dir):
            cmd = 'mkdir -p %s' % ( os.path.dirname (target))
            print "DEBUG: %s" % cmd
            if os.system (cmd) != 0:
                sys.stderr.write ('Could not execute %s' % cmd)
                sys.exit (1)
        # remove target if already exists
        if os.path.exists (target):
            os.unlink (target)

        cmd = 'cp -p --no-dereference %s %s' % (source, target)
        print "DEBUG: symlink copy: %s" % cmd
        if os.system (cmd) != 0:
            sys.stderr.write ('ERROR: symlink copy: Could not execute %s' % cmd)
            sys.exit (1)


