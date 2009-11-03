# $Id$
# Authority: dag
# Upstream: Earle Martin

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DateTime-Format-IBeat

Summary: Perl module to format times in .beat notation
Name: perl-DateTime-Format-IBeat
Version: 0.161
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DateTime-Format-IBeat/

Source: http://www.cpan.org/modules/by-module/DateTime/DateTime-Format-IBeat-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More) >= 0.47

%description
DateTime-Format-IBeat is a Perl module to format times in .beat notation.

This package contains the following Perl module:

    DateTime::Format::IBeat

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
%doc Artistic COPYING Changes INSTALL LICENCE MANIFEST MANIFEST.SKIP META.yml README
%doc %{_mandir}/man3/DateTime::Format::IBeat.3pm*
%dir %{perl_vendorlib}/DateTime/
%dir %{perl_vendorlib}/DateTime/Format/
%{perl_vendorlib}/DateTime/Format/IBeat.pm

%changelog
* Mon Apr 30 2007 Dag Wieers <dag@wieers.com> - 0.161-1
- Initial package. (using DAR)
