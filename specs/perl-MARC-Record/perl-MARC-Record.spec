# $Id$
# Authority: dag
# Upstream: Mike Rylander <mrylander$gmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name MARC-Record
%define real_version 2.0

Summary: Perl module for handling MARC fields
Name: perl-MARC-Record
Version: 2.0.0
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/MARC-Record/

Source: http://www.cpan.org/modules/by-module/MARC/MARC-Record-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 2:5.8.1
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl >= 2:5.8.1

%description
MARC-Record is a Perl module for handling MARC fields.

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
%doc %{_mandir}/man1/marcdump.1*
%doc %{_mandir}/man3/MARC::*.3pm*
%{_bindir}/marcdump
%{perl_vendorlib}/MARC/

%changelog
* Thu May 03 2007 Dag Wieers <dag@wieers.com> - 2.0.0-1
- Initial package. (using DAR)
