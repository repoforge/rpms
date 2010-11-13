# $Id$
# Authority: dag
# Upstream: Michael Kohn <mike$mikekohn,net>

### EL2 ships with asp2php-0.75.17-1
# Tag: rft

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}
%{?rh6:%define _without_freedesktop 1}

Summary: Converts WWW Active Server Pages to PHP pages
Name: asp2php
Version: 0.76.23
Release: 1.2%{?dist}
License: GPL
Group: Development/Tools
URL: http://asp2php.naken.cc/

Source: http://downloads.mikekohn.net/asp2php/asp2php-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk+-devel
%{?!_without_freedesktop:BuildRequires: desktop-file-utils}

%description
asp2php converts WWW Active Server Pages (ASP) files that run on the Microsoft
IIS Web Server into PHP pages to run on Apache.

%package gtk
Summary: Graphical frontend for asp2php
Group: Development/Tools
Requires: %{name} = %{version}-%{release}
#Obsoletes: asp2php-gtk <= %{version}

%description gtk
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
%{__install} -Dp -m0755 asp2php %{buildroot}%{_bindir}/asp2php
%{__install} -Dp -m0755 gtkasp2php %{buildroot}%{_bindir}/gtkasp2php

%if %{?_without_freedesktop:1}0
	%{__install} -Dp -m0644 gtkasp2php.desktop %{buildroot}%{_datadir}/gnome/apps/Development/gtkasp2php.desktop
%else
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --vendor %{desktop_vendor}    \
		--add-category X-Red-Hat-Base              \
		--dir %{buildroot}%{_datadir}/applications \
		gtkasp2php.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc *.png CHANGES LICENSE README sample/
%{_bindir}/asp2php

%files gtk
%defattr(-, root, root, 0755)
%{_bindir}/gtkasp2php
%{?_without_freedesktop:%{_datadir}/gnome/apps/Development/gtkasp2php.desktop}
%{!?_without_freedesktop:%{_datadir}/applications/%{desktop_vendor}-gtkasp2php.desktop}

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.76.23-1.2
- Rebuild for Fedora Core 5.

* Sun Oct 10 2004 Dag Wieers <dag@wieers.com> - 0.76.23-1
- Updated to release 0.76.23.

* Fri Apr 09 2004 Dag Wieers <dag@wieers.com> - 0.76.19-1
- Initial package. (using DAR)
