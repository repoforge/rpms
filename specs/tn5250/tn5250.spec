# $Id$
# Authority: dag
# Upstream: <linux5250$midrange,com>

%{?dist: %{expand: %%define %dist 1}}

Summary: 5250 Telnet protocol and terminal program
Name: tn5250
Version: 0.16.5
Release: 0
License: GPL 
Group: Applications/Communications
URL: http://tn5250.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/tn5250/tn5250-%{version}.tar.gz
Patch: tn5250-0.16.5-gcc33.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ncurses, slang-devel, openssl-devel, krb5-devel

%description
tn5250 is an implementation of the 5250 Telnet protocol.
It provide 5250 library and 5250 terminal emulation.

%package devel
Summary: header files and libraries needed for lib5250 development
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package includes the header files and libraries needed for
developing programs using lib5250.

%prep
%setup
%patch0 -b .gcc33

%build
%{?fc1:perl -pi.orig -e 's|^INCLUDES = |INCLUDES = -I/usr/kerberos/include |' src/Makefile.in}
%{?el3:perl -pi.orig -e 's|^INCLUDES = |INCLUDES = -I/usr/kerberos/include |' src/Makefile.in}
%{?rh9:perl -pi.orig -e 's|^INCLUDES = |INCLUDES = -I/usr/kerberos/include |' src/Makefile.in}
%configure \
	--with-slang \
	--with-x
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__install} -d -m0755 %{buildroot}%{_datadir}/%{name} \
			%{buildroot}%{_datadir}/pixmaps
%{__install} linux/5250.tcap linux/5250.terminfo %{buildroot}%{_datadir}/%{name}/
%{__install} *.png *.xpm %{buildroot}%{_datadir}/pixmaps
export TERMINFO="%{buildroot}%{_datadir}/terminfo/"
/usr/bin/tic linux/5250.terminfo
#/usr/bin/tic -o%{buildroot}%{_datadir}/terminfo/ linux/5250.terminfo

### Clean up docs
%{__rm} -f doc/Makefile*

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/*.la

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS COPYING ChangeLog NEWS README TODO linux/*.map doc/*
%doc %{_mandir}/man?/*
%{_bindir}/lp5250d
%{_bindir}/scs2*
%{_bindir}/tn3270d
%{_bindir}/tn5250
%{_bindir}/tn5250d
%{_bindir}/xt5250
%{_libdir}/*.so.*
%{_datadir}/%{name}/
%{_datadir}/pixmaps/*
%{_datadir}/terminfo/?/*

%files devel
%defattr(-, root, root, 0755)
%{_bindir}/*-config
%{_libdir}/*.a
%{_libdir}/*.so
%{_includedir}/*
%{_datadir}/aclocal/*.m4
#exclude %{_libdir}/*.la

%changelog
* Thu Apr 17 2003 Dag Wieers <dag@wieers.com> - 0.16.5-0
- Updated to release 0.16.5.

* Wed Feb  9 2000 Dag Wieers <dag@wieers.com> - 0.15.6-0
- Updated to release 0.15.6.

* Mon Nov 15 1999 Dag Wieers <dag@wieers.com> - 0.14.0-0
- Initial package.
