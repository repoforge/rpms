# $Id$
# Authority: dag
# Upstream: Yuval Kogman <nothingmuch$woobling,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Catalyst-Plugin-Session-State-Cookie

Summary: Maintain session IDs using cookies
Name: perl-Catalyst-Plugin-Session-State-Cookie
Version: 0.09
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Catalyst-Plugin-Session-State-Cookie/

Source: http://www.cpan.org/modules/by-module/Catalyst/Catalyst-Plugin-Session-State-Cookie-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Catalyst::Runtime), perl(Catalyst::Plugin::Session), perl(Test::MockObject)

%description
Maintain session IDs using cookies.

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
%doc Changes MANIFEST README
%doc %{_mandir}/man3/Catalyst::Plugin::Session::State::Cookie.3pm*
%dir %{perl_vendorlib}/Catalyst/
%dir %{perl_vendorlib}/Catalyst/Plugin/
%dir %{perl_vendorlib}/Catalyst/Plugin/Session/
%dir %{perl_vendorlib}/Catalyst/Plugin/Session/State/
#%{perl_vendorlib}/Catalyst/Plugin/Session/State/Cookie/
%{perl_vendorlib}/Catalyst/Plugin/Session/State/Cookie.pm

%changelog
* Sun Dec 30 2007 Dag Wieers <dag@wieers.com> - 0.09-1
- Initial package. (using DAR)
