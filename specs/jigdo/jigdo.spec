# $Id$

# Authority: dries
# Upstream: 

Summary: Tool for distributing large files
Name: jigdo
Version: 0.7.1
Release: 1
License: GPL
Group: Applications/Internet
URL: http://atterer.net/jigdo/

Source: http://atterer.net/jigdo/jigdo-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: w3c-libwww-devel, gtk2-devel, pkgconfig, db4-devel 
BuildRequires: gcc-c++, openssl-devel, desktop-file-utils, wget
Requires: wget

%description
Jigsaw Download, or short jigdo, is a tool designed to ease the distribution
of very large files over the internet, for example CD or DVD images. Its aim
is to make downloading the images as easy for users as a click on a direct
download link in a browser, while avoiding all the problems that server
administrators have with hosting such large files.

%prep
%setup

%{__cat} <<EOF >%{name}.desktop
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
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{_datadir}/jigdo/COPYING 
%find_lang %{name}

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor rpmforge             \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	%{name}.desktop

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc changelog COPYING README THANKS
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_datadir}/jigdo
%{_datadir}/applications/*.desktop

%changelog
* Mon Dec 13 2004 Dries Verachtert <dries@ulyssis.org> - 0.7.1-1
- Initial package.
