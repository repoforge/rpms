# $Id$
# Authority: dag
# Upstream: Damian Conway <damian$conway,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Contextual-Return
%define real_version 0.002001

Summary: Perl module to create context-senstive return values
Name: perl-Contextual-Return
Version: 0.2.1
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Contextual-Return/

#Source: http://www.cpan.org/modules/by-module/Contextual/Contextual-Return-v%{version}.tar.gz
Source: http://www.cpan.org/authors/id/D/DC/DCONWAY/Contextual-Return-v%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl

%description
Contextual-Return is a Perl module to create context-senstive return values.

%prep
%setup -n %{real_name}-v%{version}

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/Contextual/
%{perl_vendorlib}/Contextual/Return/
%{perl_vendorlib}/Contextual/Return.pm

%changelog
* Mon Apr 30 2007 Dag Wieers <dag@wieers.com> - 0.002001-1
- Initial package. (using DAR)
