# $Id: $

# Authority: dries
# Upstream: 

Summary: Responds to or drops ICMP echo requests packets
Name: echoart
Version: 0.1
Release: 1
License: GPL
Group: Applications/Internet
URL: http://mirror1.internap.com/echoart/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://mirror1.internap.com/echoart/echoart.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: 

%description
Echoart responds to or drops ICMP echo request packets based on a
pre-defined sequence, and could be used to return crude ASCII art in
response to pings from a Cisco router. It works by intercepting ICMP echo
request packets and consulting a pattern template to determine whether or
not to respond to a specific echo request. It then uses libnet to inject
responses back into the network as necessary. 

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=Name Thingy Tool
Comment=Do things with things
Icon=name.png
Exec=name
Terminal=false
Type=Application
StartupNotify=true
Encoding=UTF-8
Categories=Application;Network;X-Red-Hat-Extra;
EOF

%build
%configure \
	--disable-schemas-install
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL="1"
%makeinstall
%find_lang %{name}

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor net                  \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	%{name}.desktop

%post
/sbin/ldconfig 2>/dev/null
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas &>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING CREDITS INSTALL LICENSE NEWS README THANKS TODO
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_libdir}/*.so.*
%{_datadir}/pixmaps/*.png
%{_datadir}/applications/*.desktop

%files devel
%{_includedir}/*.h
%{_libdir}/*.a
%{_libdir}/*.so
%exclude %{_libdir}/*.la

%changelog
* Son May 19 2004 Dries Verachtert <dries@ulyssis.org> - 
- Initial package.

