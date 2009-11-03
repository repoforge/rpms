# $Id$
# Authority: dries
# Upstream: Alessandro Rubini <rubini$linux,it>

Summary: Create printouts of barcodes
Name: barcode
Version: 0.98
Release: 1.2%{?dist}
License: GPL
Group: Applications/Publishing
URL: http://www.gnu.org/software/barcode/barcode.html

Source: ftp://ftp.gnu.org/pub/gnu/barcode/barcode-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
GNU-barcode is meant to solve most needs in barcode creation with a
conventional printer. It can create printouts for the conventional
product-tagging standards: UPC-A, UPC-E, EAN-13, EAN-8, ISBN, and
several others. Output is generated as either Postscript, Encapsulated
Postscript, or PCL (other back-ends may be added if needed). The
package is released as both a library and a command-line frontend, so
that you can include barcode-generation into your application.

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

%{__perl} -pi.orig -e 's|/lib\b|/%{_lib}|g' configure Makefile.in

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall "MAN1DIR=%{buildroot}%{_mandir}/man1" MAN3DIR="%{buildroot}%{_mandir}/man3" INFODIR="%{buildroot}%{_infodir}"
# avoid file conflict on fedora systems
%{__mv} %{buildroot}%{_mandir}/man1/barcode.1 %{buildroot}%{_mandir}/man1/gnubarcode.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING INSTALL README TODO
%doc %{_mandir}/man1/gnubarcode*
%doc %{_mandir}/man3/barcode*
%doc %{_infodir}/barcode.info*
%{_bindir}/barcode

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/barcode.h
%{_libdir}/libbarcode.a

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.98-1.2
- Rebuild for Fedora Core 5.

* Sat Jan 14 2006 Dries Verachtert <dries@ulyssis.org> - 0.98-1
- Initial package.
