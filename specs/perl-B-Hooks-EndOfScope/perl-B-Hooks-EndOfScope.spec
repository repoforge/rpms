# $Id$
# Authority: cmr
# Upstream: Florian Ragwitz <rafl$debian,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name B-Hooks-EndOfScope

Summary: Execute code after a scope finished compilation
Name: perl-B-Hooks-EndOfScope
Version: 0.08
Release: 2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/B-Hooks-EndOfScope/

Source: http://www.cpan.org/modules/by-module/B/B-Hooks-EndOfScope-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 2:5.8.0
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More)
Requires: perl >= 2:5.8.0

%description
Execute code after a scope finished compilation.

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
%doc Changes MANIFEST MANIFEST.SKIP META.yml README
%doc %{_mandir}/man3/B::Hooks::EndOfScope.3pm*
%dir %{perl_vendorlib}/B/
%dir %{perl_vendorlib}/B/Hooks/
#%{perl_vendorlib}/B/Hooks/EndOfScope/
%{perl_vendorlib}/B/Hooks/EndOfScope.pm

%changelog
* Fri May 29 2009 Christoph Maser <cmr@financial.com> - 0.08-2
- Adjust dependencies

* Fri May 29 2009 Christoph Maser <cmr@financial.com> - 0.08-1
- Initial package. (using DAR)
