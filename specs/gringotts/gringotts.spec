# $Id$

# Authority: dag

# Upstream: Germano Rizzo <mano@pluto.linux.it>

Summary: Gringotts, an electronic strongbox
Name: gringotts
Version: 1.2.8
Release: 0
License: GPL
Group: Applications/Productivity
URL: http://devel.pluto.linux.it/projects/Gringotts/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://devel.pluto.linux.it/projects/Gringotts/current/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildPrereq: gtk2-devel, popt, textutils, libgringotts-devel >= 1.1.1, pkgconfig
#Requires: gtk2, bash, popt, textutils, libgringotts >= 1.1.1

%description
Gringotts is a small but (hopely ;) useful utility that stores sensitive
data (passwords, credit card numbers, friends' addresses) in an organized,
optimized and most of all very secure form.
It uses libGringotts to provide a strong level of encryption, just aiming
to be as trustworthy as possible.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS ChangeLog FAQ NEWS README TODO
%attr(4755, -, -) %{_bindir}/*
%{_datadir}/pixmaps/gringotts.xpm
%{_datadir}/gnome/apps/Utilities/gringotts.desktop

%changelog
* Thu Oct 23 2003 Dag Wieers <dag@wieers.com> - 1.2.8-0
- Updated to release 1.2.8.

* Tue Apr 29 2003 Dag Wieers <dag@wieers.com> - 1.2.7-0
- Updated to release 1.2.7.

* Thu Apr 18 2003 Dag Wieers <dag@wieers.com> - 1.2.6-0
- Updated to release 1.2.6.

* Tue Jan 07 2003 Dag Wieers <dag@wieers.com> - 1.2.3-0
- Initial package. (using DAR)
