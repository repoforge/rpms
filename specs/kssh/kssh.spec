# $Id$

# Authority: dries

Summary: A KDE front-end to ssh.
Name: kssh
Version: 0.7
Release: 1
License: GPL
Group: Applications/Internet
URL: http://kssh.sourceforge.net/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://dl.sf.net/kssh/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{_name}-%{_version}
BuildRequires: gettext, libart_lgpl-devel, libjpeg-devel, libpng-devel, arts-devel, zlib-devel, kdelibs-devel, gcc, make, gcc-c++, XFree86-devel, qt-devel
Requires: kdelibs

#(d) primscreenshot: http://kssh.sourceforge.net/foto2.png

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
export DESTDIR=$RPM_BUILD_ROOT
sed -i "s/^DESTDIR =.*/DESTDIR=${RPM_BUILD_ROOT//\//\\/}\//g" $(find . -type f | egrep "Makefile$")
make install-strip
rm -f ${DESTDIR}/usr/share/applnk/Internet/kssh.desktop
mkdir -p ${DESTDIR}/usr/share/applications
cat > ${DESTDIR}/usr/share/applications/kssh.desktop <<EOF
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
/usr/bin/kssh
/usr/share/applications/kssh.desktop
/usr/share/apps/konsole/kssh.desktop
/usr/share/doc/HTML/en/kssh
/usr/share/icons/*/*/apps/kssh.png

%changelog
* Sat Jan 10 2004 Dries Verachtert <dries@ulyssis.org> 0.7-1
- first packaging for Fedora Core 1
