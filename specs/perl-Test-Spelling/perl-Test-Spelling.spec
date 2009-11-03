# $Id$
# Authority: dag
# Upstream: Ivan Tubert-Brohman <itub$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-Spelling

Summary: Perl module to check for spelling errors in POD files
Name: perl-Test-Spelling
Version: 0.11
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-Spelling/

Source: http://www.cpan.org/modules/by-module/Test/Test-Spelling-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
perl-Test-Spelling is a Perl module to check for spelling errors in POD files.

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
%doc %{_mandir}/man3/Test::Spelling.3pm*
%dir %{perl_vendorlib}/Test/
%{perl_vendorlib}/Test/Spelling.pm

%changelog
* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 0.11-1
- Initial package. (using DAR)
