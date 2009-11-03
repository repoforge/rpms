# $Id$
# Authority: dag
# Upstream: Paul Mison <cpan$husk,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name File-Type

Summary: Perl module to determine file type using magic
Name: perl-File-Type
Version: 0.22
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/File-Type/

Source: http://www.cpan.org/modules/by-module/File/File-Type-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl

%description
File-Type is a Perl module to determine file type using magic.

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
%doc %{_mandir}/man3/File::Type.3pm*
%doc %{_mandir}/man3/File::Type::Builder.3pm*
%dir %{perl_vendorlib}/File/
%{perl_vendorlib}/File/Type/
%{perl_vendorlib}/File/Type.pm

%changelog
* Tue May 01 2007 Dag Wieers <dag@wieers.com> - 0.22-1
- Initial package. (using DAR)
