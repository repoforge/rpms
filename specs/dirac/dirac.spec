# $Id$
# Authority: dries
# Upstream: <dirac-develop$lists,sf,net>

Summary: General-purpose video codec
Name: dirac
Version: 0.5.4
Release: 1
License: MPL 1.1
Group: System Environment/Libraries
URL: http://sourceforge.net/projects/dirac

Source: http://dl.sf.net/dirac/dirac-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, xparam, doxygen, tetex-latex

%description
Dirac is a general-purpose video codec aimed at resolutions from QCIF
(180x144) to HDTV (1920x1080) progressive or interlaced. It uses wavelets,
motion compensation and arithmetic coding and aims to be competitive with
other state of the art codecs.

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

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__mv} -f %{buildroot}%{_docdir}/ rpm-doc/

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
#%doc %{_mandir}/man?/*
%{_bindir}/*
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc rpm-doc/*
%{_includedir}/dirac/
%{_libdir}/*.a
%{_libdir}/*.so
%exclude %{_libdir}/libdirac*.la
%{_libdir}/pkgconfig/dirac.pc

%changelog
* Mon Dec 05 2005 Dries Verachtert <dries@ulyssis.org> - 0.5.4-1
- Updated to release 0.5.4.

* Fri Aug 26 2005 Dries Verachtert <dries@ulyssis.org> - 0.5.3-1
- Updated to release 0.5.3.

* Thu Jun 09 2005 Dries Verachtert <dries@ulyssis.org> - 0.5.2-1
- Updated to release 0.5.2.

* Sat Dec 04 2004 Dries Verachtert <dries@ulyssis.org> - 0.5.0-1
- Updated to release 0.5.0.

* Wed Sep 22 2004 Dag Wieers <dag@wieers.com> - 0.4.3-1
- Updated to release 0.4.3.

* Sun Sep 12 2004 Dries Verachtert <dries@ulyssis.org> - 0.4.2
- Updated to release 0.4.2.

* Wed Sep 01 2004 Dries Verachtert <dries@ulyssis.org> - 0.4.1
- Updated to release 0.4.1.

* Tue Aug 24 2004 Dries Verachtert <dries@ulyssis.org> - 0.4.0
- Updated to release 0.4.0.

* Sat May 29 2004 Dries Verachtert <dries@ulyssis.org> - 0.3.0
- Updated to release 0.3.0.

* Mon May 17 2004 Dag Wieers <dag@wieers.com> - 0.2.0
- Updated to release 0.2.0.

* Tue May 11 2004 Dries Verachtert <dries@ulyssis.org> - 0.1.0
- Initial package.
