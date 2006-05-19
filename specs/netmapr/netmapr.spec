# $Id$
# Authority: dries

Summary: Shows network diagrams
Name: netmapr
Version: 1.8
Release: 1
License: GPL
Group: Applications/Networking
URL: http://www.nethack.net/software/netmapr

Source: http://www.nethack.net/software/netmapr/downloads/netmapr-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: SDL-devel, SDL_ttf-devel

%description
netmapr is a simple SDL-based network diagram program that aims to be quick 
and easy to use without a huge list of library requirements. It supports 
NetViz-style "drilldown" into nested diagrams.

%prep
%setup
%{__perl} -pi -e 's|/usr/local|%{_prefix}|g;' *
%{__perl} -pi -e 's|-o root| |g;' Makefile*
%{__perl} -pi -e 's|install -C|install|g;' Makefile*

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=Netmapr
Comment=Shows network diagrams
Exec=netmapr
Terminal=false
Type=Application
StartupNotify=true
Categories=Application;AudioVideo;
EOF

%build
%{__mv} Makefile.linux Makefile
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__perl} -pi -e 's| /usr| %{buildroot}%{_prefix}|g;' Makefile
%makeinstall

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor rpmforge             \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	%{name}.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc *.txt doc/*
%{_bindir}/netmapr*
%{_datadir}/netmapr/
%{_datadir}/applications/*netmapr.desktop

%changelog
* Fri May 19 2006 Dries Verachtert <dries@ulyssis.org> - 1.8-1
- Updated to release 1.8.

* Mon Jan 09 2006 Dries Verachtert <dries@ulyssis.org> - 1.6-1
- Updated to release 1.6.

* Tue Nov 15 2005 Dries Verachtert <dries@ulyssis.org> - 1.4-1
- Initial package.
