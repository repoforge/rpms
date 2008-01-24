# $Id$
# Authority: dries
# Upstream: Chris Williams <chris$bingosnet,co,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name POE-Component-Server-Ident

Summary: POE component that provides non-blocking ident services to your sessions
Name: perl-POE-Component-Server-Ident
Version: 1.12
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/POE-Component-Server-Ident/

Source: http://www.cpan.org/modules/by-module/POE/POE-Component-Server-Ident-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More) >= 0.47

%description
POE::Component::Server::Ident is POE (Perl Object Environment) component which
provides a non-blocking Identd for other components and POE sessions.

The component will mainly of use to the authors of client components and sessions
which sometimes have a requirement to prove the authenticity of the username that
has a connection to a server daemon.

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
%doc %{_mandir}/man3/POE::Component::Server::Ident.3pm*
%dir %{perl_vendorlib}/POE/
%dir %{perl_vendorlib}/POE/Component/
%dir %{perl_vendorlib}/POE/Component/Server/
%{perl_vendorlib}/POE/Component/Server/Ident.pm

%changelog
* Wed Jan 23 2008 Dag Wieers <dag@wieers.com> - 1.12-1
- Updated to release 1.12.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 1.10-1
- Updated to release 1.10.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 1.08-1
- Updated to release 1.08.

* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 1.06-1
- Updated to release 1.06.

* Tue Sep 19 2006 Dries Verachtert <dries@ulyssis.org> - 1.05-1
- Initial package.
