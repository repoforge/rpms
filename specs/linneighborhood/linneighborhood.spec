# $Id$
# Authority: dag
# Upstream: Hans Schmid <schmidjo$bnro,de>

%{?dtag: %{expand: %%define %dtag 1}}

%{?rh9:%define _without_samba3 1}
%{?rh8:%define _without_samba3 1}
%{?rh7:%define _without_freedesktop 1}
%{?rh7:%define _without_samba3 1}
%{?el2:%define _without_freedesktop 1}
%{?el2:%define _without_samba3 1}
%{?rh6:%define _without_freedesktop 1}
%{?rh6:%define _without_samba3 1}

%define desktop_vendor rpmforge

%define real_name LinNeighborhood

Summary: SMB network neighborhood
Name: linneighborhood
Version: 0.6.5
Release: 3.2%{?dist}
License: GPL
Group: Applications/Communications
URL: http://www.bnro.de/~schmidjo/

Source: http://www.bnro.de/~schmidjo/download/LinNeighborhood-%{version}.tar.gz
Patch0: linneighborhood-0.6.5-samba3.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gtk+-devel
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}

Obsoletes: %{real_name} <= 0.6.5
Requires: gtk+ >= 1.2.0, gettext

%description
This application is a GUI similar to the Win9x/NT network neighborhood.
It makes you able to browse entire networks and mount shares. The Samba
client (http://www.samba.org) is required (for smbmount/smbumount/smbmnt),
or Samba without smbmount/smbumount/smbmnt but with smbfs installed.

%prep
%setup -n %{real_name}-%{version}
%{!?_without_samba3:%patch0 -p1}

%{__cat} <<EOF >linneighborhood.desktop
[Desktop Entry]
Name=Linneighborhood SMB Browser
Comment=Browse Samba and Windows shares
Icon=linneighborhood.xpm
Exec=linneighborhood
Terminal=false
Type=Application
Categories=Application;Network;
EOF

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{real_name}

%{__install} -Dp -m0644 LinNeighborhood.xpm %{buildroot}%{_datadir}/pixmaps/linneighborhood.xpm

%{__ln_s} -f LinNeighborhood %{buildroot}%{_bindir}/linneighborhood

%if %{?_without_freedesktop:1}0
	%{__install} -Dp -m0644 linneighborhood.desktop %{buildroot}%{_datadir}/gnome/apps/Internet/linneighborhood.desktop
%else
	desktop-file-install --vendor %{desktop_vendor}    \
		--add-category X-Red-Hat-Base              \
		--dir %{buildroot}%{_datadir}/applications \
		linneighborhood.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files -f %{real_name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS ChangeLog CONFIGURATION COPYING NEWS README THANKS TODO
%{_bindir}/linneighborhood
%{_bindir}/LinNeighborhood
%{_datadir}/icons/LinNeighborhood.xpm
%{_datadir}/pixmaps/linneighborhood.xpm
%{?_without_freedesktop:%{_datadir}/gnome/apps/Internet/linneighborhood.desktop}
%{!?_without_freedesktop:%{_datadir}/applications/%{desktop_vendor}-linneighborhood.desktop}

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.6.5-3.2
- Rebuild for Fedora Core 5.

* Sun Oct 10 2004 Dag Wieers <dag@wieers.com> - 0.6.5-3
- Rebuild with cosmetic changes.

* Sun Mar 07 2004 Dag Wieers <dag@wieers.com> - 0.6.5-2
- Patch for samba3 from Debian. (Ng Sheaufeng)

* Tue Feb 03 2004 Dag Wieers <dag@wieers.com> - 0.6.5-1
- Added proper desktop-file.

* Sun Aug 24 2003 Dag Wieers <dag@wieers.com> - 0.6.5-0
- Initial package. (using DAR)
