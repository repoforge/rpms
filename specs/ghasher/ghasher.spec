# $Id$
# Authority: dag
# Upstream: <NOS$Utel.no>

%define desktop_vendor rpmforge

Summary: Grapical MD5 hash tool
Name: ghasher
Version: 1.2.0
Release: 1.2%{?dist}
License: BSD
Group: Applications/File
URL: http://asgaard.homelinux.org/code/ghasher/

Source: http://asgaard.homelinux.org/code/ghasher/ghasher-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk2-devel >= 2.4, openssl-devel, desktop-file-utils, libglade2-devel

%description
ghasher is a tool to calculate MD5 sum (or md2, md4, sha1, sha, ripemd160,
dss1) hashes of a file.

%prep
%setup

%{__cat} <<EOF >ghasher.desktop
[Desktop Entry]
Name=Ghasher Hashing Utility
Comment=Calculate the MD5 sum of a file
Encoding=UTF-8
Exec=ghasher
Terminal=false
Type=Application
Icon=ghasher
StartupNotify=true
Categories=GNOME;Utility;
EOF

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 ghasher %{buildroot}%{_bindir}/ghasher
%{__install} -Dp -m0644 hash.xpm %{buildroot}%{_datadir}/pixmaps/ghasher.xpm

desktop-file-install --vendor %{desktop_vendor}    \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	ghasher.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS LICENSE NEWS README TODO
%{_bindir}/ghasher
%{_datadir}/applications/%{desktop_vendor}-ghasher.desktop
%{_datadir}/pixmaps/ghasher.xpm

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.2.0-1.2
- Rebuild for Fedora Core 5.

* Sat Mar 05 2005 Dag Wieers <dag@wieers.com> - 1.2.0-1
- Initial package. (using DAR)
