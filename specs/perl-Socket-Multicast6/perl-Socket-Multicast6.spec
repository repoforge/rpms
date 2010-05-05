# $Id$
# Authority: dries
# Upstream: Nicholas J Humfrey <njh$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Socket-Multicast6

Summary: Constructors and constants for IPv4 and IPv6 multicast socket operations
Name: perl-Socket-Multicast6
Version: 0.04
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Socket-Multicast6/

Source: http://www.cpan.org/modules/by-module/Socket/Socket-Multicast6-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl(Devel::PPPort)
BuildRequires: perl(ExtUtils::CBuilder)
BuildRequires: perl(ExtUtils::Constant)
BuildRequires: perl(Module::Build) >= 0.20
BuildRequires: perl(Socket)
BuildRequires: perl(Socket6) >= 0.19
BuildRequires: perl(Test::More)
BuildRequires: perl >= 5.6.1
Requires: perl(Socket)
Requires: perl(Socket6) >= 0.19
Requires: perl(Test::More)
Requires: perl >= 5.6.1

%filter_from_requires /^perl*/d
%filter_setup

%description
Constructors and constants for IPv4 and IPv6 multicast socket operations.

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
%doc Changes README
%doc %{_mandir}/man3/Socket::Multicast6*.3pm*
%dir %{perl_vendorarch}/Socket/
%{perl_vendorarch}/Socket/Multicast6.pm
%dir %{perl_vendorarch}/auto/Socket/
%{perl_vendorarch}/auto/Socket/Multicast6/

%changelog
* Thu Dec 10 2009 Christoph Maser <cmr@financial.com> - 0.04-1
- Updated to version 0.04.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.02-1
- Initial package.
