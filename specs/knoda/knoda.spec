# $Id$

# Authority: dries
# Upstream: bugreport@knoda.org
# Screenshot: http://hk-classes.sourceforge.net/screenshots/relationeditor.html
# ScreenshotURL: http://hk-classes.sourceforge.net/screenshot.html

Summary: Database frontend
Name: knoda
Version: 0.7.1
Release: 1
License: GPL
Group: Applications/Databases
URL: http://www.knoda.org/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://dl.sf.net/knoda/knoda-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc, make, libpng-devel
BuildRequires: libart_lgpl-devel, arts-devel
BuildRequires: gcc-c++, gettext, XFree86-devel
BuildRequires: zlib-devel, qt-devel, libjpeg-devel
BuildRequires: kdelibs-devel, hk_classes
BuildRequires: python-devel, python
%{?fc3:BuildRequires: libselinux-devel}
%{?fc2:BuildRequires: libselinux-devel}

%description
knoda is a database frontend for KDE. It is based on hk_classes. 
Knoda allows you to:
* define and delete databases
* create, alter and delete tables and indices
* add, change and delete data in tables
* define, execute and store sql queries
* import and export CSV data
* define and use forms
* define and print reports
* write your own extensions using the integrated Python interpreter as
scripting language

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
%{__perl} -pi.orig -e 's|\$\(datadir\)|\$(picsdatadir)|g' hk_kdeclasses/pics/Makefile.* knoda/pics/Makefile.*
%{__perl} -pi.orig -e 's|^datadir|picsdatadir|g' hk_kdeclasses/pics/Makefile.* knoda/pics/Makefile.*
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
# with stripping: 21Mb -> 2Mb
%{__strip} %{buildroot}%{_libdir}/libhk_kdeclasses.so
%find_lang %{name}

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%{_bindir}/knoda
%{_libdir}/libhk_kdeclasses.*
%{_libdir}/kde3/libhk*
%{_datadir}/apps/hk_kdeclasses
%{_datadir}/apps/knoda
%{_datadir}/services/*.desktop
%{_datadir}/icons/*/*/apps/*.png
%{_datadir}/applnk/Office/*.desktop
%{_datadir}/doc/HTML/en/knoda

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/hk_*.h

%changelog
* Sat Oct 02 2004 Dries Verachtert <dries@ulyssis.org> - 0.7.1-1
- Update to version 0.7.1.

* Mon Jul 12 2004 Dries Verachtert <dries@ulyssis.org> - 0.7-1
- Update to version 0.7.

* Sat May 29 2004 Dries Verachtert <dries@ulyssis.org> - 0.6.3-1
- Initial package.
