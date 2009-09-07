# $Id$
# Authority: dries
# Upstream: Apocalypse <APOCAL$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name POE-Component-Server-SimpleHTTP

Summary: Perl extension to serve HTTP requests in POE
Name: perl-POE-Component-Server-SimpleHTTP
Version: 2.0
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/POE-Component-Server-SimpleHTTP/

Source: http://www.cpan.org/modules/by-module/POE/POE-Component-Server-SimpleHTTP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
# From yaml build_requires
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(POE::Filter::HTTP::Parser) >= 0.02
BuildRequires: perl(Test::More) >= 0.47
BuildRequires: perl(Test::POE::Client::TCP) >= 0.1
# From yaml requires
BuildRequires: perl(Carp)
BuildRequires: perl(HTTP::Date)
BuildRequires: perl(HTTP::Request)
BuildRequires: perl(HTTP::Response)
BuildRequires: perl(Moose) >= 0.81
BuildRequires: perl(MooseX::AttributeHelpers)
BuildRequires: perl(MooseX::POE) >= 0.205
BuildRequires: perl(POE) >= 1.0000
BuildRequires: perl(Socket)
BuildRequires: perl(Storable)
BuildRequires: perl(Sys::Hostname)
BuildRequires: perl >= 5.6.0

%description
Perl extension to serve HTTP requests in POE.

%prep
%setup -n %{real_name}-%{version}

%build
echo "y" | %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

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
%doc Changes MANIFEST META.yml README examples/
%doc %{_mandir}/man3/POE::Component::Server::SimpleHTTP.3pm*
%doc %{_mandir}/man3/POE::Component::Server::SimpleHTTP::*.3pm*
%dir %{perl_vendorlib}/POE/
%dir %{perl_vendorlib}/POE/Component/
%dir %{perl_vendorlib}/POE/Component/Server/
%{perl_vendorlib}/POE/Component/Server/SimpleHTTP/
%{perl_vendorlib}/POE/Component/Server/SimpleHTTP.pm

%changelog
* Fri Sep  4 2009 Christoph Maser <cmr@financial.com> - 2.0-1
- Updated to version 2.0.

* Fri Jul  3 2009 Christoph Maser <cmr@financial.com> - 1.58-1
- Updated to version 1.58.

* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 1.46-1
- Updated to release 1.46.

* Thu Feb 21 2008 Dag Wieers <dag@wieers.com> - 1.42-1
- Updated to release 1.42.

* Wed Jan 23 2008 Dag Wieers <dag@wieers.com> - 1.40-1
- Updated to release 1.40.

* Thu Dec 27 2007 Dag Wieers <dag@wieers.com> - 1.30-1
- Updated to release 1.30.

* Fri Dec 14 2007 Dag Wieers <dag@wieers.com> - 1.28-1
- Updated to release 1.28.

* Tue Dec 04 2007 Dag Wieers <dag@wieers.com> - 1.25-1
- Updated to release 1.25.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 1.24-1
- Updated to release 1.24.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 1.23-1
- Updated to release 1.23.

* Tue Sep 19 2006 Dries Verachtert <dries@ulyssis.org> - 1.13-1
- Initial package.

