# $Id$
# Authority: dag
# Upstream: Joe Shaw <joe$assbarn,com>

# Tag: test

Summary: Open Carpet server generation tool
Name: open-carpet
Version: 0.3
Release: 1
License: GPL
Group: System Environment/Daemons
URL: http://open-carpet.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source:	http://open-carpet.org/tarballs/open-carpet-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python, python2-devel >= 2.2, pkgconfig >= 0.12
Requires: python2 >= 2.2, libredcarpet-python >= 2.0

Provides: ximian-open-carpet = %{version}-%{release}

%description
Open Carpet allows you to set up software repositories for making
software avaialble to users running the Red Carpet Daemon software
management tool (version 2.0 and newer). This module contains
scripts and sample configuration files for easily setting up Red
Carpet servers.

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
%doc AUTHORS COPYING ChangeLog NEWS README sample/
%{_bindir}/open-carpet
%{_datadir}/open-carpet/

%changelog
* Fri Aug 20 2004 Dag Wieers <dag@wieers.com> - 0.3-1
- Initial package. (using DAR)
