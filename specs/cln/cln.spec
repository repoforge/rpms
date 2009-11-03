# $Id$
# Authority: dag

Summary: C++ Class Library for Numbers
Name: cln
Version: 1.1.13
Release: 1%{?dist}
License: GPL
Group: System Environment/Libraries
URL: http://www.ginac.de/CLN/

Source: http://www.ginac.de/CLN/cln-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gmp-devel, gcc-c++

%description
A GPLed collection of C++ math classes and functions, that will bring
efficiency, type safety, algebraic syntax to everyone in a memory
and speed efficient library.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: /sbin/install-info

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

# prepare documents
%{__rm} -rf documents/
%{__mkdir} documents/
%{__mv} %{buildroot}%{_datadir}/html documents/
%{__cp} -p --parents examples/*.cc documents/

%{__rm} -rf %{buildroot}%{_datadir}/dvi/

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%post devel
/sbin/install-info --section="Math" %{_infodir}/cln.info.gz %{_infodir}/dir

%preun devel
if [ "$1" -eq 0 ]; then
	/sbin/install-info --delete %{_infodir}/cln.info.gz %{_infodir}/dir
fi

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING NEWS README TODO*
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc documents/*
%doc %{_mandir}/man1/cln-config.1*
%doc %{_infodir}/*.info*
%{_bindir}/cln-config
%{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so
%{_includedir}/cln/
%{_datadir}/aclocal/cln.m4
%{_libdir}/pkgconfig/cln.pc

%changelog
* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 1.1.13-1
- Updated to release 1.1.13.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.1.11-1.2
- Rebuild for Fedora Core 5.

* Mon Dec 26 2005 Dag Wieers <dag@wieers.com> - 1.1.11-1
- Updated to release 1.1.11.

* Sun Nov 13 2005 Dries Verachtert <dries@ulyssis.org> - 1.1.10-1
- Updated to release 1.1.10.

* Fri Dec 10 2004 Dag Wieers <dag@wieers.com> - 1.1.8-2
- Fixed Group tag.

* Wed Aug 25 2004 Dag Wieers <dag@wieers.com> - 1.1.8-1
- Initial package. (using DAR)
