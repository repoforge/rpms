# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Date-Pcalc

Summary: Gregorian calendar date calculations
Name: perl-Date-Pcalc
Version: 1.2
Release: 1.2
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Date-Pcalc/

Source: http://www.cpan.org/modules/by-module/Date/Date-Pcalc-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)
Requires: perl

%description
Gregorian calendar date calculations

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib}
%{__rm} -rf %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc *.html *.txt
%doc %{_mandir}/man3/Date::Pcalc.3pm*
%{perl_vendorlib}/Date/Pcalc.pm

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.2-1.2
- Rebuild for Fedora Core 5.

* Sat Aug 07 2004 Dag Wieers <dag@wieers.com> - 1.2-1
- Initial package. (using DAR)
