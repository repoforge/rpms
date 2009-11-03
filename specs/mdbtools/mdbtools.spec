# $Id$
# Authority: dag

%{?dtag: %{expand: %%define %dtag 1}}

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}

%define desktop_vendor rpmforge

Summary: Access data stored in Microsoft Access databases
Name: mdbtools
Version: 0.5
Release: 1%{?dist}
License: LGPL/GPL
Group: System Environment/Libraries
URL: http://mdbtools.sourceforge.net/

Source: http://dl.sf.net/mdbtools/mdbtools-%{version}.tar.gz
Patch0: mdbtools-0.5-gcc34.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: unixODBC-devel >= 2.0.0, libgnomeui-devel >= 2.0, bison, flex
BuildRequires: glib-devel, glib2-devel
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}

%description
MDB Tools is a suite of libraries and program for accessing data stored
in Microsoft Access databases.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%package gui
Summary: gmdb2 graphical interface for MDB Tools
Group: Applications/Databases
Requires: %{name} = %{version}-%{release}

%description gui
The mdbtools-gui package contains the gmdb2 graphical user interface
for MDB Tools

%prep
%setup
%patch0 -p1

%{__cat} <<EOF >gmdb2.desktop
[Desktop Entry]
Name=MDB database explorer
Comment=Explorer your MDB database files
Icon=gnome-day.png
Exec=gmdb2
Terminal=false
Type=Application
Category=Application;Development;
EOF

%build
%configure \
	--enable-sql \
	--with-unixodbc="%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%if %{?_without_freedesktop:1}0
        %{__install} -Dp -m0644 gmdb2.desktop %{buildroot}%{_datadir}/gnome/apps/Development/gmdb2.desktop
%else
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --vendor %{desktop_vendor}    \
		--add-category X-Red-Hat-Base              \
		--dir %{buildroot}%{_datadir}/applications \
		gmdb2.desktop
%endif

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING* INSTALL NEWS README TODO
%doc doc/*.html doc/*.txt
%doc %{_mandir}/man?/*
%{_bindir}/mdb-*
%{_bindir}/pr*
%{_bindir}/unittest
%{_bindir}/updrow
%{_libdir}/libmdb*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc HACKING
%{_libdir}/libmdb*.a
%exclude %{_libdir}/libmdb*.la
%{_libdir}/libmdb*.so
%{_includedir}/*.h

%files gui
%defattr(-, root, root, 0755)
%doc %{_datadir}/gnome/help/gmdb/
%{_bindir}/gmdb2
%{_datadir}/gmdb/
%{?_without_freedesktop:%{_datadir}/gnome/apps/Development/gmdb2.desktop}
%{!?_without_freedesktop:%{_datadir}/applications/%{desktop_vendor}-gmdb2.desktop}

%changelog
* Thu Jan 18 2007 Dag Wieers <dag@wieers.com> - 0.5-1
- Fixed EL4 build.

* Fri Jun 13 2003 Dag Wieers <dag@wieers.com> - 0.5-0
- Initial package. (using DAR)
