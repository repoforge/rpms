# $Id$
# DarAuthority: dag
# Upstream: Michael Kohn <mike@mikekohn.net>

%define dfi %(which desktop-file-install &>/dev/null; echo $?)

Summary: Converts WWW Active Server Pages to PHP pages
Name: asp2php
Version: 0.76.19
Release: 2
License: GPL
Group: Development/Tools
URL: http://asp2php.naken.cc/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.mikekohn.com/asp2php/asp2php-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk+-devel

%description
asp2php converts WWW Active Server Pages (ASP) files that run on the Microsoft
IIS Web Server into PHP pages to run on Apache.

%package gui
Summary: Graphical frontend for asp2php
Group: Development/Tools
Requires: %{name} = %{version}-%{release}
Obsoletes: asp2php-gtk <= %{version}

%description gui
Graphical frontend to asp2php.

%prep
%setup 

%{__cat} <<EOF >gtkasp2php.desktop
[Desktop Entry]
Name=ASP To PHP Converor
Comment=Converts ASP files to PHP
Icon=redhat-programming.png
Exec=gtkasp2php
Terminal=false
Type=Application
StartupNotify=true
Categories=GNOME;Application;Development;
EOF

%build
%{__make} default gui \
	CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m0755 asp2php %{buildroot}%{_bindir}/asp2php
%{__install} -D -m0755 gtkasp2php %{buildroot}%{_bindir}/gtkasp2php

%if %{dfi}
	%{__install} -D -m0644 gtkasp2php.desktop %{buildroot}%{_datadir}/gnome/apps/Development/gtkasp2php.desktop
%else
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --vendor gnome                \
		--add-category X-Red-Hat-Base              \
		--dir %{buildroot}%{_datadir}/applications \
		gtkasp2php.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE README TODO *.png sample/
%{_bindir}/asp2php

%files gui
%defattr(-, root, root, 0755)
%{_bindir}/gtkasp2php
%if %{dfi}
	%{_datadir}/gnome/apps/Development/*.desktop
%else
	%{_datadir}/applications/*.desktop
%endif

%changelog
* Sat Apr 11 2004 Dag Wieers <dag@wieers.com> - 0.76.19-2
- Obsoletes asp2php-gtk.

* Fri Apr 09 2004 Dag Wieers <dag@wieers.com> - 0.76.19-1
- Initial package. (using DAR)
