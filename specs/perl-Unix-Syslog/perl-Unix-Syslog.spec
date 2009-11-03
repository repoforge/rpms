# $Id$
# Authority: dag
# Upstream: Marcus Harnisch <marcus,harnisch$gmx,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Unix-Syslog

Summary: Syslog module for perl
Name: perl-Unix-Syslog
Version: 1.1
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Unix-Syslog/

Source: http://www.cpan.org/modules/by-module/Unix/Unix-Syslog-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 0:5.00503
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl >= 0:5.00503

%description
Syslog module for perl

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
%doc Artistic Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Unix::Syslog.3pm*
%dir %{perl_vendorarch}/auto/Unix/
%{perl_vendorarch}/auto/Unix/Syslog/
%dir %{perl_vendorarch}/Unix/
%{perl_vendorarch}/Unix/Syslog.pm

%changelog
* Mon Jun  8 2009 Christoph Maser <cmr@financial.com> - 1.1-1
- Updated to version 1.1.

* Mon Nov 19 2007 Dag Wieers <dag@wieers.com> - 1.0-1
- Updated to release 1.0.

* Tue Mar 29 2005 Dag Wieers <dag@wieers.com> - 0.100-1
- Cosmetic changes.

* Mon Jul 14 2003 Dag Wieers <dag@wieers.com> - 0.100-0
- Updated to release 0.100.

* Sun Jan 26 2003 Dag Wieers <dag@wieers.com>
- Initial package. (using DAR)
