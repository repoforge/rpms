# $Id$
# Authority: dries
# Upstream: Walery Studennikov <despairr$gmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-Whois-Raw

Summary: Get Whois information for domains
Name: perl-Net-Whois-Raw
Version: 2.13
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-Whois-Raw/

Source: http://search.cpan.org/CPAN/authors/id/D/DE/DESPAIR/Net-Whois-Raw-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Encode)
BuildRequires: perl(Getopt::Long) >= 2
BuildRequires: perl(HTTP::Headers)
BuildRequires: perl(HTTP::Request)
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(Module::Build)
BuildRequires: perl(Test::More)
BuildRequires: perl(URI::URL)
BuildRequires: perl >= 5.008001
Requires: perl(Encode)
Requires: perl(Getopt::Long) >= 2
Requires: perl(HTTP::Headers)
Requires: perl(HTTP::Request)
Requires: perl(LWP::UserAgent)
Requires: perl(Test::More)
Requires: perl(URI::URL)
Requires: perl >= 5.008001

%filter_from_requires /^perl*/d
%filter_setup

%description
Get Whois information for domains.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Build.PL --installdirs vendor --destdir %{buildroot}
./Build

%install
%{__rm} -rf %{buildroot}
./Build pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYRIGHT Changes MANIFEST META.yml README
%doc %{_mandir}/man1/pwhois.1*
%doc %{_mandir}/man3/Net::Whois::Raw.3pm*
%{_bindir}/pwhois
%dir %{perl_vendorlib}/Net/
%dir %{perl_vendorlib}/Net/Whois/
%{perl_vendorlib}/Net/Whois/Raw/
%{perl_vendorlib}/Net/Whois/Raw.pm

%changelog
* Wed Feb  3 2010 Christoph Maser <cmr@financial.com> - 2.13-1
- Updated to version 2.13.

* Thu Dec 10 2009 Christoph Maser <cmr@financial.com> - 2.12-1
- Updated to version 2.12.

* Thu Sep 17 2009 Christoph Maser <cmr@financial.com> - 2.04-1
- Updated to version 2.04.

* Tue Sep  8 2009 Christoph Maser <cmr@financial.com> - 2.02-1
- Updated to version 2.02.

* Thu Jul 30 2009 Christoph Maser <cmr@financial.com> - 2.01-1
- Updated to version 2.01.

* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 2.00-1
- Updated to version 2.00.

* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 1.52-1
- Updated to release 1.52.

* Thu Feb 28 2008 Dag Wieers <dag@wieers.com> - 1.42-1
- Updated to release 1.42.

* Thu Feb 21 2008 Dag Wieers <dag@wieers.com> - 1.41-1
- Updated to release 1.41.

* Sat Nov 24 2007 Dag Wieers <dag@wieers.com> - 1.38-1
- Updated to release 1.38.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 1.36-1
- Updated to release 1.36.

* Thu Nov 15 2007 Dag Wieers <dag@wieers.com> - 1.34-1
- Updated to release 1.34.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 1.20-1
- Initial package.
