# $Id$
# Authority: dag
# Upstream: Ed Summers <ehs$pobox,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name MARC-Charset

Summary: Perl module to convert MARC-8 encoded strings to UTF-8
Name: perl-MARC-Charset
Version: 1.1
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/MARC-Charset/

Source: http://www.cpan.org/modules/by-module/MARC/MARC-Charset-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-MARC-Charset is a Perl module to convert MARC-8 encoded strings to UTF-8.

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
%doc %{_mandir}/man3/MARC::Charset.3pm*
%doc %{_mandir}/man3/MARC::Charset*.3pm*
#%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/MARC/
%{perl_vendorlib}/MARC/Charset/
%{perl_vendorlib}/MARC/Charset.pm

%changelog
* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 1.1-1
- Updated to version 1.1.

* Tue Jun 24 2008 Dag Wieers <dag@wieers.com> - 1.0-1
- Updated to release 1.0.

* Sun Oct 07 2007 Dag Wieers <dag@wieers.com> - 0.98-1
- Initial package. (using DAR)
