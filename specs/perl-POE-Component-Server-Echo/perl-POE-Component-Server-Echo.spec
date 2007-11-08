# Authority: dries
# Upstream: Chris Williams <chris$bingosnet,co,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name POE-Component-Server-Echo

Summary: POE component implementing an RFC 862 Echo server
Name: perl-POE-Component-Server-Echo
Version: 1.51
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/POE-Component-Server-Echo/

Source: http://www.cpan.org/modules/by-module/POE/POE-Component-Server-Echo-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
A POE component implementing a RFC 862 Echo server.

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/POE::Component::Server::Echo.3pm*
%dir %{perl_vendorlib}/POE/
%dir %{perl_vendorlib}/POE/Component/
%dir %{perl_vendorlib}/POE/Component/Server/
%{perl_vendorlib}/POE/Component/Server/Echo.pm

%changelog
* Thu Jul 5 2007 Quien Sabe (aka Jim) <quien-sabe@metaorg.com> - 1.51-1
- Updated to latest upstream version { old source not available }

* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 1.4-1
- Updated to release 1.4.

* Tue Sep 19 2006 Dries Verachtert <dries@ulyssis.org> - 1.2-1
- Initial package.
# $Id$
