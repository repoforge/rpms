# Authority: dag

Summary: A GNOME UNO card game.
Name: gnono
Version: 0.0.3
Release: 0
License: GPL
Group: Amusements/Games
URL: http://www.paw.co.za/projects/gnono/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: ftp://ftp.paw.co.za/pub/PAW/sources/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

%description
An interesting card game for GNOME

%prep
%setup

%build
%configure --without-debug
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_prefix}/doc/

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_bindir}/*
%{_datadir}/gnome/apps/Games/gnono.desktop
%{_datadir}/pixmaps/gnono/

%changelog
* Fri Jan 07 2003 Dag Wieers <dag@wieers.com> - 0.0.3
- Initial package. (using DAR)
