# $Id$
# Authority: dag

### FIXME: Include the java plugin
### FIXME: Check initscripts
### FIXME: Install desktop-file

Summary: Belgium electronic identity card
%define real_name Belgian_Identity_Card_Run-time
Name: eid-belgium
Version: 2.5.9
Release: 1
License: GPL
Group: Applications/Internet
URL: http://eid.belgium.be/

### Since it needs a specific referer, download it from http://www.belgium.be/zip/eid_datacapture_nl.html
Source: http://www.belgium.be/zip/Belgian_Identity_Card_Run-time%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#Buildarch: noarch
BuildRequires: scons, wxGTK-devel >= 2.4, openssl-devel >= 0.9.7, pcsc-lite-devel >= 1.2.9
BuildRequires: qt-devel >= 3.3.3
#BuildRequires: j2re
Provides: belpic = %{version}-%{release}
Obsoletes: belpic <= %{version}-%{release}
Provides: beid = %{version}-%{release}
Obsoletes: beid <= %{version}-%{release}

%description
The application for using the Belgian electronic identity card.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n beid-%{version}

%{__cat} <<EOF >eid-belgium.desktop
[Desktop Entry]
Name=Name Thingy Tool
Comment=Do things with things
Icon=name.png
Exec=name
Terminal=false
Type=Application
StartupNotify=true
Categories=GNOME;Application;AudioVideo;
EOF

### Fixing the references to /usr/local/etc in some files
%{__perl} -pi.orig -e 's|/usr/local/etc\b|%{buildroot}%{_sysconfdir}|g' SConstruct
%{__perl} -pi.orig -e 's|/usr/local/lib\b|%{buildroot}%{_libdir}|g' src/newpkcs11/SConscript
%{__perl} -pi.orig -e 's|/etc/init.d\b|%{buildroot}%{_initrddir}|g' src/beidservicecrl/SConscript "src/Belpic PCSC Service/SConscript"

%{__perl} -pi.orig -e 's|/usr/local/etc\b|%{_sysconfdir}|g' src/beidcommon/config.cpp src/newpkcs11/config.h
%{__perl} -pi.orig -e 's|/usr/local/lib\b|%{_libdir}|g' src/newpkcs11/etc/Belgian_eID_PKCS11_java.cfg
%{__perl} -pi.orig -e 's|/usr/local/bin\b|%{_bindir}|g' src/beidservicecrl/belgium.be-beidcrld "src/Belpic PCSC Service/belgium.be-beidpcscd"
%{__perl} -pi.orig -e 's|/usr/local/share\b|%{_datadir}|g' src/eidviewer/beidgui.conf

%build
source "/etc/profile.d/qt.sh"
scons configure prefix="%{_prefix}"
scons prefix="%{_prefix}"

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir}
source "/etc/profile.d/qt.sh"
scons install prefix="%{buildroot}%{_prefix}" libdir="%{buildroot}%{_libdir}"

#%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
#desktop-file-install --vendor net                  \
#	--add-category X-Red-Hat-Base              \
#	--dir %{buildroot}%{_datadir}/applications \
#	%{name}.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES INSTALL README VERSION doc/*.rtf doc/*.doc
%doc %{_mandir}/man1/*.1*
%config(noreplace) %{_sysconfdir}/beidbase.conf
%config(noreplace) %{_sysconfdir}/beidgui.conf
%config %{_initrddir}/belgium.be-beidcrld
%config %{_initrddir}/belgium.be-beidpcscd
%{_bindir}/beid-pkcs11-tool
%{_bindir}/beid-tool
%{_bindir}/beidcrld
%{_bindir}/beidpcscd
%{_bindir}/beidgui
%{_datadir}/beid/
%{_datadir}/locale/beidgui_de.mo
%{_datadir}/locale/beidgui_fr.mo
%{_datadir}/locale/beidgui_nl.mo
%{_includedir}/beid/
%{_libdir}/*.so
%{_libdir}/*.so.*
%{_libdir}/pkcs11/

%changelog
* Fri Feb 09 2007 Dag Wieers <dag@wieers.com> - 2.5.9-1
- Initial package. (using DAR)
