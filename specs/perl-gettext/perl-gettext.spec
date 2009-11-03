# $Id$
# Authority: dag
# Upstream: Phillip Vandry <vandry$TZoNE,ORG>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name gettext

Summary: Perl module implementing message handling functions
Name: perl-gettext
Version: 1.05
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/gettext/

Source: http://www.cpan.org/authors/id/P/PV/PVANDRY/gettext-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
gettext module is a Perl module implementing message handling functions.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man3/Locale::gettext.3pm*
%dir %{perl_vendorarch}/auto/Locale/
%{perl_vendorarch}/auto/Locale/gettext/
%dir %{perl_vendorarch}/Locale/
%{perl_vendorarch}/Locale/gettext.pm

%changelog
* Mon Nov 19 2007 Dag Wieers <dag@wieers.com> - 1.05-1
- Updated to release 1.05.

* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 1.00-1
- Initial package. (using DAR)
