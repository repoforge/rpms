# $Id$
# Authority: dag
# Upstream: <dan$machlin,net>

%{?dtag: %{expand: %%define %dtag 1}}

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}

%define desktop_vendor rpmforge

Summary: IP Subnet Calculator
Name: ipsc
Version: 0.4.3
Release: 1.2%{?dist}
License: GPL
Group: Applications/System
URL: http://ipsc.sourceforge.net/software.html

Source0: http://ipsc.sf.net/dist/ipsc/ipsc-%{version}-src.tar.gz
Source1: http://ipsc.sf.net/dist/prips/prips-0.9.4-src.tar.gz
Patch0: ipsc-0.4.3-gcc33.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%{!?_without_freedesktop:BuildRequires: desktop-file-utils}

%description
The IP Subnet Calculator is a tool that allows network administrators
to make calculations that will assist in subnetting a network.  It also
has a number of other useful functions.

%prep
%setup -n %{name} -b 1
%patch0

%{__cat} <<EOF >ipsc.desktop
[Desktop Entry]
Name=IP Subnet Calculator
Comment=Calculate with IPs, subnets and netmasks
Icon=gnome-util.png
Exec=gipsc
Terminal=false
Type=Application
Categories=GNOME;Application;Utility;
EOF

%build
%{__make} %{?_smp_mflags} -C src \
	CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 src/ipsc %{buildroot}%{_bindir}/ipsc
%{__install} -Dp -m0755 src/gipsc %{buildroot}%{_bindir}/gipsc

%if %{?_without_freedesktop:1}0
	%{__install} -Dp -m0644 ipsc.desktop %{buildroot}%{_datadir}/gnome/apps/Network/ipsc.desktop
%else
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications
	desktop-file-install --vendor %{desktop_vendor}    \
		--add-category X-Red-Hat-Base              \
		--dir %{buildroot}%{_datadir}/applications \
		ipsc.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog CONTRIBUTORS COPYING README TODO
%{_bindir}/*
%{!?_without_freedesktop:%{_datadir}/applications/gnome-ipsc.desktop}
%{?_without_freedesktop:%{_datadir}/gnome/apps/Network/ipsc.desktop}

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.4.3-1.2
- Rebuild for Fedora Core 5.

* Mon Aug 25 2003 Dag Wieers <dag@wieers.com> - 0.4.3-1
- Patch to build with gcc-3.3.

* Thu Apr 24 2003 Dag Wieers <dag@wieers.com> - 0.4.3-0
- Initial package. (using DAR)
