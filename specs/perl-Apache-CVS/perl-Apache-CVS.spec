# $Id$
# Authority: dries
# Upstream: John Barbee <barbee$veribox,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Apache-CVS

Summary: Method handler which provides a web interface to CVS repositories
Name: perl-Apache-CVS
Version: 0.10
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Apache-CVS/

Source: http://www.cpan.org/modules/by-module/Apache/Apache-CVS-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module contains a method handler which provides a web interface to CVS
repositories.

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
%{perl_vendorlib}/Apache/CVS.pm
%{perl_vendorlib}/Apache/CVS

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.10-1
- Initial package.
