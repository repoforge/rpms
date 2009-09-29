# $Id$
# Authority: cmr
# Upstream: Mons Anderson <mons$cpan,org>
# needs new Cwd
# ExcludeDist: el4

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name lib-abs

Summary: The same as C<lib>, but makes relative path absolute
Name: perl-lib-abs
Version: 0.90
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/lib-abs/

Source: http://www.cpan.org/modules/by-module/lib/lib-abs-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More)
BuildRequires: perl(Cwd) >= 3.12

%filter_from_requires /^perl(module2)/d
%filter_setup



%description
The same as C<lib>, but makes relative path absolute.

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

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README examples/
%doc %{_mandir}/man3/lib::abs.3pm*
%dir %{perl_vendorlib}/lib/
#%{perl_vendorlib}/lib/abs/
%{perl_vendorlib}/lib/abs.pm

%changelog
* Tue Sep 29 2009 Christoph Maser <cmr@financial.com> - 0.90-1
- Initial package. (using DAR)
