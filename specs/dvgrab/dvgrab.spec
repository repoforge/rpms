# Authority: dag

Summary: DV grabber through the FireWire interface.
Name: dvgrab
Version: 1.4
Release: 0
License: GPL
Group: Applications/Multimedia
URL: http://kino.schirmacher.de/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://kino.schirmacher.de/filemanager/download/15/%{name}-%{version}.tar.gz
Buildroot: %{_tmppath}/root-%{name}-%{name}
Prefix: %{_prefix}

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
* Wed Dec 17 2003 Dag Wieers <dag@wieers.com> - 1.4-0
- Initial package. (using DAR)
