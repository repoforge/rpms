# $Id$
# Authority: dag
# Upstream: <dan@machlin.net>

%define dfi %(which desktop-file-install &>/dev/null; echo $?)

Summary: IP Subnet Calculator
Name: ipsc
Version: 0.4.3
Release: 1
License: GPL
Group: Applications/System
URL: http://ipsc.sf.net/software.html

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source0: http://ipsc.sf.net/dist/ipsc/ipsc-%{version}-src.tar.gz
Source1: http://ipsc.sf.net/dist/prips/prips-0.9.4-src.tar.gz
Patch0: ipsc-0.4.3-gcc33.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


%description
The IP Subnet Calculator is a tool that allows network administrators 
to make calculations that will assist in subnetting a network.  It also 
has a number of other useful functions.

%prep
%setup -n %{name} -b 1
%patch0

%{__cat} <<EOF >%{name}.desktop
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
%{__install} -D -m0755 src/ipsc %{buildroot}%{_bindir}/ipsc
%{__install} -D -m0755 src/gipsc %{buildroot}%{_bindir}/ipsc

%if %{dfi}
        %{__install} -d -m0755 %{buildroot}%{_datadir}/gnome/apps/Network/
        %{__install} -m0644 gnome-%{name}.desktop %{buildroot}%{_datadir}/gnome/apps/Network/
%else
        %{__install} -d -m0755 %{buildroot}%{_datadir}/applications
        desktop-file-install --vendor gnome                \
                --add-category X-Red-Hat-Base              \
                --dir %{buildroot}%{_datadir}/applications \
                %{name}.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog CONTRIBUTORS COPYING README TODO
%{_bindir}/*
%if %{dfi}
        %{_datadir}/gnome/apps/Network/*.desktop
%else
        %{_datadir}/applications/*.desktop
%endif

%changelog
* Mon Aug 25 2003 Dag Wieers <dag@wieers.com> - 0.4.3-1
- Patch to build with gcc-3.3. 

* Thu Apr 24 2003 Dag Wieers <dag@wieers.com> - 0.4.3-0
- Initial package. (using DAR)
