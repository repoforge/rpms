# $Id$
# Authority: dries
# Upstream: Alvaro J. Iradier Muro <airadier$users,sourceforge,net>

# Screenshot: http://amsn.sf.net/shots/contactlist.jpg
# ScreenshotURL: http://amsn.sf.net/shots.htm

# ExcludeDist: fc1

%{?dist: %{expand: %%define %dist 1}}

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}
%{?rh6:%define _without_freedesktop 1}

%define desktop_vendor rpmforge

%define tls_maj 1.4
%define tls_min 1
%define real_version 0_94

Summary: Full featured MSN Messenger clone
Name: amsn
Version: 0.94
Release: 1
License: GPL
Group: Applications/Internet
URL: http://amsn.sourceforge.net/

Packager: Dries Verachtert <skotty@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://dl.sf.net/amsn/amsn-%{real_version}.tar.gz
### FIXME: tls-plugin doesn't build because of missing tclPort.h in tcl-devel
#Source1: http://dl.sf.net/amsn/tls%{tls_maj}.%{tls_min}-src.tar.bz2
Source2: http://dl.sf.net/amsn/tls%{tls_maj}.%{tls_min}-linux-x86.tar.gz

# Makefile is completely different
#Patch: amsn-0.83-makefile.patch
Patch1: amsn-0.92-login.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

ExclusiveArch: i386 x86_64
BuildRequires: tcl >= 8.3, tk >= 8.3, openssl-devel
BuildRequires: imlib-devel, libpng-devel, libtiff-devel
%{!?dist:BuildRequires: tcl-devel >= 8.3, tk-devel >= 8.3}
%{?fc3:BuildRequires: tcl-devel >= 8.3, tk-devel >= 8.3}
%{?fc2:BuildRequires: tcl-devel >= 8.3, tk-devel >= 8.3}
%{?fc1:BuildRequires: tcl-devel >= 8.3, tk-devel >= 8.3}
%{?el3:BuildRequires: tcl-devel >= 8.3, tk-devel >= 8.3}
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}
Requires: tcl >= 8.3, tk >= 8.3

%description
amsn is a Tcl/Tk clone that implements the Microsoft Messenger (MSN) for
Unix, Windows, or Macintosh platforms. It supports file transfers,
groups, and many more features.

%prep
%setup -n amsn-%{real_version} -a 2
%patch1 -p0

%{__perl} -pi.orig -e 's|\$\(datadir\)|\$(datadir)/amsn|g' Makefile

%{__cat} <<EOF >amsn.desktop
[Desktop Entry]
Name=Amsn Instant Messenger
Comment=Chat and send files using MSN
Exec=amsn
Icon=amsn.png
Type=Application
Terminal=false
Encoding=UTF-8
StartupNotify=true
Categories=Application;Network;
EOF

%{__cat} <<'EOF2' >amsn.sh
#!/bin/bash

AMSNLANG="$(echo $LANG | tr '[A-Z]' '[a-z]')"
if [ ! -e "%{_datadir}/amsn/lang/lang$AMSNLANG" ]; then
	AMSNLANG="$(echo $LANG | cut -f1 -d_)"
fi
if [ ! -e "%{_datadir}/amsn/lang/lang$AMSNLANG" ]; then
	AMSNLANG="en"
fi

if [ ! -e "$HOME/.amsn/config.xml" ]; then
	mkdir -p "$HOME/.amsn/"
	cat <<EOF >"$HOME/.amsn/config.xml"
<?xml version="1.0"?>
<config>
   <entry>
      <attribute>language</attribute>
      <value>$AMSNLANG</value>
   </entry>
   <entry>
      <attribute>last_client_version</attribute>
      <value>%{version}</value>
   </entry>
</config>
EOF
fi

exec "%{_datadir}/amsn/amsn"
EOF2

%build
cd plugins/traydock
%configure
%{__make} %{?_smp_mflags}
#cd -
#
#cd tls%{tls_maj} 
#%configure \
#	--with-ssl-dir="%{_prefix}"
#%{__make} %{?_smp_mflags}
#%{__perl} -pi -e 's|\.\.||' pkgIndex.tcl

%install
%{__rm} -rf %{buildroot}
%makeinstall \
   	proot="%{buildroot}%{_prefix}" \
	gnomelinks="%{buildroot}%{_datadir}/applications/" \
	version="%{version}" \
	libdir="%{buildroot}%{_datadir}/amsn"

%{__install} -D -m0755 amsn.sh %{buildroot}%{_bindir}/amsn
%{__install} -D -m0644 skins/default/pixmaps/messenger.png %{buildroot}%{_datadir}/pixmaps/amsn.png

%{__install} -m0644 FAQ HELP README %{buildroot}%{_datadir}/amsn/

%{__install} -d -m0755 %{buildroot}%{_datadir}/amsn/plugins/tls%{tls_maj}/
%{__install} -m0755 tls%{tls_maj}/libtls%{tls_maj}.so tls%{tls_maj}/pkgIndex.tcl tls%{tls_maj}/tls.tcl %{buildroot}%{_datadir}/amsn/plugins/tls%{tls_maj}/

%if %{?_without_freedesktop:1}0
	%{__install} -D -m0644 amsn.desktop %{buildroot}%{_datadir}/gnome/apps/Internet/amsn.desktop
%else
%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --vendor %{desktop_vendor}    \
		--add-category X-Red-Hat-Base              \
		--dir %{buildroot}%{_datadir}/applications \
		amsn.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc FAQ GNUGPL HELP README TODO
%{_bindir}/amsn
%{_datadir}/amsn/
%{_datadir}/pixmaps/*.png
%{?_without_freedesktop:%{_datadir}/gnome/apps/Internet/amsn.desktop}
%{!?_without_freedesktop:%{_datadir}/applications/%{desktop_vendor}-amsn.desktop}

%changelog
* Sat Nov 06 2004 Dag Wieers <dag@wieers.com> - 0.94-1
- Updated to release 0.94.

* Sun Aug 29 2004 Dag Wieers <dag@wieers.com> - 0.93-1
- Updated to release 0.93.

* Mon May 31 2004 Dries Verachtert <dries@ulyssis.org> - 0.92-1
- update to version 0.92
- added Encoding tag to desktop file

* Sun May 30 2004 Dag Wieers <dag@wieers.com> - 0.91-1
- Updated to release 0.91.

* Sun Feb 22 2004 Dag Wieers <dag@wieers.com> - 0.90-0
- Updated to release 0.90.

* Sun Jan 11 2004 Dag Wieers <dag@wieers.com> - 0.83-1
- Added FAQ to %%{_datadir}.

* Sat Jan 03 2004 Dag Wieers <dag@wieers.com> - 0.83-0
- Initial package. (using DAR)
