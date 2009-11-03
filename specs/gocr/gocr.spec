# $Id$
# Authority: dag

Summary: Optical Character Recognition (OCR) program
Name: gocr
Version: 0.44
Release: 1%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://jocr.sourceforge.net/

Source: http://downloads.sf.net/jocr/gocr-%{version}.tar.gz
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
# Create mkinstalldirs -> gnome/mkinstalldirs in frontend directory
%{__ln_s} -f gnome/mkinstalldirs frontend/mkinstalldirs

%build
%configure
%{__make} %{?_smp_mflags}

cd frontend/gnome
%configure
cd -
%{__make} %{?_smp_mflags} -C frontend/gnome

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%{__make} install DESTDIR="%{buildroot}" -C frontend/gnome

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS CREDITS HISTORY README REMARK.txt REVIEW TODO
%doc doc/*.html
%doc %{_mandir}/man1/gocr.1*
%{_bindir}/gocr
%{_bindir}/gocr.tcl

%files devel
%defattr(-, root, root, 0755)
%doc api/doc/*.txt
%{_libdir}/libPgm2asc.a
%{_includedir}/gocr.h

%files gtk
%defattr(-, root, root, 0755)
%doc frontend/gnome/AUTHORS frontend/gnome/README frontend/gnome/TODO
%{_bindir}/gtk-ocr

%changelog
* Wed Mar  7 2007 Matthias Saou <http://freshrpms.net/> 0.44-1
- Update to 0.44.
- Remove no longer used patch.

* Mon Dec 18 2006 Dag Wieers <dag@wieers.com> - 0.43-1
- Updated to release 0.43.

* Mon Oct 23 2006 Matthias Saou <http://freshrpms.net/> 0.41-1
- Update to 0.41.
- Remove (apparently) no longer needed libm hack.
- Include user and devel docs only once, in one format.

* Sun May 11 2003 Dag Wieers <dag@wieers.com> - 0.37-0
- Initial package. (using DAR)
