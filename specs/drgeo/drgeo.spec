# $Id$

# Authority: dag
# Upstream: Hilaire Fernandes <hilaire@ext.cri74.org>

### FIXME: configure has problems finding flex output using soapbox on RHEL3
# Soapbox: 0

Summary: Interactive educational geometry software.
Name: drgeo
Version: 0.9.12
Release: 0
License: GPL
Group: Applications/Engineering
URL: http://www.ofset.org/drgeo/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.ofset.org/%{name}/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: flex, bison, gmp-devel >= 2.0.2, glib-devel, gtk+-devel
BuildRequires: guile-devel, gnome-libs-devel, gob >= 1.0.10, libxml-devel

Obsoletes: drgenius

%description
Dr. Geo is a interactive geometry GUI application. It allows one to create
geometric figure plus the interactive manipulation of such figure in
respect with their geometric constraints. It is useable in teaching
situation with students from primary or secondary level.

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
%doc AUTHORS ChangeLog COPYING NEWS README TODO
#%doc %{_datadir}/gnome/help/*
%{_bindir}/*
%{_datadir}/drgeo/
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*
%{_datadir}/texmacs/TeXmacs/plugins/drgeo/

%changelog
* Sun Jan 31 2004 Dag Wieers <dag@wieers.com> - 0.9.12-0
- Updated to release 0.9.12.

* Fri Oct 24 2003 Dag Wieers <dag@wieers.com> - 0.9.10-0
- Updated to release 0.9.10.

* Tue Sep 23 2003 Dag Wieers <dag@wieers.com> - 0.9.9-0
- Updated to release 0.9.9.

* Sun Sep 07 2003 Dag Wieers <dag@wieers.com> - 0.9.8-0
- Updated to release 0.9.8.

* Wed Aug 13 2003 Dag Wieers <dag@wieers.com> - 0.9.7-0
- Package renamed to drgeo.
- Updated to release 0.9.7.

* Sun Mar 16 2003 Dag Wieers <dag@wieers.com> - 0.8.4-0
- Updated to release 0.8.4.

* Mon Feb 24 2003 Dag Wieers <dag@wieers.com> - 0.8.3-0
- Updated to release 0.8.3.

* Tue Jan 07 2003 Dag Wieers <dag@wieers.com> - 0.7.2-0
- Initial package. (using DAR)
