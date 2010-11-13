# $Id$
# Authority: dag

### EL6 ships with plotutils-2.5-7.1.el6
# ExclusiveDist: el2 el3 el4 el5

%{?el4:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}

Summary: GNU vector and raster graphics utilities and libraries
Name: plotutils
Version: 2.5
Release: 1%{?dist}
License: GPL
Group: Applications/Productivity
URL: http://www.gnu.org/software/plotutils/

Source: ftp://ftp.gnu.org/gnu/plotutils/plotutils-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: flex, libpng-devel
%{!?_without_modxorg:BuildRequires: libX11-devel, libXaw-devel, libXt-devel, libXext-devel, xorg-x11-proto-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}
Requires: /sbin/install-info

%description
The GNU plotutils package contains software for both programmers and
technical users. Its centerpiece is libplot, a powerful C/C++ function
library for exporting 2-D vector graphics in many file formats, both
vector and raster. It can also do vector graphics animations. Besides
libplot, the package contains command-line programs for plotting
scientific data. Many of them use libplot to export graphics

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
%{__cp} -av lib/fontlist.c graph/
%{__cp} -av lib/fontlist.c pic2plot/
%{__cp} -av lib/fontlist.c plot/
%{__cp} -av lib/fontlist.c plotfont/
%{__cp} -av lib/fontlist.c tek2plot/

%build
%configure \
	--disable-static \
	--enable-libplotter \
	--enable-libxmi \
	--enable-ps-fonts-in-pcl
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%{__install} -d -m0755 rpmdoc/
%{__mv} -f %{buildroot}%{_datadir}/libplot/ rpmdoc/
%{__mv} -f %{buildroot}%{_datadir}/ode/ rpmdoc/
%{__mv} -f %{buildroot}%{_datadir}/pic2plot/ rpmdoc/
%{__mv} -f %{buildroot}%{_datadir}/tek2plot/ rpmdoc/

%post
/sbin/install-info %{_infodir}/libxmi.info %{_infodir}/dir || :
/sbin/install-info %{_infodir}/plotutils.info %{_infodir}/dir || :
/sbin/ldconfig

%preun
if [ $1 -eq 0 ]; then
    /sbin/install-info --delete %{_infodir}/libxmi.info %{_infodir}/dir || :
    /sbin/install-info --delete %{_infodir}/plotutils.info %{_infodir}/dir || :
fi

%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COMPAT COPYING KNOWN_BUGS NEWS PROBLEMS README THANKS TODO
%doc rpmdoc/*
%doc %{_mandir}/man1/*.1*
%doc %{_infodir}/*.info*
%{_bindir}/double
%{_bindir}/graph
%{_bindir}/ode
%{_bindir}/pic2plot
%{_bindir}/plot
%{_bindir}/plotfont
%{_bindir}/spline
%{_bindir}/tek2plot
%{_libdir}/libplot.so.*
%{_libdir}/libplotter.so.*
%{_libdir}/libxmi.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/plot.h
%{_includedir}/plotcompat.h
%{_includedir}/plotter.h
%{_includedir}/xmi.h
%{_libdir}/libplot.so
%{_libdir}/libplotter.so
%{_libdir}/libxmi.so
%exclude %{_libdir}/libplot.la
%exclude %{_libdir}/libplotter.la
%exclude %{_libdir}/libxmi.la

%changelog
* Thu May 24 2007 Dag Wieers <dag@wieers.com> - 2.5-1
- Initial package. (using DAR)
