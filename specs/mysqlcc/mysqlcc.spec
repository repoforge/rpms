# $Id$
# Authority: dag

%define dfi %(which desktop-file-install &>/dev/null; echo $?)

Summary: MySQL Control Center to administer MySQL databases
Name: mysqlcc
Version: 0.9.4
Release: 0.2%{?dist}
License: GPL
Group: Applications/Databases
URL: http://www.mysql.com/products/mysqlcc/

Source: http://www.mysql.com/get/Downloads/MySQLCC/%{name}-%{version}-src.tar.gz
Patch0: mysqlcc-path.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: pkgconfig, qt-devel >= 3.0.5, openssl-devel
#BuildRequires: mysql-devel >= 4.0

%description
mysqlcc is a platform independent graphical MySQL administration client.

%prep
%setup -n %{name}-%{version}-src
%patch0 -p1

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=MySQL Command Center
Comment=A tool to manage a MySQL database
Exec=mysqlcc
Type=Application
Terminal=false
StartupNotify=true
Icon=mysqlcc.xpm
Categories=Application;Development;
EOF

%build
source "%{_sysconfdir}/profile.d/qt.sh"
#configure
./configure \
	--prefix="%{_prefix}" \
	--libdir="%{_libdir}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__install} -Dp -m0755 mysqlcc %{buildroot}%{_bindir}/mysqlcc
%{__install} -Dp -m0644 xpm/applicationIcon.xpm %{buildroot}%{_datadir}/pixmaps/mysqlcc.xpm

%{__install} -d -m0755 %{buildroot}%{_datadir}/mysqlcc/translations/
%{__install} -p -m0644 syntax.txt *.wav %{buildroot}%{_datadir}/mysqlcc/
%{__install} -p -m0644 translations/*.{qm,ts} %{buildroot}%{_datadir}/mysqlcc/translations/

%if %{dfi}
	%{__install} -Dp -m0644 mysqlcc.desktop %{buildroot}%{_datadir}/gnome/apps/Development/mysqlcc.desktop
%else
        %{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
        desktop-file-install --vendor net                 \
                --add-category X-Red-Hat-Base              \
                --dir %{buildroot}%{_datadir}/applications \
                %{name}.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changelog.txt LICENSE.txt README.txt TODO.txt
%{_bindir}/*
%{_datadir}/mysqlcc/
%{_datadir}/pixmaps/*.xpm
%if %{dfi}
        %{_datadir}/gnome/apps/Development/*.desktop
%else
        %{_datadir}/applications/*.desktop
%endif

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.9.4-0.2
- Rebuild for Fedora Core 5.

* Thu Jan 08 2004 Dag Wieers <dag@wieers.com> - 0.9.4-0
- Initial package. (using DAR)
