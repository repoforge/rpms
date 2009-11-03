# $Id$
# Authority: dag
# Upstream: Marcel Greünauer <marcel$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Attribute-TieClasses

Summary: Perl module that implements attribute wrappers for CPAN Tie classes
Name: perl-Attribute-TieClasses
Version: 0.03
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Attribute-TieClasses/

Source: http://www.cpan.org/modules/by-module/Attribute/Attribute-TieClasses-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.6.0 
BuildRequires: perl(Test::Compile)
BuildRequires: perl(Test::More)
BuildRequires: perl(UNIVERSAL::require)
Requires: perl >= 0:5.6.0 

%description
perl-Attribute-TieClasses is a Perl module that implements attribute wrappers
for CPAN Tie classes.

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
%doc %{_mandir}/man3/Attribute::TieClasses.3pm*
%dir %{perl_vendorlib}/Attribute/
#%{perl_vendorlib}/Attribute/TieClasses/
%{perl_vendorlib}/Attribute/TieClasses.pm

%changelog
* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 0.03-1
- Updated to release 0.03.

* Sun Oct 07 2007 Dag Wieers <dag@wieers.com> - 0.02-1
- Initial package. (using DAR)
