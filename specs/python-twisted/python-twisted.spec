# $Id$
# Authority: matthias
# Tag: test

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

Summary: Event-driven networking framework written in Python
Name: python-twisted
Version: 1.3.0
Release: 1
License: LGPL
Group: Applications/Internet
URL: http://www.twistedmatrix.com/

Source: http://twisted.sourceforge.net/Twisted-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python-devel
Requires: python
Obsoletes: python-Twisted < 1.3.0
Provides: python-Twisted = %{version}-%{release}

%description
An event-driven networking framework written in Python and licensed
under the LGPL. Twisted supports TCP, UDP, SSL/TLS, multicast, Unix
sockets, a large number of protocols (including HTTP, NNTP, SSH, IRC,
FTP, and others), and much more.

%package docs
Summary: Documentation for the Twisted networking framework
Group: Documentation

%description docs
An event-driven networking framework written in Python and licensed
under the LGPL. Twisted supports TCP, UDP, SSL/TLS, multicast, Unix
sockets, a large number of protocols (including HTTP, NNTP, SSH, IRC,
FTP, and others), and much more.

This package contains all the documentation for Twisted.

%prep
%setup -n Twisted-%{version}

%build
%{__python} setup.py build_ext

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

# the man pages are not installed, so install them
# and remove them from the doc dir
%{__mkdir_p} %{buildroot}%{_mandir}/man1
for man in doc/man/*.1; do
    %{__install} -p -m0644 ${man} %{buildroot}%{_mandir}/man1/
    %{__rm} -f ${man}
done

# set permissions on all doc files to 644
# because some examples are set executable and some aren't, which is
# inconsistent
find doc -type f -exec chmod 644 {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CREDITS ChangeLog README
%{_bindir}/*
%{python_sitearch}/twisted/
%{_mandir}/man1/*

%files docs
%defattr(-, root, root, 0755)
%doc doc/*

%changelog
* Tue Jun 22 2004 Matthias Saou <http://freshrpms.net> 1.3.0-1
- Update to 1.3.0.
- Spec file changes.

* Sun May 09 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 1.2.0-0.fdr.1: Update to new upstream release
- split off docs
- packaged man pages correctly
- patch to remove hardcoding of python2.2

* Fri Feb 13 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 1.1.1-0.fdr.1: Initial RPM release

