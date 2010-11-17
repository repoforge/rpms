# $Id$
# Authority: dries
# Upstream: Audrey Tang <cpan$audreyt,org>

### EL6 ships with perl-YAML-Syck-1.07-4.el6
%{?el6:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name YAML-Syck

Summary: Fast, lightweight YAML loader and dumper
Name: perl-YAML-Syck
Version: 1.07
Release: 3%{?dist}
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/YAML-Syck/

Source: http://www.cpan.org/modules/by-module/YAML/YAML-Syck-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 0:5.3.7
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl >= 0:5.3.7

# this module satisfies the requirements for JSON::Any
Provides: perl-JSON-Any-alternative = 1.21

%description
perl-YAML-Syck contains a fast, lightweight YAML loader and dumper.

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
%doc COPYING Changes MANIFEST META.yml README 
%doc %{_mandir}/man3/JSON::Syck.3pm*
%doc %{_mandir}/man3/YAML::Syck.3pm*
%dir %{perl_vendorarch}/auto/YAML/
%{perl_vendorarch}/auto/YAML/Syck/
%dir %{perl_vendorarch}/JSON/
%{perl_vendorarch}/JSON/Syck.pm
%dir %{perl_vendorarch}/YAML/
%dir %{perl_vendorarch}/YAML/Dumper/
%{perl_vendorarch}/YAML/Dumper/Syck.pm
%dir %{perl_vendorarch}/YAML/Loader/
%{perl_vendorarch}/YAML/Loader/Syck.pm
%{perl_vendorarch}/YAML/Syck.pm

%changelog
* Tue Jul  7 2009 Christoph Maser <cmr@financial.com> - 0.34-2
- Update Provides: perl-JSON-Any-alternative to 1.21

* Fri Jun 12 2009 Steve Huff <shuff@vecna.org> - 1.07-2
- Added Provides: perl-JSON-Any-alternative.

* Fri May 29 2009 Christoph Maser <cmr@financial.com> - 1.07-1
- Updated to version 1.07.

* Mon Jun 23 2008 Dag Wieers <dag@wieers.com> - 1.05-1
- Updated to release 1.05.

* Wed Feb 20 2008 Dag Wieers <dag@wieers.com> - 1.04-1
- Updated to release 1.04.

* Wed Jan 23 2008 Dag Wieers <dag@wieers.com> - 1.01-1
- Updated to release 1.01.

* Fri Dec 14 2007 Dag Wieers <dag@wieers.com> - 1.00-1
- Updated to release 1.00.

* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.99-1
- Updated to release 0.99.

* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 0.72-1
- Updated to release 0.72.

* Tue Nov 14 2006 Dries Verachtert <dries@ulyssis.org> - 0.71-1
- Updated to release 0.71.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.67-1
- Updated to release 0.67.

* Tue May 30 2006 Dries Verachtert <dries@ulyssis.org> - 0.45-1
- Initial package.
