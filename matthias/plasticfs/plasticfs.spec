# Authority: dag

Summary: The Plastic File System.
Name: plasticfs
Version: 1.7
Release: 0
License: GPL
Group: Development/Tools
URL: http://plasticfs.sourceforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://plasticfs.sourceforge.net/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: groff

%description
The Plastic File System is an LD_PRELOAD module for manipulating what the
file system looks like for programs.  This allows virtual file systems
to exist in user space, without kernel hacks or modules.

%prep
%setup
%configure

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE MANIFEST README
%doc %{_mandir}/man?/*
%{_libdir}/*


%changelog
* Fri Mar 14 2003 Dag Wieers <dag@wieers.com> - 1.7-0
- Initial package. (using DAR)
