# $Id$
# Authority: dag
# Upstream: Pádraig Brady <P@draigBrady.com>

# ExclusiveDist: fc1 el3 rh9 rh8

%{?dist: %{expand: %%define %dist 1}}

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}

%define real_name FSlint

Summary: Utility to find and clean "lint" on a filesystem
Name: fslint
Version: 2.08
Release: 1
License: GPL
Group: System Environment/Base
URL: http://www.pixelbeat.org/fslint/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.iol.ie/~padraiga/fslint/FSlint-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: gettext, pygtk2-devel
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}
Requires: python >= 2.0, pygtk2, pygtk2-libglade, textutils >= 2.0.21, gettext >= 0.11.1, cpio

%description
FSlint is a utility to find and clean "lint" on a filesystem.
It is written in Python, using pyGtk and libGlade.

%prep
%setup -n %{real_name}-%{version}

%{__perl} -pi.orig -e 's|^liblocation=.*$|liblocation="%{_datadir}/fslint"|' FSlint

%{__cat} <<EOF >fslint.desktop
[Desktop Entry]
Name=Filesystem Lint
Comment=Clean up your filesystems
Exec=fslint
Icon=fslint.png
Terminal=false
Type=Application
Encoding=UTF-8
Categories=GNOME;Application;Utility;System;
EOF

%build

%install
%{__rm} -rf %{buildroot}

%{__install} -D -m0755 FSlint %{buildroot}%{_bindir}/fslint
%{__ln_s} -f fslint %{buildroot}%{_bindir}/FSlint

%{__install} -D -m0644 fslint_icon.png %{buildroot}%{_datadir}/pixmaps/fslint.png
%{__install} -D -m0644 fslint_icon.png %{buildroot}%{_datadir}/fslint/fslint_icon.png
%{__install} -D -m0644 fslint.glade %{buildroot}%{_datadir}/fslint/fslint.glade

%{__install} -d -m0755 %{buildroot}%{_datadir}/fslint/fslint/{fstool,rmlint}
%{__install} -m0755 fslint/{find*,fsl*,get*,zipdir} %{buildroot}%{_datadir}/fslint/fslint/
%{__install} -m0755 fslint/fstool/* %{buildroot}%{_datadir}/fslint/fslint/fstool/
%{__install} -m0755 fslint/rmlint/* %{buildroot}%{_datadir}/fslint/fslint/rmlint/

%makeinstall -C po \
	DATADIR="%{buildroot}%{_datadir}"
%find_lang %{name}

%if %{?_without_freedesktop:1}0
        %{__install} -D -m0644 fslint.desktop %{buildroot}%{_datadir}/gnome/apps/Applications/fslint.desktop
%else
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --vendor gnome                \
		--add-category X-Red-Hat-Base              \
		--dir %{buildroot}%{_datadir}/applications \
                fslint.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc doc/*
%{_bindir}/*
%{_datadir}/fslint/
%{_datadir}/pixmaps/*.png
%{!?_without_freedesktop:%{_datadir}/applications/gnome-fslint.desktop}
%{?_without_freedesktop:%{_datadir}/gnome/apps/Applications/fslint.desktop}

%changelog
* Thu Jun 17 2004 Dag Wieers <dag@wieers.com> - 2.08-1
- Updated to release 2.08.

* Sun Apr 25 2004 Dag Wieers <dag@wieers.com> - 2.06-2
- Reverted datadir location patch. (Erik Williamson)

* Sat Apr 24 2004 Dag Wieers <dag@wieers.com> - 2.06-1
- Updated to release 2.06.

* Sun Nov 23 2003 Dag Wieers <dag@wieers.com> - 2.04-0
- Updated to release 2.04.

* Wed Jul 30 2003 Dag Wieers <dag@wieers.com> - 2.02-0
- Updated to release 2.02.
- Initial package. (using DAR)
