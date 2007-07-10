# $Id$
# Authority: dag

%define real_name fuseiso
%define real_version 20070708

Summary: FUSE module to mount ISO filesystem images
Name: fuse-iso
Version: 0.0.20070708
Release: 1
License: GPL
Group: Applications/Archiving
URL: http://fuse.sourceforge.net/wiki/index.php/FuseIso

Source: http://ubiz.ru/dm/fuseiso-%{real_version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#BuildRequires: fuse-devel, zlib-devel, glib2-devel >= 2.6
BuildRequires: fuse-devel, zlib-devel, glib2-devel
Requires: fuse

%description
Allow normal users to mount iso images with fuse. 
Supported image types are .iso, .img, .bin, .mdf and .nrg.

%prep
%setup -n %{real_name}-%{real_version}

%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_bindir}/fuseiso

%changelog
* Tue Jul 10 2007 Dag Wieers <dag@wieers.com> - 0.0.20061017-1
- Initial package. (using DAR)
