# $Id$
# Authority: dries
# Upstream: Apocalypse <perl$0ne,us>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name POE-Component-Server-SOAP

Summary: Publish POE event handlers via SOAP over HTTP
Name: perl-POE-Component-Server-SOAP
Version: 1.14
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/POE-Component-Server-SOAP/

Source: http://www.cpan.org/modules/by-module/POE/POE-Component-Server-SOAP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
With this module, you can publish POE event handlers via SOAP over HTTP.

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

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/POE/
%dir %{perl_vendorlib}/POE/Component/
%dir %{perl_vendorlib}/POE/Component/Server/
%{perl_vendorlib}/POE/Component/Server/SOAP.pm
%{perl_vendorlib}/POE/Component/Server/SOAP/

%changelog
* Fri Jul  3 2009 Christoph Maser <cmr@financial.com> - 1.14-1
- Updated to version 1.14.

* Mon Jun 18 2007 Dries Verachtert <dries@ulyssis.org> - 1.11-1
- Updated to release 1.11.

* Tue Sep 19 2006 Dries Verachtert <dries@ulyssis.org> - 1.10-1
- Initial package.
