# $Id$
# Authority: dries
# Upstream: ar$oszine,de

Summary: Graphical subversion client
Name: qsvn
Version: 0.7.0
Release: 1%{?dist}
License: GPL
Group: Development/Tools
URL: http://www.anrichter.net/projects/qsvn/

Source: http://www.anrichter.net/projects/qsvn/chrome/site/qsvn-%{version}-src.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: qt4-devel, gcc-c++, gettext, cmake, apr-devel, subversion-devel

%description
QSvn is a graphical Subversion client.

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

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=Qsvn
Comment=Qt Subversion Tool
Exec=qsvn
Terminal=false
Type=Application
StartupNotify=true
Categories=Application;Qt;Development;
EOF

%build
mkdir build
cd build
cmake -D CMAKE_INSTALL_PREFIX=%{_prefix} -D CMAKE_BUILD_TYPE="Release" ../src
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
cd build
%{__make} install DESTDIR=%{buildroot}

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor rpmforge             \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	../%{name}.desktop

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog INSTALL README
%{_bindir}/qsvn
%{_libdir}/libsvnqt-qt4.so.*
%{_datadir}/applications/*-qsvn.desktop

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/svnqt-qt4/
%{_libdir}/libsvnqt-qt4.so

%changelog
* Tue Aug  5 2008 Dries Verachtert <dries@ulyssis.org> - 0.7.0-1
- Updated to release 0.7.0.

* Tue Apr 17 2007 Dries Verachtert <dries@ulyssis.org> - 0.5.0-1
- Updated to release 0.5.0.

* Tue Nov 14 2006 Dries Verachtert <dries@ulyssis.org> - 0.4.0-1
- Updated to release 0.4.0.

* Wed Mar 01 2006 Dries Verachtert <dries@ulyssis.org> - 0.3.0-1
- Initial package.
