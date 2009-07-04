# $Id$
# Authority: dag
# Upstream: Carl Franks <cpan$fireartist,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Perl6-Junction

Summary: Perl6 style Junction operators in Perl5
Name: perl-Perl6-Junction
Version: 1.40000
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Perl6-Junction/

Source: http://www.cpan.org/modules/by-module/Perl6/Perl6-Junction-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Perl6 style Junction operators in Perl5.

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
%doc %{_mandir}/man3/Perl6::Junction.3pm*
%dir %{perl_vendorlib}/Perl6/
%{perl_vendorlib}/Perl6/Junction/
%{perl_vendorlib}/Perl6/Junction.pm

%changelog
* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 1.40000-1
- Updated to version 1.40000.

* Sat Nov 24 2007 Dag Wieers <dag@wieers.com> - 1.30000-1
- Switch to upstream version.

* Wed Nov 21 2007 Dag Wieers <dag@wieers.com> - 1.30-1
- Initial package. (using DAR)
