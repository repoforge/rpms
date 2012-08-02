# $Id$
# Authority: dag
# Upstream: Gisle Aas <gisle$ActiveState,com>

### EL6 ships with perl-URI-1.40-2.el6
%{?el6:# Tag: rfx}
### EL5 ships with perl-URI-1.35-3
%{?el5:# Tag: rfx}
### EL4 ships with perl-URI-1.30-4
%{?el4:# Tag: rfx}
### EL3 ships with perl-URI-1.21-7
%{?el3:# Tag: rfx}
### EL2 ships with perl-URI-1.12-5
%{?el2:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name URI

Summary: Perl module that implements Uniform Resource Identifiers (absolute and relative)
Name: perl-URI
Version: 1.60
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/URI/

Source: http://search.cpan.org/CPAN/authors/id/G/GA/GAAS/URI-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(MIME::Base64) >= 2
BuildRequires: perl >= 5.008001
Requires: perl(MIME::Base64) >= 2
Requires: perl >= 5.008001

%filter_from_requires /^perl*/d
%filter_setup

%description
perl-URI is a Perl module that implements Uniform Resource Identifiers.
(absolute and relative)

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}
%{__make} test

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README uri-test
%doc %{_mandir}/man3/URI.3pm*
%doc %{_mandir}/man3/URI::*.3pm*
%{perl_vendorlib}/URI/
%{perl_vendorlib}/URI.pm

%changelog
* Thu Aug  2 2012 Steve Huff <shuff@vecna.org> - 1.60-1
- Updated to version 1.60.

* Mon Feb  7 2011 Christoph Maser <cmaser@gmx.de> - 1.58-1
- Updated to version 1.58.

* Wed Apr  7 2010 Christoph Maser <cmr@financial.com> - 1.54-1
- Updated to version 1.54.

* Fri Mar 26 2010 Christoph Maser <cmr@financial.com> - 1.53-1
- Updated to version 1.53.

* Thu Dec 31 2009 Christoph Maser <cmr@financial.com> - 1.52-1
- Updated to version 1.52.

* Wed Dec  9 2009 Christoph Maser <cmr@financial.com> - 1.51-1
- Updated to version 1.51.

* Sat Aug 29 2009 Christoph Maser <cmr@financial.com> - 1.40-1
- Updated to version 1.40.

* Mon Jun  8 2009 Christoph Maser <cmr@financial.com> - 1.38-1
- Updated to version 1.38.

* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 1.36-1
- Updated to release 1.36.

* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 1.35-1
- Initial package. (using DAR)
