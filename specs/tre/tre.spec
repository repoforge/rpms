# $Id$
# Authority: dries
# Upstream: Ville Laurikari <vlaurika$cs,hut,fi>

Summary: Regexp matching library
Name: tre
Version: 0.7.5
Release: 1%{?dist}
License: GPL
Group: Development/Libraries
URL: http://laurikari.net/tre/

Source: http://laurikari.net/tre/tre-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gettext

%description
TRE is a lightweight, robust, efficient, portable, and POSIX compliant
regexp matching library. Key features include the agrep command line tool
for approximate regexp matching in the style of grep, an approximate
matching library API, portability, wide character and multibyte character
support, binary pattern and data support, complete thread safety,
consistently efficient matching, low memory consumption and small
footprint, and strict standards conformance.

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
%configure \
	--program-prefix="%{?_program_prefix}" \
	--enable-static
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog INSTALL LICENSE NEWS README THANKS TODO
%doc %{_mandir}/man1/agrep*
%{_bindir}/agrep
%{_libdir}/libtre.so.*

%files devel
%{_includedir}/tre/
%{_libdir}/libtre.a
%exclude %{_libdir}/libtre.la
%{_libdir}/libtre.so
%{_libdir}/pkgconfig/tre.pc

%changelog
* Sun Dec 10 2006 Dries Verachtert <dries@ulyssis.org> - 0.7.5-1
- Updated to release 0.7.5.

* Wed Aug 09 2006 Nico Kadel-Garcia <nkadel@comcast.net> - 0.7.4-2
- Include static libraries in -devel package.

* Tue May 24 2006 Dries Verachtert <dries@ulyssis.org> - 0.7.4-1
- Updated to release 0.7.4.

* Mon Apr 03 2006 Dries Verachtert <dries@ulyssis.org> - 0.7.3-1
- Updated to release 0.7.3.

* Tue Nov 08 2005 Dries Verachtert <dries@ulyssis.org> - 0.7.2-1
- Initial package.
