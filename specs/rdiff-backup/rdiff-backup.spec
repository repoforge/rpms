# $Id$
# Authority: dag
# Upstream: Ben Escoto <bescoto$stanford,edu>
# Upstream: <rdiff-backup-users$nongnu,org>

%define python_version %(python2 -c 'import sys; print sys.version[:3]')

Summary: Convenient and transparent local/remote incremental mirror/backup
Name: rdiff-backup
Version: 0.12.7
Release: 1
License: GPL
Group: Applications/Archiving
URL: http://rdiff-backup.stanford.edu/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://rdiff-backup.stanford.edu/OLD/%{version}/rdiff-backup-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python-devel >= 2.2, librsync-devel >= 0.9.6
Requires: python

%description
rdiff-backup is a script, written in Python, that backs up one directory
to another and is intended to be run periodically (nightly from cron for
instance). The target directory ends up a copy of the source directory,
but extra reverse diffs are stored in the target directory, so you can
still recover files lost some time ago.

The idea is to combine the best features of a mirror and an incremental
backup. rdiff-backup can also operate in a bandwidth efficient manner
over a pipe, like rsync. Thus you can use rdiff-backup and ssh to
securely back a hard drive up to a remote location, and only the
differences from the previous backup will be transmitted.

%prep
%setup

%build
python setup.py build

%install
%{__rm} -rf %{buildroot}
python setup.py install \
	--root "%{buildroot}"

### Create .pyo files
python -Oc 'from compileall import *; compile_dir("%{buildroot}%{_libdir}/python%{python_version}/site-packages/rdiff_backup")'

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGELOG COPYING examples.html FAQ.html README
%doc %{_mandir}/man1/rdiff-backup*
%{_bindir}/rdiff-backup
%dir %{_libdir}/python*/site-packages/rdiff_backup/
%{_libdir}/python*/site-packages/rdiff_backup/*.py
%{_libdir}/python*/site-packages/rdiff_backup/*.pyc
%ghost %{_libdir}/python*/site-packages/rdiff_backup/*.pyo
%{_libdir}/python*/site-packages/rdiff_backup/*.so

%changelog
* Mon Aug 02 2004 Dag Wieers <dag@wieers.com> - 0.12.7-1
- Cosmetic changes.

* Sun Nov 4 2001 Ben Escoto <bescoto@stanford.edu>
- Initial RPM.
