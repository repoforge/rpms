# $Id$
# Authority: dag

%{?dtag: %{expand: %%define %dtag 1}}

%define desktop_vendor rpmforge
%define real_name TrueCrypt

Summary: Free open-source disk encryption software
Name: truecrypt
Version: 6.2a
Release: 2
License: TrueCrypt License 2.7
Group: Applications/System
URL: http://www.truecrypt.org/

#http://www.truecrypt.org/download/transient/86ce1a8ea6/TrueCrypt%206.2%20Source.tar.gz
Source0: truecrypt-%{version}-source.tar.gz

# wget ftp://mirror.switch.ch/mirror/pkcs/pkcs-11/v2-20/*.h
Source1: pkcs-11-v2-20.tar.bz2

Source2: truecrypt.png

Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: fuse-devel wxGTK-devel >= 2.8

%description
Manages encrypted TrueCrypt volumes, which can be mapped as virtual block
devices and used as any other standard block device. All data being read
from a mapped TrueCrypt volume is transparently decrypted and all data
being written to it is transparently encrypted. 

%prep
%setup -n %{name}-%{version}-source
%setup -n %{name}-%{version}-source -T -D -a 1

### Remove --static from compilation options for WxGTK
%{__perl} -pi.orig -e 's| --static||' Main/Main.make

%{__cat} <<EOF >truecrypt.desktop
[Desktop Entry]
Name=Truecrypt
Exec=truecrypt
Icon=truecrypt.png
StartupNotify=true
Terminal=false
Type=Application
Encoding=UTF-8
Categories=System;Application;
EOF

%build
PKCS_DIR=`pwd` ; PKCS_DIR="$PKCS_DIR/pkcs-11-v2-20" ;

%{__make} \
    WX_BUILD_DIR="%{_bindir}" \
    NO_WARNINGS="1" \
    PKCS11_INC="$PKCS_DIR" \
    VERBOSE="1"

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 Main/truecrypt %{buildroot}%{_bindir}/truecrypt
%{__install} -Dp -m0644 %{SOURCE2} %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/truecrypt.png

%{__mkdir_p} %{buildroot}%{_datadir}/applications/

desktop-file-install --vendor %{desktop_vendor} \
        --dir %{buildroot}%{_datadir}/applications  \
        truecrypt.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc License.txt Readme.txt Release/Setup\ Files/TrueCrypt\ User\ Guide.pdf
%{_bindir}/truecrypt
%{_datadir}/applications/%{desktop_vendor}-truecrypt.desktop
%{_datadir}/icons/hicolor/48x48/apps/truecrypt.png

%changelog
* Sat Aug 29 2009 Yury V. Zaytsev <yury@shurup.com> - 6.2a-2
- Added sources to the VCS tree

* Sun Jul 26 2009 Yury V. Zaytsev <yury@shurup.com> - 6.2a-1
- Bumped to the new version and fixed missing PKCS includes

* Sun May 24 2009 Dag Wieers <dag@wieers.com> - 6.2-1
- Updated to release 6.2.

* Tue Dec 02 2008 Dag Wieers <dag@wieers.com> - 6.1a-1
- Updated to release

* Mon Nov 03 2008 Dag Wieers <dag@wieers.com> - 6.1-1
- Updated to release 6.1.

* Mon Sep 15 2008 Dag Wieers <dag@wieers.com> - 6.0a-1
- Initial package. (using DAR)

