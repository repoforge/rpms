# $Id$
# Authority: matthias

Summary: Portable C library for dynamically generating PDF files
Name: pdflib
Version: 6.0.2
Release: 1%{?dist}
License: See PDFlib-license.pdf
Group: System Environment/Libraries
URL: http://www.pdflib.com/
Source: http://www.pdflib.com/products/pdflib/download/601src/PDFlib-Lite-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
# perl, python, tcl bindings are disabled on purpose : the goal was only to
# get the php module built

%description
PDFlib is a C library for generating PDF files. It offers a graphics
API with support for drawing, text, fonts, images, and hypertext. Call
PDFlib routines from within your client program and voila: dynamic PDF
files! For detailed instructions on PDFlib programming and the
associated API, see the PDFlib Programming Manual, included in PDF
format in the PDFlib distribution.


%package devel
Summary: Development files for pdflib
Group: Development/Libraries
Requires: %{name} = %{version}, zlib-devel, libpng-devel

%description devel
PDFlib is a C library for generating PDF files. It offers a graphics
API with support for drawing, text, fonts, images, and hypertext. Call
PDFlib routines from within your client program and voila: dynamic PDF
files! For detailed instructions on PDFlib programming and the
associated API, see the PDFlib Programming Manual, included in PDF
format in the PDFlib distribution.

This package contains the files needed for compiling programs that will use
the PDFlib library.


%prep
%setup -n PDFlib-Lite-%{version}


%build
%configure \
    --with-perl="no"
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
# This one is required (6.0.1)
%{__mkdir_p} %{buildroot}%{_bindir}
%makeinstall
%{__install} -p -m 0644 bind/pdflib/cpp/pdflib.hpp \
    %{buildroot}%{_includedir}/pdflib.hpp


%clean
%{__rm} -rf %{buildroot}


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-, root, root, 0755)
%doc doc/pdflib/PDFlib-Lite-license.pdf readme.txt
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc doc/pdflib/changes.txt doc/pdflib/compatibility.txt
%doc doc/pdflib/PDFlib-manual.pdf doc/pdflib/readme-source-unix.txt
%{_bindir}/pdflib-config
%{_includedir}/*
%{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so


%changelog
* Mon Nov 21 2005 Matthias Saou <http://freshrpms.net/> 6.0.2-1
- Update to 6.0.2.

* Wed Jun  1 2005 Matthias Saou <http://freshrpms.net/> 6.0.1-1
- Update to 6.0.1 "Lite".

* Tue May 17 2005 Matthias Saou <http://freshrpms.net/> 4.0.3-2
- Use internal tiff and png libs to fix problems with external recent versions.
- Keep zlib-devel and libpng-devel reqs for the devel package, as it fails
  otherwise with unresolved symbols when trying to recompile the php module.

* Wed Feb  9 2005 Matthias Saou <http://freshrpms.net/> 4.0.3-1
- Spec file cleanup.

* Wed Apr 16 2003 Matthias Saou <http://freshrpms.net/>
- Grrr, lost my old spec and .src.rpm, rebuilt one based on the PLD spec.

