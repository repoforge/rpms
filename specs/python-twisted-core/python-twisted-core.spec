# $Id$
# Authority: dag

### EL6 ships with python-twisted-core-8.2.0-4.el6
# ExclusiveDist: el2 el3 el4 el5

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%define real_name TwistedCore

Summary: Asynchronous networking framework written in Python
Name: python-twisted-core
Version: 8.1.0
Release: 1%{?dist}
License: MIT
Group: Development/Libraries
URL: http://twistedmatrix.com/trac/wiki/TwistedCore

Source0: http://tmrc.mit.edu/mirror/twisted/Core/8.1/%{real_name}-%{version}.tar.bz2
Source1: twisted-dropin-cache
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python-devel
BuildRequires: python-zope-interface
Requires: pyOpenSSL
Requires: python-zope-interface
Obsoletes: python-twisted <= 1.3.0
Provides: python-twisted = %{version}-%{release}

%description
An extensible framework for Python programming, with special focus
on event-based network programming and multiprotocol integration.

It is expected that one day the project will expanded to the point
that the framework will seamlessly integrate with mail, web, DNS,
netnews, IRC, RDBMSs, desktop environments, and your toaster.

%package doc
Summary: Documentation for Twisted Core
Group: Documentation
Requires: python-twisted-core = %{version}-%{release}

%description doc
Documentation for Twisted Core.

%prep
%setup -n %{real_name}-%{version}
%{__sed} -i -e '/^#! *\/usr\/bin\/python/d' twisted/internet/glib2reactor.py
%{__sed} -i -e '/^#!\/bin\/python/d'        twisted/trial/test/scripttest.py

find doc -name \*.py | xargs chmod a-x
chmod a-x doc/howto/listings/pb/copy_receiver.tac
%{__sed} -i 's/\r//' doc/howto/listings/udp/MulticastClient.py
%{__sed} -i 's/\r//' doc/howto/listings/udp/MulticastServer.py

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

### Man pages
%{__install} -d -m0755 %{buildroot}%{_mandir}/man1/
%{__install} -p -m0644 doc/man/*.1 %{buildroot}%{_mandir}/man1/
%{__rm} -rf doc/man/

### Clean up buildroot
### cfsupport is support for MacOSX Core Foundations, so we can delete it
%{__rm} -rf %{buildroot}%{python_sitearch}/twisted/internet/cfsupport/

### iocpreactor is a win32 reactor, so we can delete it
%{__rm} -rf %{buildroot}%{python_sitearch}/twisted/internet/iocpreactor/

### Remove the version we won't use
%{__rm} -f %{buildroot}%{python_sitearch}/twisted/python/_twisted_zsh_stub

### Script to regenerate dropin.cache
%{__install} -Dp -m0755 %{SOURCE1} %{buildroot}%{_libexecdir}/twisted-dropin-cache

%{__rm} -f %{buildroot}%{python_sitearch}/twisted/protocols/_c_urlarg.c
%{__rm} -f %{buildroot}%{python_sitearch}/twisted/python/_epoll.c

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CREDITS LICENSE NEWS README
%doc %{_mandir}/man1/*.1*
%{_bindir}/manhole
%{_bindir}/mktap
%{_bindir}/pyhtmlizer
%{_bindir}/t-im
%{_bindir}/tap2deb
%{_bindir}/tap2rpm
%{_bindir}/tapconvert
%{_bindir}/trial
%{_bindir}/twistd
%{_libexecdir}/twisted-dropin-cache
%{python_sitearch}/twisted/

%files doc
%defattr(-, root, root, 0755)
%doc doc/*

%changelog
* Wed Dec 10 2008 Dag Wieers <dag@wieers.com> - 8.1.0-1
- Initial package. (based on fedora)
