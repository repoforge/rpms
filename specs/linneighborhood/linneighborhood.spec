# $Id$
# Authority: dag
# Upstream: Hans Schmid <schmidjo@bnro.de>

%{?dist: %{expand: %%define %dist 1}}

%define dfi %(which desktop-file-install &>/dev/null; echo $?)

%define real_name LinNeighborhood

Summary: SMB network neighborhood
Name: linneighborhood
Version: 0.6.5
Release: 2
License: GPL
Group: Applications/Communications
URL: http://www.bnro.de/~schmidjo/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.bnro.de/~schmidjo/download/LinNeighborhood-%{version}.tar.gz
Patch0: linneighborhood-0.6.5-samba3.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


Obsoletes: %{real_name} <= 0.6.5
Requires: gtk+ >= 1.2.0, gettext

%description
This application is a GUI similar to the Win9x/NT network neighborhood.
It makes you able to browse entire networks and mount shares. The Samba
client (http://www.samba.org) is required (for smbmount/smbumount/smbmnt),
or Samba without smbmount/smbumount/smbmnt but with smbfs installed.

%prep
%setup -n %{real_name}-%{version}
%{?fc1:%patch0 -p1}
%{?el3:%patch0 -p1}

%{__cat} <<EOF >%{real_name}.desktop
[Desktop Entry]
Name=Linneighborhood SMB Browser
Comment=Browse Samba and Windows shares
Icon=LinNeighborhood.xpm
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

%{__install} -d -m0755 %{buildroot}%{_datadir}/pixmaps/
%{__install} -m0644 LinNeighborhood.xpm %{buildroot}%{_datadir}/pixmaps/

%{__ln_s} -f %{real_name} %{buildroot}%{_bindir}/%{name}

%if %{dfi}
	%{__install} -d -m0755 %{buildroot}%{_datadir}/gnome/apps/Internet/
	%{__install} -m0644 %{real_name}.desktop %{buildroot}%{_datadir}/gnome/apps/Internet/
%else
	desktop-file-install --vendor gnome                \
		--add-category X-Red-Hat-Base              \
		--dir %{buildroot}%{_datadir}/applications \
		%{real_name}.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files -f %{real_name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS ChangeLog CONFIGURATION COPYING NEWS README TODO THANKS
%{_bindir}/*
%{_datadir}/icons/*
%{_datadir}/pixmaps/*
%if %{dfi}
	%{_datadir}/gnome/apps/Internet/*.desktop
%else
        %{_datadir}/applications/*.desktop
%endif

%changelog
* Sun Mar 07 2004 Dag Wieers <dag@wieers.com> - 0.6.5-2
- Patch for samba3 from Debian. (Ng Sheaufeng)

* Tue Feb 03 2004 Dag Wieers <dag@wieers.com> - 0.6.5-1
- Added proper desktop-file.

* Sun Aug 24 2003 Dag Wieers <dag@wieers.com> - 0.6.5-0
- Initial package. (using DAR)
