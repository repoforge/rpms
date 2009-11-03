# $Id$
# Authority: dag
# Upstream: Adam Kennedy <cpan$ali,as>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name File-Find-Rule-PPI

Summary: Perl module to add support for PPI queries to File::Find::Rule
Name: perl-File-Find-Rule-PPI
Version: 0.05
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/File-Find-Rule-PPI/

Source: http://www.cpan.org/modules/by-module/File/File-Find-Rule-PPI-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl

%description
File-Find-Rule-PPI is a Perl module to add support
for PPI queries to File::Find::Rule.

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
%doc Changes LICENSE MANIFEST META.yml README
%doc %{_mandir}/man3/File::Find::Rule::PPI.3pm*
%dir %{perl_vendorlib}/File/
%dir %{perl_vendorlib}/File/Find/
%dir %{perl_vendorlib}/File/Find/Rule/
%{perl_vendorlib}/File/Find/Rule/PPI.pm

%changelog
* Tue May 01 2007 Dag Wieers <dag@wieers.com> - 0.05-1
- Initial package. (using DAR)
