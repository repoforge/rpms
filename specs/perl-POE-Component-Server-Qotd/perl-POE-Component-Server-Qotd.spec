# $Id$
# Authority: dries
# Upstream: Chris Williams <chris$bingosnet,co,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name POE-Component-Server-Qotd

Summary: POE component that implements an RFC 865 QotD server
Name: perl-POE-Component-Server-Qotd
Version: 1.10
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/POE-Component-Server-Qotd/

Source: http://www.cpan.org/modules/by-module/POE/POE-Component-Server-Qotd-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More) >= 0.47

%description
A POE component that implements an RFC 865 QotD server.

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

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README examples/
%doc %{_mandir}/man3/POE::Component::Server::Qotd.3pm*
%dir %{perl_vendorlib}/POE/
%dir %{perl_vendorlib}/POE/Component/
%dir %{perl_vendorlib}/POE/Component/Server/
%{perl_vendorlib}/POE/Component/Server/Qotd.pm

%changelog
* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 1.10-1
- Updated to release 1.10.

* Wed Jan 23 2008 Dag Wieers <dag@wieers.com> - 1.08-1
- Updated to release 1.08.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 1.07-1
- Updated to release 1.07.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 1.05-1
- Updated to release 1.05.

* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 1.03-1
- Updated to release 1.03.

* Tue Sep 19 2006 Dries Verachtert <dries@ulyssis.org> - 1.02-1
- Initial package.
