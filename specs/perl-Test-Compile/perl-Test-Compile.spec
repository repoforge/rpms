# $Id$
# Authority: dag
# Upstream: Marcel Grënauer <marcel$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-Compile

Summary: check whether Perl module files compile correctly
Name: perl-Test-Compile
Version: 0.13
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-Compile/

Source: http://search.cpan.org/CPAN/authors/id/M/MA/MARCEL/Test-Compile-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl(ExtUtils::MakeMaker) 
#BuildRequires: perl(Test::More) >= 0.88
BuildRequires: perl(Test::More) 
BuildRequires: perl(UNIVERSAL::require)
BuildRequires: perl >= v5.6.0
Requires: perl(UNIVERSAL::require)
Requires: perl >= v5.6.0

### remove autoreq Perl dependencies
%filter_from_requires /^perl*/d
%filter_setup

%description
check whether Perl module files compile correctly.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}" --skipdeps
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
%doc %{_mandir}/man3/Test::Compile.3pm*
%dir %{perl_vendorlib}/Test/
#%{perl_vendorlib}/Test/Compile/
%{perl_vendorlib}/Test/Compile.pm

%changelog
* Tue Feb  8 2011 Christoph Maser <cmaser@gmx.de> - 0.13-1
- Updated to version 0.13.

* Wed Dec  9 2009 Christoph Maser <cmr@financial.com> - 0.11-1
- Updated to version 0.11.

* Thu Oct 22 2009 Christoph Maser <cmr@financial.com> - 0.10-1
- Updated to version 0.10.

* Thu Feb 21 2008 Dag Wieers <dag@wieers.com> - 0.08-1
- Updated to release 0.08.

* Sat Dec 08 2007 Dag Wieers <dag@wieers.com> - 0.07-1
- Updated to release 0.07.

* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 0.05-1
- Initial package. (using DAR)
