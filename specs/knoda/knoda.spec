# $Id: $

# Authority: dries
# Upstream: 

Summary: Database frontend
Name: knoda
Version: 0.6.3
Release: 1
License: GPL
Group: Applications/Databases
URL: http://www.knoda.org/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://dl.sf.net/knoda/knoda-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc, make, libpng-devel, libart_lgpl-devel, arts-devel, gcc-c++, gettext, XFree86-devel, zlib-devel, qt-devel, libjpeg-devel, kdelibs-devel

# Screenshot: http://hk-classes.sourceforge.net/screenshots/relationeditor.html
# ScreenshotURL: http://hk-classes.sourceforge.net/screenshot.html

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
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%{_bindir}/knoda
%{_libdir}/libhk_kdeclasses.*
%{_libdir}/kde3/libhk_kdegridpart.*
%{_datadir}/apps/hk_kdeclasses/*.rc
%{_datadir}/apps/knoda/*.rc
%{_datadir}/*.png
%{_datadir}/services/hk_kdegridpart.desktop
%{_datadir}/icons/*/*/apps/*.png
%{_datadir}/applnk/Office/*.desktop
%{_datadir}/locale/*/LC_MESSAGES/knoda.mo
%{_datadir}/doc/HTML/en/knoda


%files devel
%defattr(-, root, root, 0755)
%{_includedir}/hk_*.h


%changelog
* Sat May 29 2004 Dries Verachtert <dries@ulyssis.org> - 0.6.3-1
- Initial package.

