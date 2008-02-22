# $Id$
# Authority: dries
# Upstream: Chris Williams <chris$bingosnet,co,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name POE-Component-Server-IRC

Summary: Event-driven networkable IRC server daemon
Name: perl-POE-Component-Server-IRC
Version: 1.28
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/POE-Component-Server-IRC/

Source: http://www.cpan.org/modules/by-module/POE/POE-Component-Server-IRC-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More) >= 0.47

%description
A fully event-driven networkable IRC server daemon module.

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
%doc Changes MANIFEST MANIFEST.SKIP META.yml README examples/
%doc %{_mandir}/man1/pmkpasswd.1*
%doc %{_mandir}/man3/POE::Component::Server::IRC.3pm*
%doc %{_mandir}/man3/POE::Component::Server::IRC::*.3pm*
%{_bindir}/pmkpasswd
%dir %{perl_vendorlib}/POE/
%dir %{perl_vendorlib}/POE/Component/
%dir %{perl_vendorlib}/POE/Component/Server/
%{perl_vendorlib}/POE/Component/Server/IRC/
%{perl_vendorlib}/POE/Component/Server/IRC.pm

%changelog
* Thu Feb 21 2008 Dag Wieers <dag@wieers.com> - 1.28-1
- Updated to release 1.28.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 1.24-1
- Updated to release 1.24.

* Fri Jan 05 2007 Dries Verachtert <dries@ulyssis.org> - 1.07-1
- Updated to release 1.07.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 1.05-1
- Initial package.
