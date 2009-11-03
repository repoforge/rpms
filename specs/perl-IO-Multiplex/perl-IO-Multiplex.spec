# $Id$
# Authority: dag
# Upstream: Rob Brown <bbb$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name IO-Multiplex

Summary: IO-Multiplex module for perl
Name: perl-IO-Multiplex
Version: 1.10
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/IO-Multiplex/

Source: http://www.cpan.org/modules/by-module/IO/IO-Multiplex-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 2:5.8.0
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl >= 2:5.8.0

%description
IO-Multiplex module for perl.

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

### Clean up docs
find contrib/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README TODO contrib/
%doc %{_mandir}/man3/IO::Multiplex.3pm*
%dir %{perl_vendorlib}/IO/
#%{perl_vendorlib}/IO/Multiplex/
%{perl_vendorlib}/IO/Multiplex.pm

%changelog
* Wed Oct 08 2008 Dag Wieers <dag@wieers.com> - 1.10-1
- Updated to release 1.10.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 1.09-1
- Updated to release 1.09.

* Sun Feb 20 2005 Dag Wieers <dag@wieers.com> - 1.08-2
- Cosmetic changes.

* Thu Mar 18 2004 Dag Wieers <dag@wieers.com> - 1.08-1
- Updated to release 1.08.

* Mon Jul 14 2003 Dag Wieers <dag@wieers.com> - 1.04-0
- Initial package. (using DAR)
