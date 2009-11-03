# $Id$
# Authority: cmr
# Upstream: Chris Williams <chris$bingosnet,co,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name POE-Filter-HTTP-Parser

Summary: A HTTP POE filter for HTTP clients or servers
Name: perl-POE-Filter-HTTP-Parser
Version: 1.02
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/POE-Filter-HTTP-Parser/

Source: http://www.cpan.org/modules/by-module/POE/POE-Filter-HTTP-Parser-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.6.0
BuildRequires: perl(ExtUtils::MakeMaker) 
BuildRequires: perl(Test::More) >= 0.47
BuildRequires: perl(Test::POE::Client::TCP) >= 0.1
BuildRequires: perl(Test::POE::Server::TCP) >= 0.16
# From yaml requires
BuildRequires: perl(HTTP::Parser) >= 0.04
BuildRequires: perl(HTTP::Request)
BuildRequires: perl(HTTP::Response)
BuildRequires: perl(HTTP::Status)
BuildRequires: perl(POE) >= 1.003
BuildRequires: perl >= 5.6.0


%description
A HTTP POE filter for HTTP clients or servers.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes LICENSE MANIFEST META.yml README examples/
%doc %{_mandir}/man3/POE::Filter::HTTP::Parser.3pm*
%dir %{perl_vendorlib}/POE/
%dir %{perl_vendorlib}/POE/Filter/
%dir %{perl_vendorlib}/POE/Filter/HTTP/
#%{perl_vendorlib}/POE/Filter/HTTP/Parser/
%{perl_vendorlib}/POE/Filter/HTTP/Parser.pm

%changelog
* Mon Sep 07 2009 Christoph Maser <cmr@financial.com> - 1.02-1
- Initial package. (using DAR)
