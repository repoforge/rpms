# $Id: perl-IP-Country.spec 171 2004-03-28 01:43:07Z dag $
# Authority: dag

%define perl_vendorlib  %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch  %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name NetAddr-IP

Summary: Manages IPv4 and IPv6 addresses and subnets
Name: perl-NetAddr-IP
Version: 3.20
Release: 1
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/NetAddr-IP/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://search.cpan.org/CPAN/authors/id/L/LU/LUISMUNOZ/NetAddr-IP-%{version}.tar.gz
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
%{__make} %{?_smp_mflags} \
        OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot (noarch)
%{__rm} -rf %{buildroot}%{perl_archlib} \
		%{buildroot}%{perl_vendorarch}

### Clean up buildroot (arch)
%{__rm} -rf %{buildroot}%{perl_archlib} \
                %{buildroot}%{perl_vendorarch}/auto/*{,/*{,/*}}/.packlist


%clean 
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc MANIFEST README TODO tutorial.htm
%doc %{_mandir}/man?/*

### (noarch)
%{perl_vendorlib}/*

### (arch)
%{perl_vendorarch}/*


%changelog
* Sat Mar 03 2004 Dag Wieers <dag@wieers.com> - 3.20-1
- Initial package. (using DAR)
