# Authority: dag

# Upstream: Hubert Feyrer <hubert@feyrer.de>

Summary: Harddisk image cloning tool.
Name: g4u
Version: 1.12
Release: 0
License: GPL
Group: Applications/System
URL: http://www.feyrer.de/g4u/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.feyrer.de/g4u/%{name}-%{version}.tgz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

#BuildRequires: 

%description
g4u ("ghost for unix") is a NetBSD-based bootfloppy/CD-ROM that allows
easy cloning of PC harddisks to deploy a common setup on a number of
PCs using FTP. The floppy/CD offers two functions. First is to upload
the compressed image of a local harddisk to a FTP server. Other is to
restore that image via FTP, uncompress it and write it back to disk;
network configuration is fetched via DHCP. As the harddisk is
processed as a image, any filesystem and operating system can be
deployed using g4u. Easy cloning of local disks as well as partitions
is also supported.

%prep
%setup -c

%build
%{__make} %{?_smp_mflags} all

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_libdir}/*
%{_datadir}/pixmaps/*
%{_datadir}/applications/*.desktop

%changelog
* Thu Oct 02 2003 Dag Wieers <dag@wieers.com> - 1.12-0
- Initial package. (using DAR)
