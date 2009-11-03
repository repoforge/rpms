# $Id$
# Authority: dag
# Upstream: Paul Sheer <psheer$obsidian,co,za>

Summary: Easy to use ftp mirroring package
Name: mirrordir
Version: 0.10.49
Release: 1.2%{?dist}
License: GPL
Group: Applications/Internet
URL: ftp://ftp.obsidian.co.za/pub/mirrordir/

Source: ftp://ftp.obsidian.co.za/pub/mirrordir/mirrordir-%{version}.tar.bz2
Patch: mirrordir-0.10.49-datadir-fix.patch
Patch1: mirrordir-0.10.49-zlib-1.1.3-zfree.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Easy to use ftp mirroring package - simply use
mirrordir ftp://some.where.com/dir /some/local/dir

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup
%patch -p1
%patch1 -p1 -b .zfree

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__perl} -pi -e 's|-f \$\(bindir\)/mirrordir \$|-f \$\(bindir\)/mirrordir \$\(DESTDIR\)\$|' src/Makefile
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS ChangeLog COPYING NEWS README THANKS TODO
%doc %{_mandir}/man1/copydir.1*
%doc %{_mandir}/man1/forward.1*
%doc %{_mandir}/man1/mirrordir.1*
%doc %{_mandir}/man1/pslogin.1*
%doc %{_mandir}/man1/recursdir.1*
%doc %{_mandir}/man1/secure-mcserv.1*
%config(noreplace) %{_sysconfdir}/secure*
%config(noreplace) %{_sysconfdir}/pam.d/*
%{_bindir}/copydir
%{_bindir}/forward
%{_bindir}/mirrordir
%{_bindir}/pslogin
%{_bindir}/recursdir
%{_bindir}/secure-mcserv
%{_datadir}/mirrordir/
%{_libdir}/libdiffie.so.*
%{_libdir}/libmirrordirz.so.*

%files devel
%defattr(-, root, root, 0755)
%{_libdir}/libdiffie.a
%exclude %{_libdir}/libdiffie.la
%{_libdir}/libdiffie.so
%{_libdir}/libmirrordirz.a
%exclude %{_libdir}/libmirrordirz.la
%{_libdir}/libmirrordirz.so

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.10.49-1.2
- Rebuild for Fedora Core 5.

* Thu Feb 09 2006 Dag Wieers <dag@wieers.com> - 0.10.49-1
- Initial package. (using DAR)
