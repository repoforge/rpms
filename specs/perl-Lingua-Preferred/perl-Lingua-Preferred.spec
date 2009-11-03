# $Id$
# Authority: dag
# Upstream: Ed Avis <ed$membled,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Lingua-Preferred
%define real_version 0.002004

Summary: Perl module named Lingua-Preferred
Name: perl-Lingua-Preferred
Version: 0.2.4
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Lingua-Preferred/

Source: http://www.cpan.org/modules/by-module/Lingua/Lingua-Preferred-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
perl-Lingua-Preferred is a Perl module.

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
%doc Changes MANIFEST README
%doc %{_mandir}/man3/Lingua::Preferred.3pm*
%dir %{perl_vendorlib}/Lingua/
%{perl_vendorlib}/Lingua/Preferred.pm
%{perl_vendorlib}/auto/Lingua/Preferred/

%changelog
* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 0.2.4-1
- Initial package. (using DAR)
