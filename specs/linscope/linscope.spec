# $Id$
# Authority: dries

Summary: Network scanner for network shares
Name: linscope
Version: 0.3.2
Release: 1.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://sourceforge.net/projects/linscope/

Source: http://dl.sf.net/linscope/linscope-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: qt-devel, desktop-file-utils, gcc-c++
Requires: /usr/bin/rpcclient

%description
LinScope is GUI, port scanner with enumerating windows network shares (SMB).
LinScope can save favorites list. You can add different ip address ranges
and scan them apart or together. Linscope searches FTP and HTTP services too.
It works in large networks and internet, where broadcast traffic is disabled
(uses direct ip address and rpcclient from samba). User could manually assign
command s for opening shares, apart for ftp,http and smb.

%prep
%setup -n Linscope

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=linscope
Comment=Find network shares
Exec=linscope
Terminal=false
Type=Application
StartupNotify=true
Categories=Application;Internet;Network;
Encoding=UTF-8
EOF

%build
cd linscope
qmake
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -D linscope/lrpcscanip %{buildroot}%{_bindir}/lrpcscanip
%{__install} linscope/linscope %{buildroot}%{_bindir}/linscope

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor rpmforge             \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	%{name}.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES.TXT README.TXT TODO.TXT
%{_bindir}/linscope
%{_bindir}/lrpcscanip
%{_datadir}/applications/*linscope.desktop

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.3.2-1.2
- Rebuild for Fedora Core 5.

* Sat Jan 14 2006 Dries Verachtert <dries@ulyssis.org> - 0.3.2-1
- Updated to release 0.3.2.

* Fri Dec 02 2005 Dries Verachtert <dries@ulyssis.org> - 0.2.0-1
- Initial package.
