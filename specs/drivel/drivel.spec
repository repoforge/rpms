# $Id$
# Authority: dag
# Upstream: Todd Kulesza <todd@dropline.net>

Summary: LiveJournal client for GNOME
Name: drivel
Version: 0.9.4
Release: 1
License: GPL
Group: Applications/Internet
URL: http://www.dropline.net/drivel/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/drivel/drivel-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: gtk2 >= 2.0.0, curl >= 7.10.0

%description
Drivel is an advanced LiveJournal client for the GNOME desktop.  While 
maintaining a full set of features, it had been designed with usability 
in mind, and presents an elegant user interface.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING README TODO
%config %{_sysconfdir}/gconf/schemas/*.schemas
%{_bindir}/*
%{_datadir}/pixmaps/*
%{_datadir}/applications/*

%changelog
* Thu Mar 25 2004 Dag Wieers <dag@wieers.com> - 0.9.4-1
- Updated to release 0.9.4.

* Tue May 06 2003 Dag Wieers <dag@wieers.com> - 0.9.1-0
- Initial package. (using DAR)
