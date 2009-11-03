# $Id$
# Authority: dries
# Upstream: H. Merijn Brand <h,merijn$xs4all,nl>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-CSV_XS

Summary: Comma-separated values manipulation routines
Name: perl-Text-CSV_XS
Version: 0.69
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-CSV_XS/

Source: http://www.cpan.org/modules/by-module/Text/Text-CSV_XS-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl(Config)
BuildRequires: perl(DynaLoader)
#BuildRequires: perl(IO::Handle)
#BuildRequires: perl(Test::Harness)
#BuildRequires: perl(Test::More)
BuildRequires: perl(Tie::Scalar)
BuildRequires: perl >= 5.005
Requires: perl(DynaLoader)
Requires: perl(IO::Handle)
Requires: perl >= 5.005

%filter_from_requires /^perl*/d
%filter_setup

%description
Text::CSV provides facilities for the composition and decomposition of
comma-separated values.  An instance of the Text::CSV class can combine
fields into a CSV string and parse a CSV string into fields.

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
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog MANIFEST META.yml README examples/
%doc %{_mandir}/man3/Text::CSV_XS.3pm*
%dir %{perl_vendorarch}/auto/Text/
%{perl_vendorarch}/auto/Text/CSV_XS/
%dir %{perl_vendorarch}/Text/
%{perl_vendorarch}/Text/CSV_XS.pm

%changelog
* Thu Oct 22 2009 Christoph Maser <cmr@financial.com> - 0.69-1
- Updated to version 0.69.

* Sat Aug 29 2009 Christoph Maser <cmr@financial.com> - 0.67-1
- Updated to version 0.67.

* Thu Jun 11 2009 Christoph Maser <cmr@financial.com> - 0.65-1
- Updated to version 0.65.

* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 0.45-1
- Updated to release 0.45.

* Fri Mar 14 2008 Dag Wieers <dag@wieers.com> - 0.37-1
- Updated to release 0.37.

* Mon Mar 03 2008 Dag Wieers <dag@wieers.com> - 0.35-1
- Updated to release 0.35.

* Wed Jan 23 2008 Dag Wieers <dag@wieers.com> - 0.34-1
- Updated to release 0.34.

* Fri Jan 04 2008 Dag Wieers <dag@wieers.com> - 0.33-1
- Updated to release 0.33.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 0.32-1
- Updated to release 0.32.

* Tue Mar  1 2005 Dries Verachtert <dries@ulyssis.org> - 0.23-1
- Initial package.
