# $Id$

# Authority: dag

%define perl_vendorlib  %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch  %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name NetAddr-IP

Summary: Manages IPv4 and IPv6 addresses and subnets
Name: perl-NetAddr-IP
Version: 3.028
Release: 1
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/NetAddr-IP/

Source: http://www.cpan.org/modules/by-module/NetAddr/NetAddr-IP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.00503
Requires: perl >= 0:5.00503

%description
Manages IPv4 and IPv6 addresses and subnets.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL \
	PREFIX="%{buildroot}%{_prefix}" \
	INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
		%{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc MANIFEST README TODO tutorial.htm
%doc %{_mandir}/man?/*
%{perl_vendorlib}/*

%changelog
* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 3.028-1
- Updated to release 3.028.

* Sat Mar 03 2004 Dag Wieers <dag@wieers.com> - 3.20-1
- Initial package. (using DAR)
