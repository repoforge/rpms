# $Id$
# Authority: dag
# Upstream: Shannon -jj Behrens <jjinux$yahoo,com>
# Upstream: <gcipher-development$lists,sf,net>

# Screenshot: http://gcipher.sourceforge.net/images/screenshot_sparse.png
# ScreenshotURL: http://gcipher.sourceforge.net/images/screenshot.png

Summary: Simple encryption tool
Name: gcipher
Version: 1.0
Release: 2.2%{?dist}
License: BSD
Group: Applications/System
URL: http://gcipher.sourceforge.net/

Source: http://dl.sf.net/gcipher/gcipher-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python >= 2.2, desktop-file-utils
Requires: python >= 2.2

%description
This is a simple encryption tool to work with home-grown encryption algorithms.
It can run as either a GUI, a command-line application, or a network proxy.

%prep
%setup

%{__perl} -pi.orig -e 's|^GLADEDIR = "."$|GLADEDIR = "%{_datadir}/gcipher/lib"|' src/Const.py
%{__perl} -pi.orig -e 's|^# sys.path.append.+$|sys.path.append("%{_datadir}/gcipher/lib")|' src/gcipher

%{__cat} <<EOF >gcipher.desktop
[Desktop Entry]
Name=GCipher Encryption Tool
Comment=Encrypt data and network traffic
Exec=gcipher
Icon=gnome-lockscreen.png
Terminal=false
Type=Application
StartupNotify=true
Categories=GNOME;Application;Utility;
EOF

%build
python %{_libdir}/python*/compileall.py src

%install
%{__rm} -rf %{buildroot}

%{__install} -Dp -m0644 gcipher.1 %{buildroot}%{_mandir}/man1/gcipher.1
%{__install} -Dp -m0755 src/gcipher %{buildroot}%{_bindir}/gcipher

%{__install} -d -m0755 %{buildroot}%{_datadir}/gcipher/lib/{cipher,ciphergui}/
%{__install} -p -m0644 src/*.{py,pyc,glade,gladep} %{buildroot}%{_datadir}/gcipher/lib/
%{__install} -p -m0644 src/cipher/*.{py,pyc} %{buildroot}%{_datadir}/gcipher/lib/cipher/
%{__install} -p -m0644 src/ciphergui/*.{py,pyc,glade,gladep} %{buildroot}%{_datadir}/gcipher/lib/ciphergui/

%{__install} -d -m0755 %{buildroot}%{_datadir}/gcipher/plugins/{cipher,ciphergui}/
%{__install} -p -m0644 plugins/cipher/*.py %{buildroot}%{_datadir}/gcipher/plugins/cipher/
%{__install} -p -m0644 plugins/ciphergui/*.py %{buildroot}%{_datadir}/gcipher/plugins/ciphergui/

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor %{desktop_vendor}    \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	gcipher.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CONTRIB LICENSE README
%doc %{_mandir}/man?/*
%{_bindir}/gcipher
%{_datadir}/applications/*gcipher.desktop
%{_datadir}/gcipher/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.0-2.2
- Rebuild for Fedora Core 5.

* Fri Jun 11 2004 Dag Wieers <dag@wieers.com> - 1.0-2
- Added improved desktop file.
- Changed BuildArch to noarch.

* Thu Jun 26 2003 Dag Wieers <dag@wieers.com> - 1.0-0
- Initial package. (using DAR)
