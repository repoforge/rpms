# $Id$

# Authority: dag

%define dfi %(which desktop-file-install &>/dev/null; echo $?)

Summary: MySQL Control Center to administer MySQL databases
Name: mysqlcc
Version: 0.9.4
Release: 0
License: GPL 	
Group: Applications/Databases
URL: http://www.mysql.com/products/mysqlcc/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

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
%{?rhfc1:export QTDIR="/usr/lib/qt-3.1"}
%{?rhel3:export QTDIR="/usr/lib/qt-3.1"}
%{?rh90:export QTDIR="/usr/lib/qt3"}
%{?rh80:export QTDIR="/usr/lib/qt3"}
%{?rh73:export QTDIR="/usr/lib/qt2"}
%{?rh62:export QTDIR="/usr/lib/qt-2.1.0"}
#configure
./configure \
	--prefix="%{_prefix}" \
	--libdir="%{_libdir}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__install} -d -m0755 %{buildroot}%{_bindir} \
			%{buildroot}%{_datadir}/mysqlcc/translations/ \
			%{buildroot}%{_datadir}/applications/ \
			%{buildroot}%{_datadir}/pixmaps/
%{__install} -m0755 mysqlcc %{buildroot}%{_bindir}
%{__install} -m0644 syntax.txt *.wav %{buildroot}%{_datadir}/mysqlcc/
%{__install} -m0644 translations/*.{qm,ts} %{buildroot}%{_datadir}/mysqlcc/translations/
%{__install} -m0644 xpm/applicationIcon.xpm %{buildroot}%{_datadir}/pixmaps/mysqlcc.xpm

%if %{dfi}
	%{__install} -d -m0755 %{buildroot}%{_datadir}/gnome/apps/Development/
	%{__install} -m0644 %{name}.desktop %{buildroot}%{_datadir}/gnome/apps/Development/
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
* Thu Jan 08 2004 Dag Wieers <dag@wieers.com> - 0.9.4-0
- Initial package. (using DAR)
