# $Id$

# Authority: dries

Summary: KDE front-end to ssh
Name: kssh
Version: 0.7
Release: 2
License: GPL
Group: Applications/Internet
URL: http://kssh.sourceforge.net/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://dl.sf.net/kssh/kssh-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires: gettext, libart_lgpl-devel, libjpeg-devel, libpng-devel, arts-devel, zlib-devel, kdelibs-devel, gcc, make, gcc-c++, XFree86-devel, qt-devel
%{?fc2:BuildRequires:libselinux-devel}
Requires: kdelibs

# Screenshot: http://kssh.sourceforge.net/foto2.png
# ScreenshotURL: http://kssh.sourceforge.net/#screenshots

%description
Kssh is a KDE front-end to ssh. It can work as a standard KDE application 
that launches ssh connections in a terminal or as a konsole session. This 
means that you can press in any konsole "New Session" and then select 
"Secure Shell".

%prep
%{__rm} -rf "${RPM_BUILD_ROOT}"
%setup

%build
. /etc/profile.d/qt.sh
%configure
%{__make} %{?_smp_mflags}

%install
. /etc/profile.d/qt.sh
%makeinstall
rm -f %{buildroot}/usr/share/applnk/Internet/kssh.desktop
mkdir -p %{buildroot}/usr/share/applications
cat > %{buildroot}/usr/share/applications/kssh.desktop <<EOF
[Desktop Entry]
Name=Kssh
Icon=kssh.png
Comment=A Secure Shell front-end
Exec=kssh
Terminal=0
Type=Application
Encoding=UTF-8
Categories=Application;Network;X-Red-Hat-Base;
EOF

%files
%defattr(-,root,root, 0755)
%{_bindir}/kssh
%{_datadir}/applications/kssh.desktop
%{_datadir}/apps/konsole/kssh.desktop
%{_datadir}/doc/HTML/en/kssh
%{_datadir}/icons/*/*/apps/kssh.png

%changelog
* Sat Apr 24 2004 Dries Verachtert <dries@ulyssis.org> 0.7-2
- cleanup of spec file, rebuild

* Sat Jan 10 2004 Dries Verachtert <dries@ulyssis.org> 0.7-1
- first packaging for Fedora Core 1
