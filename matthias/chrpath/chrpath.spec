# Authority: dag

Summary: Change the dynamic library load path (rpath) of binaries.
Name: chrpath
Version: 0.11
Release: 0
License: GPL
Group: Development/Tools
URL: ftp://ftp.hungry.com/pub/hungry/chrpath/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: ftp://ftp.hungry.com/pub/hungry/chrpath/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

%description
Chrpath allows you to modify the dynamic library load path (rpath) of
compiled programs.  Currently, only removing and modifying the rpath
is supported.  Eventually, I hope to be able to add an rpath if it is
missing.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall 

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_prefix}/doc/

%clean
%{__rm} -rf %{buildroot}

%files 
%defattr (-, root, root,0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%doc %{_mandir}/man?/*
%{_bindir}/*

%changelog
* Tue Sep 16 2003 Dag Wieers <dag@wieers.com> - 0.11-0
- Updated to release 0.11.

* Tue Aug 19 2003 Dag Wieers <dag@wieers.com> - 0.10-0
- Initial package. (using DAR)
