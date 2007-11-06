# $Id$
# Authority: dries
# Upstream: Dana Hudes <dhudes$hudes,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-Whois

Summary: Get and parse whois domain data from InterNIC
Name: perl-Net-Whois
Version: 1.9
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-Whois/

Source: http://search.cpan.org/CPAN/authors/id/D/DH/DHUDES/Net-Whois-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
This is a Perl 5 module that retrieves and parses information from the
'whois' databases. Currently, only domains .com, .edu, .net are supported.
Forthcoming versions will support .mil, .gov, .arpa, and eventually other
top-level domains. Additional classes to get POC/Handle, Host, and all the other
things stored in the ARIN and 'InterNIC' whois databases and eventually
the RIPE and others as well.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Net/Whois.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.9-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.9-1
- Initial package.
