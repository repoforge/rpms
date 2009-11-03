# $Id$
# Authority: dries
# Upstream: Darren Chamberlain <darren$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name String-Format

Summary: Sprintf-like string formatting capabilities with arbitrary format definitions
Name: perl-String-Format
Version: 1.16
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/String-Format/

Source: http://www.cpan.org/modules/by-module/String/String-Format-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
String::Format lets you define arbitrary printf-like format
sequences to be expanded. This module would be most useful in
configuration files and reporting tools, where the results of a
query need to be formatted in a particular way.

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
%doc %{_mandir}/man3/String::Format.3pm*
%dir %{perl_vendorlib}/String/
#%{perl_vendorlib}/String/Format/
%{perl_vendorlib}/String/Format.pm

%changelog
* Thu Jun 18 2009 Christoph Maser <cmr@financial.com> - 1.16-1
- Updated to version 1.16.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 1.14-1
- Updated to release 1.14.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.13-1
- Initial package.
