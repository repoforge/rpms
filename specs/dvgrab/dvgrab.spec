# $Id$

# Authority: dag
# Upstream: Dan Dennedy

Summary: DV grabber through the FireWire interface.
Name: dvgrab
Version: 1.5
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://kino.schirmacher.de/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://kino.schirmacher.de/filemanager/download/20/dvgrab-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libraw1394-devel, libavc1394-devel
Requires: kernel >= 2.4.0

%description
Dvgrab is a command line driven soft that grab AVI-2 films from a DV camera
using the IEEE-1394 bus (aka FireWire).
DV stand for Digital Video and is the name of the new numeric camera
generation.

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
%doc AUTHORS ChangeLog COPYING README TODO
%doc %{_mandir}/man?/*
%{_bindir}/*

%changelog
* Tue Mar 23 2004 Dag Wieers <dag@wieers.com> - 1.5-1
- Updated to release 1.5.

* Wed Dec 17 2003 Dag Wieers <dag@wieers.com> - 1.4-0
- Initial package. (using DAR)
