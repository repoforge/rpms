# Authority: dag

Summary: A LiveJournal client for GNOME.
Name: drivel
Version: 0.9.1
Release: 0
License: GPL
Group: Applications/Internet
URL: http://www.sf.net/projects/drivel

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/home-made/apt/

Source: http://dl.sf.net/drivel/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

Requires: gtk2 >= 2.0.0, curl >= 7.10.0

%description
Drivel is an advanced LiveJournal client for the GNOME desktop.  While 
maintaining a full set of features, it had been designed with usability 
in mind, and presents an elegant user interface.

%prep
%setup

%build
%configure
%{__make}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING README TODO
%{_bindir}/*
%{_datadir}/pixmaps/*
%{_datadir}/applications/*

%changelog
* Tue May 06 2003 Dag Wieers <dag@wieers.com> - 0.9.1-0
- Initial package. (using DAR)
