# $Id$
# Authority: dag

%{?dtag: %{expand: %%define %dtag 1}}

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}

%define desktop_vendor rpmforge

Summary: 5250 terminal emulator for the AS/400 written in Java
Name: tn5250j
Version: 0.6.0
Release: 2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://tn5250j.sourceforge.net/

Source: http://dl.sf.net/sourceforge/tn5250j/tn5250j-%{version}-bin-full-nosubdir.zip
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: unzip
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}
Requires: tn5250, jre

%description
tn5250j is a 5250 terminal emulator for the AS/400 written in Java.
It has features like continued edit fields, gui windows, cursor
progression fields. There are 3 modes: basic mode, enhanced mode
and gui mode.

%prep
%setup -c -n %{name}

%{__cat} <<EOF >tn5250j
#!/bin/bash
cd %{_localstatedir}/lib/tn5250j/
java -jar ./tn5250j.jar
EOF

%{__cat} <<EOF >tn5250j.desktop
[Desktop Entry]
Encoding=UTF-8
Version=1.0
Type=Application
Terminal=false
Exec=%{_bindir}/tn5250j
Name=tn5250j
Comment=Telnet 5250 java emulator
Icon=%{_datadir}/icons/tn5250-48x48.png
Categories=Application;Utility;X-Red-Hat-Base;
EOF

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0775 tn5250j %{buildroot}%{_bindir}/tn5250j

%{__install} -d -m0755 %{buildroot}%{_localstatedir}/lib/tn5250j/
%{__install} -Dp -m0644 *.jar %{buildroot}/var/lib/tn5250j/

%if %{?_without_freedesktop:1}0
    %{__install} -D -m0644 tn5250j.desktop %{buildroot}/etc/X11/applnk/Utilities/tn5250j.desktop
%else
    %{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
    desktop-file-install --vendor %{desktop_vendor}  \
        --dir %{buildroot}%{_datadir}/applications/  \
        tn5250j.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%post
update-desktop-database %{_datadir}/applications &>/dev/null || :

%files
%defattr(-, root, root, 0755)
%doc COPYING *.html *.txt
%{_bindir}/tn5250j
%{!?_without_freedesktop:%{_datadir}/applications/%{desktop_vendor}-tn5250j.desktop}
%{?_without_freedesktop:/etc/X11/applnk/Utilities/tn5250j.desktop}
%{_localstatedir}/lib/tn5250j/

%changelog
* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 0.6.0-2
- Fixed group tag.

* Tue Sep 25 2007 Fabian Arrotin <fabian.arrotin@arrfab.net> - 0.6.0-1
- Initial release
