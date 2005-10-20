# $Id$

# Authority: dag

Summary: Optical Character Recognition (OCR) program
Name: gocr
Version: 0.37
Release: 0
License: GPL
Group: Applications/Multimedia
URL: http://altmark.nat.uni-magdeburg.de/~jschulen/ocr/

Source: http://dl.sf.net/jocr/gocr-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk+-devel >= 1.2.8, netpbm-devel

%description
GOCR is an optical character recognition program, released under the
GNU General Public License. It reads images in many formats (pnm, pbm,
pgm, ppm, some pcx and tga image files) and outputs a text file.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%package gtk
Summary: GTK frontend for gocr
Group: Applications/Multimedia
Requires: %{name} = %{version}-%{release}

%description gtk
This package contains a gtk+ frontend to gocr.

%prep
%setup
%{__ln_s} -f gnome/mkinstalldirs frontend/mkinstalldirs

%build
# needed for configure
export CFLAGS=-lm
%configure
%{__perl} -pi -e 's|^LDFLAGS=|LDFLAGS=-lm |g;' Makefile */Makefile
%{__make} %{?_smp_mflags}
  
cd frontend/gnome
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall DESTDIR=""
%makeinstall DESTDIR="" -C frontend/gnome

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS CREDITS HISTORY README REMARK.txt REVIEW TODO
%doc doc/*.html doc/*.txt
%doc %{_mandir}/man?/*
%{_bindir}/gocr

%files devel
%defattr(-, root, root, 0755)
%doc api/doc/*.tex api/doc/*.txt
%doc AUTHORS
%{_libdir}/*.a
%{_includedir}/gocr.h

%files gtk
%defattr(-, root, root, 0755)
%doc frontend/gnome/AUTHORS frontend/gnome/README frontend/gnome/TODO
%{_bindir}/gtk-ocr

%changelog
* Sun May 11 2003 Dag Wieers <dag@wieers.com> - 0.37-0
- Initial package. (using DAR)
