# $Id$
# Authority: dag
# Upstream: Erick Calder <ecalder$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Lingua-EN-Numericalize

Summary: Replaces English descriptions of numbers with numerals
Name: perl-Lingua-EN-Numericalize
Version: 1.52
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Lingua-EN-Numericalize/

Source: http://www.cpan.org/modules/by-module/Lingua/Lingua-EN-Numericalize-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Replaces English descriptions of numbers with numerals.

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
%doc Changes LICENSE MANIFEST README
%doc %{_mandir}/man3/Lingua::EN::Numericalize.3pm*
%dir %{perl_vendorlib}/Lingua/
%dir %{perl_vendorlib}/Lingua/EN/
#%{perl_vendorlib}/Lingua/EN/Numericalize/
%{perl_vendorlib}/Lingua/EN/Numericalize.pm

%changelog
* Fri Nov 23 2007 Dag Wieers <dag@wieers.com> - 1.52-1
- Initial package. (using DAR)
