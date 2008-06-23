# $Id$
# Authority: dries
# Upstream: Luis Mu&#241;oz <luismunoz$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Authen-Challenge-Basic

Summary: Basic challenge/response authentication scheme
Name: perl-Authen-Challenge-Basic
Version: 0.1
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Authen-Challenge-Basic/

Source: http://www.cpan.org/modules/by-module/Authen/Authen-Challenge-Basic-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This is a perl5 module implementing basic MD5-based challenge/response.
The authentication method provided, allows for mutual authentications
of the endpoints of a communication channel provided that a shared
secret known only to them has been exchanged prior to the session.

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
%doc README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Authen/Challenge/Basic.pm

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.1-1
- Initial package.
