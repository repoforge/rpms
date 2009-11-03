# $Id$
# Authority: dries
# Upstream: Greg Roelofs

Summary: PNG tester and debugger
Name: pngcheck
Version: 2.3.0
Release: 1%{?dist}
License: BSD
Group: Applications/Multimedia
URL: http://www.libpng.org/pub/png/apps/pngcheck.html

Source: http://dl.sf.net/png-mng/pngcheck-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: zlib-devel

%description
pngcheck is the official PNG tester and debugger. Originally designed simply
to test the CRCs within a PNG image file (e.g., to check for ASCII rather
than binary transfer), it has since been extended to check and optionally
print almost all the information about a PNG image and to verify that it
conforms to the PNG specification. It also includes partial support for MNG
animations.

%prep
%setup

%build
%{__make} %{?_smp_mflags} -f Makefile.unx ZINC="-I%{_includedir}" ZPATH="%{_libdir}"

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m755 pngcheck %{buildroot}%{_bindir}/pngcheck

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGELOG README
%{_bindir}/pngcheck

%changelog
* Tue Jul 10 2007 Dries Verachtert <dries@ulyssis.org> - 2.3.0-1
- Updated to release 2.3.0.

* Tue Dec 05 2006 Dries Verachtert <dries@ulyssis.org> - 2.2.0-1
- Updated to release 2.2.0.

* Tue Aug 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.1.0-1
- Updated to release 2.1.0.

* Mon Jul 18 2005 Dries Verachtert <dries@ulyssis.org> - 2.0.0-1
- Initial package.
