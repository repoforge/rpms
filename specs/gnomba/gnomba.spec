# $Id$
# Authority: dag
# Upstream: Chris Rogers <gandalf$darkcorner,net>

### Goes into a loop with x86_64 (Please investigate)
# ExcludeDist: el3a fc2a fc3 el4

%define dfi %(which desktop-file-install &>/dev/null; echo $?)

Summary: GNOME Samba Browser
Name: gnomba
Version: 0.6.2
Release: 1.2%{?dist}
License: GPL
Group: Applications/System
URL: http://gnomba.sourceforge.net/

Source: http://dl.sf.net/gnomba/gnomba-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gtk+-devel, readline-devel, gnome-libs-devel
BuildRequires: gettext, automake, autoconf, texinfo

%description
gnomba is a GUI network browser using the smb protocol.  It allows users
to browse workgroups, machines, and shares in a "Network Neighborhood."

%prep
%setup

%{__cat} <<EOF >gnomba.desktop
[Desktop Entry]
Name=SMB Network Browser
Comment=Browse your local network SMB servers
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
		%{buildroot}%{_datadir}/gnome/apps/Internet/gnomba.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 755)
%doc ChangeLog COPYING README
%{_bindir}/*
%{_mandir}/man?/*
%{_datadir}/pixmaps/*.png
%if %{dfi}
        %{_datadir}/gnome/apps/Internet/*.desktop
%else
        %{_datadir}/applications/*.desktop
%endif

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.6.2-1.2
- Rebuild for Fedora Core 5.

* Mon Dec 15 2003 Dag Wieers <dag@wieers.com> - 0.6.2-1
- Improved desktop file.

* Tue May 06 2003 Dag Wieers <dag@wieers.com> - 0.6.2-0
- Initial package. (using DAR)
