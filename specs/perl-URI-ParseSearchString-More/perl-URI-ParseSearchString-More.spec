# $Id$
# Authority: dag
# Upstream: Olaf Alders <olaf$wundersolutions,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name URI-ParseSearchString-More

Summary: Perl module to extract search strings from more referrers
Name: perl-URI-ParseSearchString-More
Version: 0.13
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/URI-ParseSearchString-More/

Source: http://www.cpan.org/modules/by-module/URI/URI-ParseSearchString-More-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Config::General)
BuildRequires: perl(Data::Dump)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Spec)
BuildRequires: perl(List::Compare)
BuildRequires: perl(Params::Validate)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Pod)
BuildRequires: perl(Test::Pod::Coverage)
BuildRequires: perl(Test::Simple) >= 0.44
BuildRequires: perl(Test::WWW::Mechanize)
BuildRequires: perl(URI::Heuristic)
BuildRequires: perl(URI::ParseSearchString)
BuildRequires: perl(WWW::Mechanize)
BuildRequires: perl(WWW::Mechanize::Cached) >= 1.33
Requires: perl(Config::General)
Requires: perl(Data::Dump)
Requires: perl(File::Spec)
Requires: perl(List::Compare)
Requires: perl(Params::Validate)
Requires: perl(Test::More)
Requires: perl(Test::Pod)
Requires: perl(Test::Pod::Coverage)
Requires: perl(Test::Simple) >= 0.44
Requires: perl(Test::WWW::Mechanize)
Requires: perl(URI::Heuristic)
Requires: perl(URI::ParseSearchString)
Requires: perl(WWW::Mechanize)
Requires: perl(WWW::Mechanize::Cached) >= 1.33

%filter_from_requires /^perl*/d
%filter_setup

%description
perl-URI-ParseSearchString-More is a Perl module to extract search strings
from more referrers.

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
%doc Changes LICENSE MANIFEST README
%doc %{_mandir}/man3/URI::ParseSearchString::More.3pm*
%dir %{perl_vendorlib}/URI/
%dir %{perl_vendorlib}/URI/ParseSearchString/
#%{perl_vendorlib}/URI/ParseSearchString/More/
%{perl_vendorlib}/URI/ParseSearchString/More.pm

%changelog
* Wed Dec  9 2009 Christoph Maser <cmr@financial.com> - 0.13-1
- Updated to version 0.13.

* Wed Jul 29 2009 Christoph Maser <cmr@financial.com> - 0.12-1
- Updated to version 0.12.

* Mon Jul 13 2009 Christoph Maser <cmr@financial.com> - 0.11-1
- Updated to version 0.11.

* Mon Jun  8 2009 Christoph Maser <cmr@financial.com> - 0.10-1
- Updated to version 0.10.

* Mon Nov 19 2007 Dag Wieers <dag@wieers.com> - 0.05-1
- Updated to release 0.05.

* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.04-1
- Initial package. (using DAR)
