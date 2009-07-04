# $Id$
# Authority: dries
# Upstream: Rocco Caputo <rcaputo$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name POE-Component-Client-HTTP

Summary: Non-blocking/concurrent HTTP queries with POE
Name: perl-POE-Component-Client-HTTP
Version: 0.88
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/POE-Component-Client-HTTP/

Source: http://www.cpan.org/modules/by-module/POE/POE-Component-Client-HTTP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
A HTTP user-agent component.

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
%doc CHANGES CHANGES.OLD MANIFEST META.yml README examples/
%doc %{_mandir}/man3/POE::Component::Client::HTTP.3pm*
%doc %{_mandir}/man3/POE::Component::Client::HTTP::*.3pm*
%doc %{_mandir}/man3/POE::Filter::*.3pm*
%dir %{perl_vendorlib}/POE/
%dir %{perl_vendorlib}/POE/Component/
%dir %{perl_vendorlib}/POE/Component/Client/
%{perl_vendorlib}/POE/Component/Client/HTTP/
%{perl_vendorlib}/POE/Component/Client/HTTP.pm
%{perl_vendorlib}/POE/Filter/

%changelog
* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 0.88-1
- Updated to version 0.88.

* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 0.83-1
- Updated to release 0.83.

* Thu Nov 15 2007 Dag Wieers <dag@wieers.com> - 0.82-1
- Updated to release 0.82.

* Sat Jan 06 2007 Dries Verachtert <dries@ulyssis.org> - 0.80-1
- Updated to release 0.80.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.78-1
- Initial package.
