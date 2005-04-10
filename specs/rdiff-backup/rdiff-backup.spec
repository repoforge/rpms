# $Id$
# Authority: dag
# Upstream: Ben Escoto <bescoto$stanford,edu>
# Upstream: <rdiff-backup-users$nongnu,org>

%define python_version %(python2 -c 'import sys; print sys.version[:3]')
%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

Summary: Convenient and transparent local/remote incremental mirror/backup
Name: rdiff-backup
Version: 0.12.8
Release: 1
License: GPL
Group: Applications/Archiving
URL: http://www.nongnu.org/rdiff-backup/

Source: http://savannah.nongnu.org/download/rdiff-backup/rdiff-backup-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python-devel >= 2.2, librsync-devel >= 0.9.6, python
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
%doc %{_mandir}/man1/rdiff-backup.1*
%{_bindir}/rdiff-backup
%dir %{python_sitearch}/rdiff_backup/
%{python_sitearch}/rdiff_backup/*.py
%{python_sitearch}/rdiff_backup/*.pyc
%ghost %{python_sitearch}/rdiff_backup/*.pyo
%{python_sitearch}/rdiff_backup/*.so

%changelog
* Sat Apr 09 2005 Dag Wieers <dag@wieers.com> - 0.12.8-1
- Updated to release 0.12.8.

* Mon Aug 02 2004 Dag Wieers <dag@wieers.com> - 0.12.7-1
- Cosmetic changes.

* Sun Nov 4 2001 Ben Escoto <bescoto@stanford.edu>
- Initial RPM.
