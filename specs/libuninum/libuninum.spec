# $Id$
# Authority: dries
# Upstream: Bill Poser <billposer$alum,mit,edu>

Summary: Library for converting unicode strings to numbers
Name: libuninum
%define real_version 2.7
Version: 2.7
Release: 1
License: LGPL
Group: Development/Libraries
URL: http://billposer.org/Software/libuninum.html

Source: http://billposer.org/Software/Downloads/libuninum-%{real_version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gmp-devel

%description
libuninum is a library for converting Unicode strings to numbers. Internal 
computation is done using arbitrary precision arithmetic, so there is no 
limit on the size of the integer that can be converted. The value is returned 
as an ASCII decimal string, a GNU MP object, or an unsigned long integer. 
Auto-detection of the number system is provided. The number systems supported 
include Arabic, Armenian, Balinese, Bengali, Burmese, Chinese, Cyrillic, 
Devanagari, Egyptian, Ethiopic, Glagolitic, Greek, Gujarati, Gurmukhi, Hebrew, 
Kannada, Khmer, Klingon, Lao, Limbu, Malayalam, Mongolian, New Tai Lue, Nko, 
Old Italic, Old Persian, Oriya, Osmanya, Perso-Arabic, Phoenician, Roman 
Numerals, Tamil, Telugu, Tengwar, Thai, and Tibetan.

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
# the source tries to include for example 'uninum/uninum.h'
%{__ln_s} . uninum

%build
%configure \
    --disable-static
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%doc %{_mandir}/man1/numconv.1*
%{_bindir}/numconv
%{_bindir}/NumberConverter.tcl
%{_libdir}/libuninum.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/uninum/
%{_libdir}/libuninum.so
%exclude %{_libdir}/libuninum.la

%changelog
* Wed Dec 19 2007 Dries Verachtert <dries@ulyssis.org> - 2.7-1
- Updated to release 2.7.

* Mon Sep 24 2007 Dag Wieers <dag@wieers.com> - 2.6-1
- Updated to release 2.6.

* Sun Jun 17 2007 Dries Verachtert <dries@ulyssis.org> - 2.5-1
- Updated to release 2.5.

* Tue Apr 17 2007 Dries Verachtert <dries@ulyssis.org> - 2.3-1
- Updated to release 2.3.

* Mon Mar 12 2007 Dries Verachtert <dries@ulyssis.org> - 2.2-1
- Updated to release 2.2.

* Mon Feb 12 2007 Dries Verachtert <dries@ulyssis.org> - 2.1-1
- Updated to release 2.1.

* Sat Jan 27 2007 Dries Verachtert <dries@ulyssis.org> - 2.0.3-1
- Updated to release 2.0.3.

* Tue Jan 09 2007 Dag Wieers <dag@wieers.com> - 1.2.2-1
- Updated to release 1.2.2.

* Sun Jan 07 2007 Dries Verachtert <dries@ulyssis.org> - 1.2-1
- Initial package.
