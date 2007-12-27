# $Id$
# Authority: dries
# Upstream: Apocalypse <APOCAL$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name POE-Component-Server-SimpleHTTP

Summary: Perl extension to serve HTTP requests in POE
Name: perl-POE-Component-Server-SimpleHTTP
Version: 1.30
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/POE-Component-Server-SimpleHTTP/

Source: http://www.cpan.org/modules/by-module/POE/POE-Component-Server-SimpleHTTP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(LWP::ConnCache)
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(POE::Component::Client::HTTP)
BuildRequires: perl(POE::Component::SSLify)
BuildRequires: perl(Test::More) >= 0.47

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

