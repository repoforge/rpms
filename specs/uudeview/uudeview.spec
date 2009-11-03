# $Id$
# Authority: dag
# Upstream: Frank Pilhofer <fp$fpx,de>


%{?rh9:%define _without_tcltk_devel 1}
%{?rh8:%define _without_tcltk_devel 1}
%{?rh7:%define _without_tcltk_devel 1}
%{?el2:%define _without_tcltk_devel 1}

Summary: Smart decoder for uuencode, xxencode, Base64 and BinHex
Name: uudeview
Version: 0.5.20
Release: 1%{?dist}
License: GPL
Group: Applications/File
URL: http://www.fpx.de/fp/Software/UUDeview/

Source: http://www.fpx.de/fp/Software/UUDeview/download/uudeview-%{version}.tar.gz
Patch: uudeview-shared.patch
Patch1: uudeview-latex-psfig-deprecated.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: autoconf, libtool
BuildRequires: tetex-dvips, tetex-latex, transfig
%{!?_without_tcltk_devel:BuildRequires: tcl-devel >= 8.3, tk-devel}
%{?_without_tcltk_devel:BuildRequires: tcl >= 8.3, tk}

%description
The uudeview package contains an encoder and a decoder, for
transmitting and receiving binary files over electronic lines.
UUDeview can handle uuencode, xxencode, BinHex, yEnc and MIME
Base64 encoding. The decoder automatically detects the type of
encoding used. The uudeview package is a must for anyone who
does serious encoding and decoding.

%package gui
Summary: xdeview - uudeview with a GUI
Group: Applications/File
Requires: %{name} = %{version}-%{release}
Obsoletes: uudeview-x11

%description gui
xdeview - uudeview with a GUI.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup
%patch -p1
%patch1 -p1

%build
%{__libtoolize} --force --copy
%configure \
    --x-libraries="%{_prefix}/X11R6/%{_lib}" \
    --enable-tcl="%{_libdir}" \
    --enable-tk="%{_libdir}"
%{__make} %{?_smp_mflags}
%{__make} ps -C doc

%install
%{__rm} -rf %{buildroot}
%makeinstall \
    BINDIR="%{buildroot}%{_bindir}" \
    MANDIR="%{buildroot}%{_mandir}"
%makeinstall -C uulib

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc HISTORY IAFA-PACKAGE README* doc uudeview.lsm
%doc %{_mandir}/man1/uudeview.1*
%doc %{_mandir}/man1/uuenview.1*
#%{_bindir}/minews
%{_bindir}/uudeview
%{_bindir}/uuenview
%{_libdir}/libuu.so.*

%files gui
%defattr(-, root, root, 0755)
%doc %{_mandir}/man1/xdeview.*
%{_bindir}/uuwish
%{_bindir}/xdeview

%files devel
%defattr(-, root, root, 0755)
%doc doc/library.ps
%{_libdir}/libuu.a
%{_libdir}/libuu.so
%{_includedir}/fptools.h
%{_includedir}/uudeview.h
%exclude %{_libdir}/libuu.la

%changelog
* Thu Nov 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.5.20-1
- Added patch for the latex docs, thanks to Nicolas Thierry-Mieg.

* Wed Mar 03 2004 Bert de Bruijn <bert@debruijn.be> - 0.5.20-0
- Updated to release 0.5.20.

* Fri Nov 21 2003 Dag Wieers <dag@wieers.com> - 0.5.19-0
- Updated to release 0.5.19.

* Tue Jan 14 2003 Dag Wieers <dag@wieers.com> - 0.5.18-0
- Cleaned up SPEC file (use of macros)

* Tue Jan 14 2003 Bert de Bruijn <bert@debruijn.be> - 0.5.18
- split into multiple packages (based on PLD)

* Thu Dec 12 2002 Bert de Bruijn <bert@debruijn.be> - 0.5.18
- updated to 0.5.18, rebuilt for 8.0

* Thu Jul 22 1999 Tim Powers <timp@redhat.com>
- rebuilt for 6.1

* Thu Apr 15 1999 Michael Maher <mike@redhat.com>
- built package for 6.0

* Tue Sep 15 1998 Michael Maher <mike@redhat.com>
- built package
