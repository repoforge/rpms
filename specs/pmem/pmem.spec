# $Id$

# Authority: dries
# Upstream: 

Summary: Process Memory Information
Name: pmem
Version: 1.1
Release: 1
License: GPL
Group: Applications/System
URL: http://www.pmem.net/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://www.pmem.net/pmem-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
pmem is a small command line utility for all Linux und Unix operating
systems to display memory information of running processes. To do this, pmem
reads the memory information that are provided by the /proc file systems.
Therefore, pmem does not work on operating systems that do not maintain this
files system. 

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
%doc ChangeLog COPYING INSTALL NEWS README
%{_bindir}/*

%changelog
* Mon May 24 2004 Dries Verachtert <dries@ulyssis.org> 1.1-1
- Initial package.
