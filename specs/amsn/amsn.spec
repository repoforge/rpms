# $Id$

# Authority: dries
# Screenshot: http://amsn.sourceforge.net/shots/contactlist.jpg
# ScreenshotURL: http://amsn.sourceforge.net/shots.htm

%define dfi %(which desktop-file-install &>/dev/null; echo $?)
%define tls_maj 1.4
%define tls_min 1
%define rversion 0_90

Summary: Full featured MSN Messenger clone
Name: amsn
Version: 0.90
Release: 1
License: GPL
Group: Applications/Internet
URL: http://amsn.sf.net/

Packager: Dries Verachtert <skotty@ulyssis.org>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/amsn/amsn-%{rversion}.tar.gz
### FIXME: tls-plugin doesn't build because of missing tclPort.h in tcl-devel
#Source1: http://dl.sf.net/amsn/tls%{tls_maj}.%{tls_min}-src.tar.bz2
Source2: http://dl.sf.net/amsn/tls%{tls_maj}.%{tls_min}-linux-x86.tar.gz
Patch: amsn-0.83-makefile.patch
Patch1: amsn-0.83-login.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


ExclusiveArch: i386
%{?rhfc1:BuildRequires: tcl-devel >= 8.3, tk-devel >= 8.3}
%{?rhel3:BuildRequires: tcl-devel >= 8.3, tk-devel >= 8.3}
BuildRequires: tcl >= 8.3, tk >= 8.3, openssl-devel
BuildRequires: imlib-devel, libpng-devel

%description
amsn is a Tcl/Tk clone that implements the Microsoft Messenger (MSN) for
Unix, Windows, or Macintosh platforms. It supports file transfers,
groups, and many more features.

%prep
#setup -n msn -a 1
%setup -n msn -a 2
#%patch -p0
%patch1 -p0

%{__perl} -pi.orig -e 's|\$\(datadir\)|\$(datadir)/amsn|g' Makefile

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=Amsn Instant Messaging
Comment=A full featured MSN Messenger clone
Exec=amsn
Icon=amsn.png
Type=Application
Terminal=false
StartupNotify=true
Categories=Application;Network;
EOF

%{__cat} <<'EOF2' >%{name}.sh
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

%{__install} -d -m0755 %{buildroot}%{_bindir} \
			%{buildroot}%{_datadir}/pixmaps/
%{__install} -m0755 amsn.sh %{buildroot}%{_bindir}/amsn
%{__install} -m0644 FAQ HELP README %{buildroot}%{_datadir}/amsn/
%{__install} -m0644 skins/default/pixmaps/messenger.png %{buildroot}%{_datadir}/pixmaps/amsn.png

%{__install} -d -m0755 %{buildroot}%{_datadir}/amsn/plugins/tls%{tls_maj}/
%{__install} -m0755 tls%{tls_maj}/libtls%{tls_maj}.so tls%{tls_maj}/pkgIndex.tcl tls%{tls_maj}/tls.tcl %{buildroot}%{_datadir}/amsn/plugins/tls%{tls_maj}/

%if %{dfi}
        %{__install} -d -m0755 %{buildroot}%{_datadir}/gnome/apps/Internet/
        %{__install} -m0644 %{name}.desktop %{buildroot}%{_datadir}/gnome/apps/Internet/
%else   
        %{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
        desktop-file-install --vendor net                  \
                --add-category X-Red-Hat-Base              \
                --dir %{buildroot}%{_datadir}/applications \
                %{name}.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc FAQ GNUGPL HELP README TODO
%{_bindir}/*
%{_datadir}/amsn/
%{_datadir}/pixmaps/*.png
%if %{dfi}
        %{_datadir}/gnome/apps/Internet/*.desktop
%else
        %{_datadir}/applications/*.desktop
%endif

%changelog
* Sun Feb 22 2004 Dag Wieers <dag@wieers.com> - 0.90-0
- Updated to release 0.90.

* Sun Jan 11 2004 Dag Wieers <dag@wieers.com> - 0.83-1
- Added FAQ to %%{_datadir}.

* Sat Jan 03 2004 Dag Wieers <dag@wieers.com> - 0.83-0
- Initial package. (using DAR)
