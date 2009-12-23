# $Id$
# Authority: dag
# Upstream: Marc Lehmann <pcg$goof,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name JSON-XS

Summary: Perl module that implements JSON serialising/deserialising
Name: perl-JSON-XS
Version: 2.26
Release: 1%{?dist}
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/JSON-XS/

Source: http://search.cpan.org/CPAN/authors/id/M/ML/MLEHMANN/JSON-XS-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(common::sense)
Requires: perl(common::sense)

%filter_from_requires /^perl*/d
%filter_setup

# this module satisfies the requirements for JSON::Any
Provides: perl-JSON-Any-alternative = 1.22

%description
perl-JSON-XS is a Perl module that implements JSON serialising/deserialising,
done correctly and fast.

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

### Clean up docs
find eg/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING Changes MANIFEST META.yml README eg/
%doc %{_mandir}/man1/json_xs.1*
%doc %{_mandir}/man3/JSON::XS.3pm*
%doc %{_mandir}/man3/JSON::XS::Boolean.3pm*
%{_bindir}/json_xs
%dir %{perl_vendorarch}/auto/JSON/
%{perl_vendorarch}/auto/JSON/XS/
%dir %{perl_vendorarch}/JSON/
%{perl_vendorarch}/JSON/XS/
%{perl_vendorarch}/JSON/XS.pm

%changelog
* Wed Dec 23 2009 Christoph Maser <cmr@financial.com> - 2.26-1
- Updated to version 2.26.

* Wed Sep  9 2009 Christoph Maser <cmr@financial.com> - 2.25-1
- Updated to version 2.25.

* Mon Jul  6 2009 Christoph Maser <cmr@financial.com> - 2.24-2
- Update Provides: perl-JSON-Any-alternative to 1.21

* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 2.24-1
- Updated to version 2.24.

* Fri Jun 12 2009 Steve Huff <shuff@vecna.org> - 2.23-2
- Added Provides: perl-JSON-Any-alternative.

* Thu Oct 09 2008 Dag Wieers <dag@wieers.com> - 2.23-1
- Updated to release 2.23.

* Mon Jun 23 2008 Dag Wieers <dag@wieers.com> - 2.21-1
- Updated to release 2.21.

* Mon May 05 2008 Dag Wieers <dag@wieers.com> - 2.2-1
- Updated to release 2.2.

* Sat Dec 08 2007 Dag Wieers <dag@wieers.com> - 2.01-1
- Updated to release 2.01.

* Wed Dec 05 2007 Dag Wieers <dag@wieers.com> - 2.0-1
- Updated to release 2.0.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 1.53-1
- Updated to release 1.53.

* Tue Nov 13 2007 Dag Wieers <dag@wieers.com> - 1.52-1
- Updated to release 1.52.

* Tue Aug 07 2007 Dag Wieers <dag@wieers.com> - 1.43-2
- Disabled auto-requires for eg/.

* Sat Aug 04 2007 Dag Wieers <dag@wieers.com> - 1.43-1
- Initial package. (using DAR)
