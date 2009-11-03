# $Id$
# Authority: dag
# Upstream: Niklas Knutsson <nq$altern,org>

%define desktop_vendor rpmforge

Summary: Versatile desktop calculator library
Name: libqalculate
Version: 0.9.6
Release: 1%{?dist}
License: GPL
Group: System Environment/Libraries
URL: http://qalculate.sourceforge.net/

Source: http://dl.sf.net/qalculate/libqalculate-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: pkgconfig, cln-devel, gcc-c++, gmp-devel
BuildRequires: ImageMagick, gettext, glib2-devel >= 2.4
BuildRequires: intltool, perl-XML-Parser, libxml2-devel
BuildRequires: desktop-file-utils

%description
Qalculate! is a modern multi-purpose desktop calculator for GNU/Linux. It is
small and simple to use but with much power and versatility underneath.
Features include customizable functions, units, arbitrary precision and plotting.

This package contains the qulculate library which is used by the KDE and GTK+
GUI packages.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%package -n qalculate
Summary: Versatile desktop calculator
Group: Applications/Engineering
Requires: %{name} = %{version}-%{release}
Requires: gnuplot, wget

%description -n qalculate
Qalculate! is a modern multi-purpose desktop calculator for GNU/Linux. It is
small and simple to use but with much power and versatility underneath.
Features include customizable functions, units, arbitrary precision and plotting.

%prep
%setup

%{__cat} <<EOF >qalc.desktop
[Desktop Entry]
Name=Qalculate!
Comment=Powerful and easy to use desktop calculator
GenericName=Scientific Calculator
Exec=qalc
Terminal=false
Type=Application
StartupNotify=true
Categories=GNOME;Application;Utility;
Encoding=UTF-8
EOF

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang libqalculate

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor %{desktop_vendor}    \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	qalc.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog NEWS README TODO docs/reference/
%{_datadir}/qalculate/
%{_libdir}/libqalculate.so.*

%files devel
%{_includedir}/libqalculate/
%{_libdir}/libqalculate.a
%exclude %{_libdir}/libqalculate.la
%{_libdir}/libqalculate.so
%{_libdir}/pkgconfig/libqalculate.pc

%files -n qalculate -f libqalculate.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog NEWS README TODO docs/reference/
%{_bindir}/qalc
%{_datadir}/applications/%{desktop_vendor}-qalc.desktop
%exclude %{_docdir}/libqalculate-%{version}/

%changelog
* Sun Jun 17 2007 Dries Verachtert <dries@ulyssis.org> - 0.9.6-1
- Updated to release 0.9.6.

* Wed Dec 20 2006 Dag Wieers <dag@wieers.com> - 0.9.5-3
- Added the qalculate sub-package (this allows upgrade path from qalculate).

* Wed Dec 20 2006 Dries Verachtert <dries@ulyssis.org> - 0.9.5-2
- Renamed to libqalculate.
- Made a devel subpackage.

* Tue Dec 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.9.5-1
- Updated to release 0.9.5.

* Fri Jun 09 2006 Dag Wieers <dag@wieers.com> - 0.9.4-1
- Updated to release 0.9.4.

* Thu Mar 16 2006 Dag Wieers <dag@wieers.com> - 0.9.3-1
- Updated to release 0.9.3.

* Sun Dec 25 2005 Dries Verachtert <dries@ulyssis.org> - 0.9.2-1
- Updated to release 0.9.2.

* Sun Nov 13 2005 Dries Verachtert <dries@ulyssis.org> - 0.9.0-1
- Updated to release 0.9.0.

* Mon Oct 10 2005 Dries Verachtert <dries@ulyssis.org> - 0.8.2-1
- Updated to release 0.8.2.

* Fri Jun 10 2005 Dag Wieers <dag@wieers.com> - 0.8.1-1
- Updated to release 0.8.1.

* Sun Feb 06 2005 Dag Wieers <dag@wieers.com> - 0.7.2-1
- Updated to release 0.7.2.

* Mon Nov 22 2004 Dag Wieers <dag@wieers.com> - 0.7.1-1
- Updated to release 0.7.1.

* Sat Nov 13 2004 Dag Wieers <dag@wieers.com> - 0.7.0-1
- Updated to release 0.7.0.

* Wed Aug 25 2004 Dag Wieers <dag@wieers.com> - 0.6.2-1
- Initial package. (using DAR)
