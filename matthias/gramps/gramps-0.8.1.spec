# Authority: dag

Summary: Genealogical Research and Analysis Management Programming System.
Name: gramps
Version: 0.8.1
Release: 0
License: GPL
Group: Applications/Editors
URL: http://gramps.sourceforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://download.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: autoconf >= 2.52, automake >= 1.6, scrollkeeper >= 0.1.4
BuildRequires: pygtk2-libglade

Requires(post): scrollkeeper

Requires: python >= 1.5.2

%description
gramps (Genealogical Research and Analysis Management Programming
System) is a GNOME based genealogy program supporting a Python
based plugin system.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall GNOME_DATADIR="%{buildroot}%{_datadir}"
%find_lang %{name}

%post
scrollkeeper-update -q

%postun
scrollkeeper-update -q

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc COPYING README TODO
%doc %{_mandir}/man1/*
%doc %{_datadir}/gnome/help/gramps-manual/
%doc %{_datadir}/gnome/help/extending-gramps/
%{_bindir}/*
%{_datadir}/gramps/
%{_datadir}/gnome/apps/Applications/*.desktop
%{_datadir}/omf/gramps/
%{_datadir}/pixmaps/*
 
%changelog
* Sun Feb 16 2003 Dag Wieers <dag@wieers.com> - 0.8.1-0
- Initial package. (using DAR)
