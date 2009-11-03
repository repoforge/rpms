# $Id$
# Authority: dag
# Upstream: Pádraig Brady <P$draigBrady,com>

%{?dtag: %{expand: %%define %dtag 1}}

%define desktop_vendor rpmforge

%define real_name FSlint

Summary: Utility to find and clean "lint" on a filesystem
Name: fslint
Version: 2.40
Release: 1%{?dist}
License: GPL
Group: System Environment/Base
URL: http://www.pixelbeat.org/fslint/

Source: http://www.pixelbeat.org/fslint/fslint-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python-devel >= 2.0, gettext >= 0.13, pygtk2-devel
BuildRequires: desktop-file-utils
Requires: python >= 2.0, pygtk2, pygtk2-libglade, textutils >= 2.0.21, gettext >= 0.11.1, cpio

%description
fslint is a toolkit to find all redundant disk usage (duplicate files
for e.g.). It includes a GUI as well as a command line interface.


%prep
%setup

%{__perl} -pi.orig -e '
        s|^liblocation=.*$|liblocation="%{_datadir}/fslint"|;
        s|^locale_base=.*$|locale_base=None #RPM edit|;
    ' fslint-gui

#%{__cat} <<EOF >fslint.desktop
#[Desktop Entry]
#Name=Filesystem Lint
#Comment=Clean up your filesystems
#Exec=fslint
#Icon=fslint.png
#Terminal=false
#Type=Application
#Encoding=UTF-8
#Categories=GNOME;Application;Utility;System;
#EOF

%build

%install
%{__rm} -rf %{buildroot}

%{__install} -Dp -m0755 fslint-gui %{buildroot}%{_bindir}/fslint-gui
%{__ln_s} -f fslint-gui %{buildroot}%{_bindir}/fslint

%{__install} -Dp -m0644 fslint_icon.png %{buildroot}%{_datadir}/pixmaps/fslint_icon.png
%{__install} -Dp -m0644 fslint_icon.png %{buildroot}%{_datadir}/fslint/fslint_icon.png
%{__install} -Dp -m0644 fslint.glade %{buildroot}%{_datadir}/fslint/fslint.glade

%{__install} -d -m0755 %{buildroot}%{_datadir}/fslint/fslint/{fstool,supprt/rmlint}
%{__install} -p -m0755 fslint/{find*,fslint,zipdir} %{buildroot}%{_datadir}/fslint/fslint/
%{__install} -p -m0755 fslint/fstool/* %{buildroot}%{_datadir}/fslint/fslint/fstool/
%{__install} -p -m0644 fslint/supprt/fslver %{buildroot}%{_datadir}/fslint/fslint/supprt/
%{__install} -p -m0755 fslint/supprt/get* %{buildroot}%{_datadir}/fslint/fslint/supprt/
%{__install} -p -m0755 fslint/supprt/rmlint/* %{buildroot}%{_datadir}/fslint/fslint/supprt/rmlint/

%{__install} -Dp -m0644 man/fslint-gui.1 %{buildroot}%{_mandir}/man1/fslint-gui.1
%{__ln_s} -f fslint-gui.1 %{buildroot}%{_mandir}/man1/fslint.1

%{__make} install -C po DESTDIR="%{buildroot}"
%find_lang %{name}

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor %{desktop_vendor}    \
    --add-category X-Red-Hat-Base              \
    --dir %{buildroot}%{_datadir}/applications \
            fslint.desktop

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc doc/*
%doc %{_mandir}/man1/fslint*
%{_bindir}/fslint
%{_bindir}/fslint-gui
%{_datadir}/fslint/
%{_datadir}/pixmaps/fslint_icon.png
%{?_without_freedesktop:%{_datadir}/gnome/apps/Applications/fslint.desktop}
%{!?_without_freedesktop:%{_datadir}/applications/%{desktop_vendor}-fslint.desktop}

%changelog
* Tue Jul 21 2009 Dag Wieers <dag@wieers.com> - 2.40-1
- Updated to release 2.40.

* Sat Sep 22 2007 Dag Wieers <dag@wieers.com> - 2.24-1
- Updated to release 2.24.

* Thu Jun 28 2007 Dag Wieers <dag@wieers.com> - 2.22-1
- Updated to release 2.22.

* Sun Mar 18 2007 Dag Wieers <dag@wieers.com> - 2.20-1
- Updated to release 2.20.

* Tue Dec 26 2006 Dag Wieers <dag@wieers.com> - 2.18-1
- Updated to release 2.18.

* Mon Sep 05 2005 Dries Verachtert <dries@ulyssis.org> - 2.12-1
- Updated to release 2.12.

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
