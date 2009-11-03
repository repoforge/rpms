# $Id$
# Authority: cmr
# Upstream: Florian Ragwitz C<rafl$debian,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Class-C3-Adopt-NEXT

Summary: make NEXT suck less
Name: perl-Class-C3-Adopt-NEXT
Version: 0.12
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Class-C3-Adopt-NEXT/

Source: http://www.cpan.org/modules/by-module/Class/Class-C3-Adopt-NEXT-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::Exception) >= 0.27
# From yaml requires
BuildRequires: perl(List::MoreUtils)
BuildRequires: perl(MRO::Compat)
BuildRequires: perl(NEXT)


%description
make NEXT suck less.

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
%doc %{_mandir}/man3/Class::C3::Adopt::NEXT.3pm*
%dir %{perl_vendorlib}/Class/
%dir %{perl_vendorlib}/Class/C3/
%dir %{perl_vendorlib}/Class/C3/Adopt/
#%{perl_vendorlib}/Class/C3/Adopt/NEXT/
%{perl_vendorlib}/Class/C3/Adopt/NEXT.pm

%changelog
* Sat Aug 22 2009 Christoph Maser <cmr@financial.com> - 0.12-1
- Initial package. (using DAR)
