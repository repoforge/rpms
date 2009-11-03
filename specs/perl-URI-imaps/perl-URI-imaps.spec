# $Id$
# Authority: dag
# Upstream: Casey West <casey$geeknest,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name URI-imaps

Summary: Perl module to support IMAPS URI
Name: perl-URI-imaps
Version: 1.01
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/URI-imaps/

Source: http://www.cpan.org/modules/by-module/URI/URI-imaps-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-URI-imaps is a Perl module to support IMAPS URI.

This package contains the following Perl module:

    URI::imaps

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/URI::imaps.3pm*
%dir %{perl_vendorlib}/URI/
#%{perl_vendorlib}/URI/imaps/
%{perl_vendorlib}/URI/imaps.pm

%changelog
* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 1.01-1
- Initial package. (using DAR)
