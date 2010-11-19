# $Id$
# Authority: dag

Summary: Optical Character Recognition (OCR) program
Name: gocr
Version: 0.49
Release: 1%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://jocr.sourceforge.net/

Source: http://www-e.uni-magdeburg.de/jschulen/ocr/gocr-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Obsoletes: gocr-devel <= %{version}-%{release}
Obsoletes: gocr-gtk <= %{version}-%{release}

BuildRequires: netpbm-devel

%description
GOCR is an optical character recognition program, released under the
GNU General Public License. It reads images in many formats (pnm, pbm,
pgm, ppm, some pcx and tga image files) and outputs a text file.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS CREDITS HISTORY README REMARK.txt REVIEW TODO
%doc doc/*.html
%doc %{_mandir}/man1/gocr.1*
%{_bindir}/gocr
%{_bindir}/gocr.tcl

%changelog
* Fri Nov 19 2010 Dag Wieers <dag@wieers.com> - 0.49-1
- Updated to release 0.49.

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
