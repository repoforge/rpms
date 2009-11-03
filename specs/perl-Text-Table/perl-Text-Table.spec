# $Id$
# Authority: dag
# Upstream: Anno Siegel <siegel$zrz,tu-berlin,de>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-Table

Summary: Organize Data in Tables
Name: perl-Text-Table
Version: 1.114
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-Table/

Source: http://www.cpan.org/modules/by-module/Text/Text-Table-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Organize Data in Tables.

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
%doc Changes LICENSE MANIFEST MANIFEST.SKIP META.yml README
%doc %{_mandir}/man3/Text::Table.3pm*
%dir %{perl_vendorlib}/Text/
#%{perl_vendorlib}/Text/Table/
%{perl_vendorlib}/Text/Table.pm

%changelog
* Thu May 15 2008 Dag Wieers <dag@wieers.com> - 1.114-1
- Updated to release 1.114.

* Fri Nov 23 2007 Dag Wieers <dag@wieers.com> - 1.107-1
- Initial package. (using DAR)
