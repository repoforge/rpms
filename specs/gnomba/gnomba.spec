# $Id$

# Authority: dag

# Upstream: Chris Rogers <gandalf@darkcorner.net>

%define dfi %(which desktop-file-install &>/dev/null; echo $?)

Summary: GNOME Samba Browser.
Name: gnomba
Version: 0.6.2
Release: 1
License: GPL
Group: Applications/System
URL: http://gnomba.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/gnomba/gnomba-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


%description
gnomba is a GUI network browser using the smb protocol.  It allows users
to browse workgroups, machines, and shares in a "Network Neighborhood."

%prep
%setup

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=SMB Network Browser
Comment=Browse your local network servers.
Exec=gnomba
Icon=gnome-gnomba.png
Terminal=false
Type=Application
Categories=Gnome;Application;Network;
EOF

%build
%configure
%{__make} %{?_smp_mflags} \
	LIBDIR="%{_sysconfdir}"
     
%install
%{__rm} -rf %{buildroot}
%makeinstall \
	gnulocaledir="%{buildroot}%{_datadir}/locale"
%find_lang %{name}

%if %{dfi}
%else  
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --vendor gnome --delete-original \
		--add-category X-Red-Hat-Base                 \
		--dir %{buildroot}%{_datadir}/applications    \
		%{buildroot}%{_datadir}/gnome/apps/Internet/%{name}.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 755)
%doc ChangeLog COPYING README
%{_bindir}/*
%{_mandir}/man?/*
%{_datadir}/pixmaps/*
%if %{dfi}
        %{_datadir}/gnome/apps/Internet/*.desktop
%else   
        %{_datadir}/applications/*.desktop
%endif

%changelog
* Mon Dec 15 2003 Dag Wieers <dag@wieers.com> - 0.6.2-1
- Improved desktop file.

* Tue May 06 2003 Dag Wieers <dag@wieers.com> - 0.6.2-0
- Initial package. (using DAR)
