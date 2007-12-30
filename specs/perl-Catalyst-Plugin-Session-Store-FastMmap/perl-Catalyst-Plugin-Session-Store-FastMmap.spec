# $Id$
# Authority: dag
# Upstream: Yuval Kogman <nothingmuch$woobling,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Catalyst-Plugin-Session-Store-FastMmap

Summary: FastMmap session storage backend
Name: perl-Catalyst-Plugin-Session-Store-FastMmap
Version: 0.03
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Catalyst-Plugin-Session-Store-FastMmap/

Source: http://www.cpan.org/modules/by-module/Catalyst/Catalyst-Plugin-Session-Store-FastMmap-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Catalyst::Runtime)

%description
FastMmap session storage backend.

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
%doc %{_mandir}/man3/Catalyst::Plugin::Session::Store::FastMmap.3pm*
%dir %{perl_vendorlib}/Catalyst/
%dir %{perl_vendorlib}/Catalyst/Plugin/
%dir %{perl_vendorlib}/Catalyst/Plugin/Session/
%dir %{perl_vendorlib}/Catalyst/Plugin/Session/Store/
#%{perl_vendorlib}/Catalyst/Plugin/Session/Store/FastMmap/
%{perl_vendorlib}/Catalyst/Plugin/Session/Store/FastMmap.pm

%changelog
* Sun Dec 30 2007 Dag Wieers <dag@wieers.com> - 0.03-1
- Initial package. (using DAR)
