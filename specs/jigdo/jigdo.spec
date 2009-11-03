# $Id$

# Authority: dries

%{?dtag: %{expand: %%define %dtag 1}}

%define desktop_vendor rpmforge

Summary: Tool for distributing large files
Name: jigdo
Version: 0.7.3
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://atterer.net/jigdo/

Source: http://atterer.net/jigdo/jigdo-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk2-devel, pkgconfig, db4-devel
BuildRequires: gcc-c++, openssl-devel, desktop-file-utils, wget
BuildRequires: curl-devel, bzip2-devel

Requires: wget
%{?fc4:BuildRequires: compat-gcc-32, compat-gcc-32-c++}

%description
Jigsaw Download, or short jigdo, is a tool designed to ease the distribution
of very large files over the internet, for example CD or DVD images. Its aim
is to make downloading the images as easy for users as a click on a direct
download link in a browser, while avoiding all the problems that server
administrators have with hosting such large files.

%prep
%setup

%{__cat} <<EOF >jigdo.desktop
[Desktop Entry]
Name=Jigdo
Comment=Download large files from jigdo enabled webservers.
Exec=jigdo
Terminal=false
Type=Application
StartupNotify=true
Encoding=UTF-8
Categories=Application;Network;X-Red-Hat-Extra;
EOF

%build
%{?fc4:export CC=gcc32}
%{?fc4:export CXX=g++32}
%{expand: %%define optflags -O2}
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{_datadir}/jigdo/COPYING
%find_lang %{name}

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor %{desktop_vendor}    \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	jigdo.desktop

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc changelog COPYING README THANKS doc/
%doc %{_mandir}/man1/jigdo.1*
%doc %{_mandir}/man1/jigdo-file.1*
%doc %{_mandir}/man1/jigdo-lite.1*
%doc %{_mandir}/man1/jigdo-mirror.1*
%{_bindir}/jigdo
%{_bindir}/jigdo-file
%{_bindir}/jigdo-lite
%{_bindir}/jigdo-mirror
%{_datadir}/jigdo/
%{_datadir}/applications/%{desktop_vendor}-jigdo.desktop

%changelog
* Wed Apr 18 2007 Ralph Angenendt <ra@br-online.de> 0.7.3-1
- Updated to release 0.7.3.

* Mon Dec 13 2004 Dries Verachtert <dries@ulyssis.org> - 0.7.1-1
- Initial package.
