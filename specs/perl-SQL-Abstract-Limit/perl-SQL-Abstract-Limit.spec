# $Id$
# Authority: dag
# Upstream: David Baird <cpan$riverside-cms,co,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name SQL-Abstract-Limit

Summary: Portable LIMIT emulation
Name: perl-SQL-Abstract-Limit
Version: 0.141
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/SQL-Abstract-Limit/

Source: http://www.cpan.org/modules/by-module/SQL/SQL-Abstract-Limit-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Portable LIMIT emulation.

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
%doc %{_mandir}/man3/SQL::Abstract::Limit.3pm*
%dir %{perl_vendorlib}/SQL/
%dir %{perl_vendorlib}/SQL/Abstract/
%{perl_vendorlib}/SQL/Abstract/Limit.pm

%changelog
* Fri Apr 24 2009 Christoph Maser <cmr@financial.com> - 0.141-1
- Update version to 0.141

* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 0.12-1
- Initial package. (using DAR)
