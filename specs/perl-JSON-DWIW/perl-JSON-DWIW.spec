# $Id$
# Authority: dag
# Upstream: Don Owens <dowens$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name JSON-DWIW

Summary: Perl module that implements a JSON converter that Does What I Want
Name: perl-JSON-DWIW
Version: 0.36
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/JSON-DWIW/

Source: http://www.cpan.org/modules/by-module/JSON/JSON-DWIW-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

# this module satisfies the requirements for JSON::Any
Provides: perl-JSON-Any-alternative = 1.21

%description
perl-JSON-DWIW is a Perl module that implements a JSON converter that
Does What I Want.

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
%doc Artistic INSTALL META.yml README
%doc %{_mandir}/man3/JSON::DWIW.3pm*
%doc %{_mandir}/man3/JSON::DWIW::Changes.3pm*
%doc %{_mandir}/man3/JSON::DWIW::Boolean.3pm*
%dir %{perl_vendorarch}/auto/JSON/
%{perl_vendorarch}/auto/JSON/DWIW/
%dir %{perl_vendorarch}/JSON/
%{perl_vendorarch}/JSON/DWIW/
%{perl_vendorarch}/JSON/DWIW.pm

%changelog
* Wed Sep  9 2009 Christoph Maser <cmr@financial.com> - 0.36-1
- Updated to version 0.36.

* Thu Jul  9 2009 Christoph Maser <cmr@financial.com> - 0.35-1
- Updated to version 0.35.

* Tue Jul  7 2009 Christoph Maser <cmr@financial.com> - 0.34-2
- Update Provides: perl-JSON-Any-alternative to 1.21

* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 0.34-1
- Updated to version 0.34.

* Fri Jun 12 2009 Steve Huff <shuff@vecna.org> - 0.27-2
- Added Provides: perl-JSON-Any-alternative.

* Thu Oct 09 2008 Dag Wieers <dag@wieers.com> - 0.27-1
- Updated to release 0.27.

* Mon May 05 2008 Dag Wieers <dag@wieers.com> - 0.24-1
- Updated to release 0.24.

* Fri Jan 04 2008 Dag Wieers <dag@wieers.com> - 0.21-1
- Updated to release 0.21.

* Tue Nov 13 2007 Dag Wieers <dag@wieers.com> - 0.19-1
- Updated to release 0.19.

* Sun Aug 05 2007 Dag Wieers <dag@wieers.com> - 0.13-1
- Initial package. (using DAR)
