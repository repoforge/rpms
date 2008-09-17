# $Id$
# Authority: dag

%{?dtag: %{expand: %%define %dtag 1}}

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}

%define desktop_vendor rpmforge

%define real_name TrueCrypt

Summary: Free open-source disk encryption software
Name: truecrypt
Version: 6.0a
Release: 1
License: TrueCrypt License 2.0
Group: Applications/System
URL: http://www.truecrypt.org/

#Source: http://www.truecrypt.org/downloads/transient/d21a47cbd3/TrueCrypt%206.0a%20Source.tar.gz
Source0: truecrypt-%{version}-source.tar.gz
Source1: truecrypt.png
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: fuse-devel
BuildRequires: wxGTK-devel >= 2.8

%description
Manages encrypted TrueCrypt volumes, which can be mapped as virtual block
devices and used as any other standard block device. All data being read
from a mapped TrueCrypt volume is transparently decrypted and all data
being written to it is transparently encrypted. 

%prep
%setup -n %{name}-%{version}-source

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
%{__make} \
    WX_BUILD_DIR="%{_bindir}" \
    NO_WARNINGS="1" \
    VERBOSE="1"

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 Main/truecrypt %{buildroot}%{_bindir}/truecrypt
%{__install} -Dp -m0644 %{SOURCE1} %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/truecrypt.png

%if %{?_without_freedesktop:1}0
    %{__install} -D -m0644 truecrypt.desktop %{buildroot}/etc/X11/applnk/Utilities/truecrypt.desktop
%else
    %{__mkdir_p} %{buildroot}%{_datadir}/applications/
    desktop-file-install --vendor %{desktop_vendor} \
        --dir %{buildroot}%{_datadir}/applications  \
        truecrypt.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc License.txt Readme.txt Release/Setup\ Files/TrueCrypt\ User\ Guide.pdf
#%doc %{_mandir}/man1/truecrypt.1*
%{_bindir}/truecrypt
%{_datadir}/applications/%{desktop_vendor}-truecrypt.desktop
%{_datadir}/icons/hicolor/48x48/apps/truecrypt.png

%changelog
* Mon Sep 15 2008 Dag Wieers <dag@wieers.com> - 6.0a-1
- Initial package. (using DAR)
