# $Id$
# Authority: dries
# Upstream: Apocalypse <perl$0ne,us>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name POE-Component-SSLify

Summary: Use SSL in POE
Name: perl-POE-Component-SSLify
Version: 0.08
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/POE-Component-SSLify/

Source: http://search.cpan.org//CPAN/authors/id/A/AP/APOCAL/POE-Component-SSLify-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
This module makes Net::SSLeay's SSL sockets behave with POE.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/POE/
%dir %{perl_vendorlib}/POE/Component/
%{perl_vendorlib}/POE/Component/SSLify.pm
%{perl_vendorlib}/POE/Component/SSLify/

%changelog
* Mon Jun 18 2007 Dries Verachtert <dries@ulyssis.org> - 0.08-1
- Updated to release 0.08.

* Tue Sep 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.06-1
- Initial package.
