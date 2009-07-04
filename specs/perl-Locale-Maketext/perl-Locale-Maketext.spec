# $Id$
# Authority: dag
# Upstream: Andy Lester <andy$petdance,com>

# ExclusiveDist: rh6 el2 rh7

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Locale-Maketext

Summary: framework for localization and inheritance-based lexicons for Perl
Name: perl-Locale-Maketext
Version: 1.13
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Locale-Maketext/

Source: http://www.cpan.org/modules/by-module/Locale/Locale-Maketext-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.00503
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl >= 0:5.00503

%description
Locale::Maketext is a base class providing a framework for
localization and inheritance-based lexicons, as described in my
article in The Perl Journal #13 (a corrected version of which appears
in this dist).

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
%doc ChangeLog MANIFEST MANIFEST.SKIP META.yml README
%doc %{_mandir}/man3/Locale::Maketext.3pm*
%doc %{_mandir}/man3/Locale::Maketext::*.3pm*
%dir %{perl_vendorlib}/Locale/
%{perl_vendorlib}/Locale/Maketext/
%{perl_vendorlib}/Locale/Maketext.pm
%{perl_vendorlib}/Locale/Maketext.pod

%changelog
* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 1.13-1
- Updated to version 1.13.

* Tue Jun 24 2008 Dag Wieers <dag@wieers.com> - 1.13-1
- Updated to release 1.13.

* Sat Nov 24 2007 Dag Wieers <dag@wieers.com> - 1.12-1
- Updated to release 1.12.

* Tue Nov 13 2007 Dag Wieers <dag@wieers.com> - 1.10-1
- Updated to release 1.10.

* Sat Apr 02 2005 Dag Wieers <dag@wieers.com> - 1.06-1
- Cosmetic cleanup.

* Mon Jul 14 2003 Dag Wieers <dag@wieers.com> - 1.06-0
- Updated to release 1.06.

* Sat Feb 01 2003 Dag Wieers <dag@wieers.com> - 1.03-0
- Initial package. (using DAR)
