# $Id$

# Authority: dag

Summary: Trace a chain of DNS servers to the source
Name: dnstracer
Version: 1.7
Release: 1
License: GPL
Group: Applications/Internet
URL: http://www.mavetju.org/unix/general.php

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.mavetju.org/download/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


Obsoletes: dnstrace

%description
dnstrace determines where a given Domain Name Server (DNS) gets its
information from, and follows the chain of DNS servers back to the
servers which know the data.

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
%doc CHANGES CONTACT README
%doc %{_mandir}/man8/*
%{_bindir}/*

%changelog
* Sat Dec 28 2002 Dag Wieers <dag@wieers.com> - 1.6-0
- Updated to 1.6 (name changed from dnstrace to dnstracer)

* Sun Jan 20 2002 Dag Wieers <dag@wieers.com> - 1.1-0
- Initial package.
