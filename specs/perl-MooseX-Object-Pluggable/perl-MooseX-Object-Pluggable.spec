# $Id$
# Authority: dag
# Upstream: Guillermo Roditi <groditi$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name MooseX-Object-Pluggable

Summary: Perl module to make your classes pluggable
Name: perl-MooseX-Object-Pluggable
Version: 0.0011
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/MooseX-Object-Pluggable/

Source: http://www.cpan.org/modules/by-module/MooseX/MooseX-Object-Pluggable-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Module::Pluggable::Object)
BuildRequires: perl(Moose) >= 0.17
#BuildRequires: perl(Test::More) >= 0.62
BuildRequires: perl(ExtUtils::MakeMaker)

%description
MooseX-Object-Pluggable is a Perl module to make your classes pluggable.

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
%doc %{_mandir}/man3/MooseX::Object::Pluggable.3pm*
#%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/MooseX/
%dir %{perl_vendorlib}/MooseX/Object/
#%{perl_vendorlib}/MooseX/Object/Pluggable/
%{perl_vendorlib}/MooseX/Object/Pluggable.pm

%changelog
* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 0.0011-1
- Updated to version 0.0011.

* Wed Jan 23 2008 Dag Wieers <dag@wieers.com> - 0.0007-1
- Updated to release 0.0007.

* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 0.0005-1
- Initial package. (using DAR)
