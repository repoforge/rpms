# $Id$
# Authority: dries
# Upstream: Apocalypse <perl$0ne,us>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name POE-Component-Server-SimpleHTTP

Summary: Serve HTTP requests in POE
Name: perl-POE-Component-Server-SimpleHTTP
Version: 1.23
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/POE-Component-Server-SimpleHTTP/

Source: http://search.cpan.org/CPAN/authors/id/B/BI/BINGOS/POE-Component-Server-SimpleHTTP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(POE::Component::SSLify), perl(ExtUtils::MakeMaker)

%description
Serve HTTP requests in POE.

%prep
%setup -n %{real_name}-%{version}

%build
echo y | %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/POE/Component/
%dir %{perl_vendorlib}/POE/Component/Server/
%{perl_vendorlib}/POE/Component/Server/SimpleHTTP.pm
%{perl_vendorlib}/POE/Component/Server/SimpleHTTP/

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 1.23-1
- Updated to release 1.23.

* Tue Sep 19 2006 Dries Verachtert <dries@ulyssis.org> - 1.13-1
- Initial package.

