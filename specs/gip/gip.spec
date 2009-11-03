# $Id$
# Authority: dag
# Upstream: Samuel Abels <spam$debain,org>

%define desktop_vendor rpmforge

%define real_version 1.6.1-1

Summary: GUI for making IP address based calculations
Name: gip
Version: 1.6.1.1
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.debain.org/software/gip/

#Source: http://www.debain.org/dlcounter.php?id=83&file=gip-%{real_version}.tar.gz
#Source: gip-%{real_version}.tar.gz
Source: http://dl.debain.org/gip/gip-%{real_version}.tar.gz
#http://web222.mis02.de/releases/gip/gip-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gettext, gtkmm24-devel, which, gcc-c++, desktop-file-utils
BuildRequires: intltool, perl-XML-Parser, libsigc++20-devel

%description
Gip is a nice GNOME GUI for making IP address based calculations.
For example, it can display IP addresses in binary format. Also,
it is possible to calculate subnets.

%prep
%setup -n %{name}-%{real_version}

%{__perl} -pi.orig -e 's|(\$INST_PREFIX)/lib/(\$EXECUTABLE)|$1/share/$2|' build.sh

%{__cat} <<EOF >gip.desktop
[Desktop Entry]
Name=Gip IP Subnet Calculator
Comment=Calculate with IPs, subnets and netmasks
Icon=redhat-accessories.png
Exec=gip
Terminal=false
Type=Application
StartupNotify=true
Categories=GNOME;Application;Utility;
EOF

%build
./build.sh \
	--rebuild \
	--prefix "%{_prefix}"

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_prefix}
./build.sh \
	--install \
	--prefix "%{buildroot}%{_prefix}"
%find_lang %{name}

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor %{desktop_vendor}    \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	gip.desktop

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS CHANGELOG COPYING INSTALL README
%{_bindir}/gip
%{_datadir}/applications/%{desktop_vendor}-gip*.desktop
%{_datadir}/gip/

%changelog
* Fri Jan 06 2006 Dries Verachtert <dries@ulyssis.org> - 1.6.0.1-1
- Updated to release 1.6.0-1

* Mon Jul 11 2005 Dag Wieers <dag@wieers.com> - 1.4.0.1-1
- Updated to release 1.4.0-1

* Sat Nov 20 2004 Dag Wieers <dag@wieers.com> - 1.2.1.1-1
- Updated to release 1.2.1-1

* Sun Jul 18 2004 Dag Wieers <dag@wieers.com> - 1.2.0.1-1
- Initial package. (using DAR)
