# $Id$
# Authority: dag

### FIXME: Include the java plugin
### FIXME: Check initscripts

%define desktop_vendor rpmforge

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
Patch: eid-belgium-2.5.9-openscreader.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#Buildarch: noarch
BuildRequires: scons, wxGTK-devel >= 2.4, openssl-devel >= 0.9.7, pcsc-lite-devel >= 1.2.9
BuildRequires: qt-devel >= 3.3.3, java-sdk
#BuildRequires: java-sdk-1.4.2
Provides: belpic = %{version}-%{release}
Obsoletes: belpic <= %{version}-%{release}
Provides: beid = %{version}-%{release}
Obsoletes: beid <= %{version}-%{release}

%description
The application for using the Belgian electronic identity card.

%prep
%setup -n beid-%{version}

%patch -p0

### Fixing the references to /usr/local in some files
%{__perl} -pi.orig -e 's|/usr/local/etc\b|%{buildroot}%{_sysconfdir}|g' \
	SConstruct
%{__perl} -pi.orig -e 's|/usr/local/lib\b|%{buildroot}%{_libdir}|g' \
	src/newpkcs11/SConscript
%{__perl} -pi.orig -e 's|/etc/init.d\b|%{buildroot}%{_initrddir}|g' \
	src/beidservicecrl/SConscript \
	"src/Belpic PCSC Service/SConscript"

%{__perl} -pi.orig -e 's|/usr/local/etc\b|%{_sysconfdir}|g' \
	src/beidcommon/config.cpp \
	src/newpkcs11/config.h
%{__perl} -pi.orig -e 's|/usr/local/lib\b|%{_libdir}|g' \
	src/newpkcs11/etc/Belgian_eID_PKCS11_java.cfg \
	src/newpkcs11/etc/beid-pkcs11-register.html
%{__perl} -pi.orig -e 's|/usr/local/bin/beidgui.png\b|%{_datadir}/icons/beidgui.png|g' \
	src/eidviewer/beidgui.desktop
%{__perl} -pi.orig -e 's|/usr/local/bin\b|%{_bindir}|g' \
	src/beidservicecrl/belgium.be-beidcrld \
	"src/Belpic PCSC Service/belgium.be-beidpcscd" \
	src/eidviewer/beidgui.desktop
%{__perl} -pi.orig -e 's|/usr/local/share\b|%{_datadir}|g' \
	src/eidviewer/beidgui.conf

%build
export CCFLAGS="%{optflags}"
export JAVA_HOME="$(readlink /etc/alternatives/java_sdk)"
source "/etc/profile.d/qt.sh"
scons configure prefix="%{_prefix}"
scons prefix="%{_prefix}"

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir}
%{__install} -d -m0755 %{buildroot}%{_libdir}
export JAVA_HOME="$(readlink /etc/alternatives/java_sdk)"
source "/etc/profile.d/qt.sh"
scons install --cache-disable prefix="%{buildroot}%{_prefix}" libdir="%{buildroot}%{_libdir}"

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --delete-original             \
	--vendor %{desktop_vendor}                 \
	--add-category X-Red-Hat-Base              \
	--add-category Utility                     \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_bindir}/beidgui.desktop

%{__install} -d -m0755 %{buildroot}%{_datadir}/icons/
%{__mv} -vf %{buildroot}%{_bindir}/beidgui.png %{buildroot}%{_datadir}/icons/beidgui.png

### Fix library symlinks
for lib in $(ls %{buildroot}%{_libdir}/libbeid*.so.?.?.?); do
	%{__ln_s} -f $(basename $lib) ${lib//%\.?\.?}
done

### Fix locale files
for file in $(ls %{buildroot}%{_datadir}/locale/beidgui_*.mo); do
	lang="${file%.mo}"
	lang="${lang#%{buildroot}%{_datadir}/locale/beidgui_}"
	%{__mkdir} -p %{buildroot}%{_datadir}/locale/$lang/LC_MESSAGES/
	%{__mv} -f $file %{buildroot}%{_datadir}/locale/$lang/LC_MESSAGES/beidgui.mo
done
%find_lang beidgui

%post
/sbin/ldconfig
update-desktop-database %{_datadir}/applications &>/dev/null || :

%postun
/sbin/ldconfig
update-desktop-database %{_datadir}/applications &>/dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files -f beidgui.lang
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
%{_datadir}/applications/%{desktop_vendor}-beidgui.desktop
%{_datadir}/beid/
%exclude %{_datadir}/beid/eID-toolkit_licensingtermsconditions*.rtf
%exclude %{_datadir}/beid/DeveloperGuide.doc
%{_datadir}/icons/beidgui.png
%{_includedir}/beid/
%{_libdir}/*.so*
%{_libdir}/pkcs11/

%changelog
* Fri Feb 09 2007 Dag Wieers <dag@wieers.com> - 2.5.9-1
- Initial package. (using DAR)
