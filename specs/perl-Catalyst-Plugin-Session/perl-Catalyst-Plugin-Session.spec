# $Id$
# Authority: dag
# Upstream: Yuval Kogman <nothingmuch$woobling,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Catalyst-Plugin-Session

Summary: Generic Session plugin - ties together server side storage and client side state required to maintain session data.  
Name: perl-Catalyst-Plugin-Session
Version: 0.19
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Catalyst-Plugin-Session/

Source: http://www.cpan.org/modules/by-module/Catalyst/Catalyst-Plugin-Session-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Catalyst) >= 5.7
BuildRequires: perl(Object::Signature)
BuildRequires: perl(Tie::RefHash)
#BuildRequires: perl(Tie::RefHash) >= 1.34

%description
Generic Session plugin - ties together server side storage and client side state
required to maintain session data.

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
%doc Changes MANIFEST META.yml README SIGNATURE TODO
%doc %{_mandir}/man3/Catalyst::Plugin::Session.3pm*
%doc %{_mandir}/man3/Catalyst::Plugin::Session::*.3pm*
%dir %{perl_vendorlib}/Catalyst/
%dir %{perl_vendorlib}/Catalyst/Plugin/
%{perl_vendorlib}/Catalyst/Plugin/Session/
%{perl_vendorlib}/Catalyst/Plugin/Session.pm

%changelog
* Sun Dec 30 2007 Dag Wieers <dag@wieers.com> - 0.19-1
- Initial package. (using DAR)
