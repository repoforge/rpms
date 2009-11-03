# $Id$
# Authority: dries

# Screenshot: http://kssh.sourceforge.net/foto2.png
# ScreenshotURL: http://kssh.sourceforge.net/#screenshots


Summary: KDE front-end to ssh
Name: kssh
Version: 0.7
Release: 3%{?dist}
License: GPL
Group: Applications/Internet
URL: http://kssh.sourceforge.net/

Source: http://dl.sf.net/kssh/kssh-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gettext, libart_lgpl-devel, libjpeg-devel, libpng-devel
BuildRequires: arts-devel, zlib-devel, kdelibs-devel, gcc, make, gcc-c++
BuildRequires: qt-devel, fam-devel
%{?el4:BuildRequires:libselinux-devel}
%{?fc3:BuildRequires:libselinux-devel}
%{?fc2:BuildRequires:libselinux-devel}

%description
Kssh is a KDE front-end to ssh. It can work as a standard KDE application
that launches ssh connections in a terminal or as a konsole session. This
means that you can press in any konsole "New Session" and then select
"Secure Shell".

%prep
%setup

%build
. /etc/profile.d/qt.sh
%configure LDFLAGS="$LDFLAGS -L/usr/X11R6/%{_lib}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
. /etc/profile.d/qt.sh
%makeinstall
# Install a nicer desktop entry
%{__rm} -f %{buildroot}%{_datadir}/applnk/Internet/kssh.desktop
%{__mkdir_p} %{buildroot}%{_datadir}/applications
%{__cat} > %{buildroot}%{_datadir}/applications/kssh.desktop << EOF
[Desktop Entry]
Name=Kssh
Comment=A Secure Shell front-end
Icon=kssh.png
Exec=kssh
Terminal=0
Type=Application
Categories=Application;Network;X-Red-Hat-Base;
Encoding=UTF-8
EOF

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_bindir}/kssh
%{_datadir}/applications/kssh.desktop
%{_datadir}/apps/konsole/kssh.desktop
%{_datadir}/doc/HTML/en/kssh
%{_datadir}/icons/*/*/apps/kssh.png

%changelog
* Thu Mar 30 2006 Dries Verachtert <dries@ulyssis.org> - 0.7-3
- Simplify buildequirements: kdelibs-devel already requires xorg-x11-devel/XFree86-devel

* Sat Apr 24 2004 Dries Verachtert <dries@ulyssis.org> 0.7-2
- cleanup of spec file, rebuild

* Sat Jan 10 2004 Dries Verachtert <dries@ulyssis.org> 0.7-1
- first packaging for Fedora Core 1

