# $Id$
# Authority: dag
# Upstream: <dan$machlin,net>


%define desktop_vendor rpmforge

Summary: IP Subnet Calculator
Name: ipsc
Version: 0.4.3
Release: 2%{?dist}
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
%{__make} %{?_smp_mflags} -C ../prips CFLAGS="%{optflags}" clean prips.o
%{__make} %{?_smp_mflags} -C src CFLAGS="%{optflags}" clean all

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 src/ipsc %{buildroot}%{_bindir}/ipsc
%{__install} -Dp -m0755 src/gipsc %{buildroot}%{_bindir}/gipsc

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications
desktop-file-install --vendor %{desktop_vendor} \
    --add-category X-Red-Hat-Base               \
    --dir %{buildroot}%{_datadir}/applications  \
    ipsc.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog CONTRIBUTORS COPYING README TODO
%{_bindir}/gipsc
%{_bindir}/ipsc
%{_datadir}/applications/%{desktop_vendor}-ipsc.desktop

%changelog
* Tue Oct 06 2009 Dag Wieers <dag@wieers.com> - 0.4.3-2
- Rebuild for RHEL4 and RHEL4.

* Mon Aug 25 2003 Dag Wieers <dag@wieers.com> - 0.4.3-1
- Patch to build with gcc-3.3.

* Thu Apr 24 2003 Dag Wieers <dag@wieers.com> - 0.4.3-0
- Initial package. (using DAR)
