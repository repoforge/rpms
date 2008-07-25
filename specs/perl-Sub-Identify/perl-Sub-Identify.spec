# $Id$
# Authority: dag
# Upstream: Rafaël Garcia-Suarez <rgarciasuarez$gmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Sub-Identify

Summary: Perl module to retrieve names of code references
Name: perl-Sub-Identify
Version: 0.03
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Sub-Identify/

Source: http://www.cpan.org/modules/by-module/Sub/Sub-Identify-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
Requires: perl

%description
Sub-Identify is a Perl module to retrieve names of code references.

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
%doc Changes MANIFEST META.yml
%doc %{_mandir}/man3/Sub::Identify.3pm*
%dir %{perl_vendorlib}/Sub/
%{perl_vendorlib}/Sub/Identify.pm

%changelog
* Fri Jul 25 2008 Dries Verachtert <dries@ulyssis.org> - 0.03-1
- Updated to release 0.03.

* Tue May 01 2007 Dag Wieers <dag@wieers.com> - 0.02-1
- Initial package. (using DAR)
