# $Id$
# Authority: shuff
# Upstream: Jonathan Rockway <jrockway$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Weewar

Summary: get data from the weewar.com XML API
Name: perl-%{real_name}
Version: 0.01
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Weewar/

Source: http://search.cpan.org/CPAN/authors/id/J/JR/JROCKWAY/%{real_name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

Requires: perl(Class::Accessor)

%description
This module lets you interact with the (Weewar) API. See Weewar::User,
Weewar::Game, and Weewar::HQ for details about what data you can get from the
API.

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
%doc MANIFEST
%doc %{_mandir}/man3/Weewar*.3pm*
%dir %{perl_vendorlib}/Weewar/
%{perl_vendorlib}/Weewar/*.pm
%{perl_vendorlib}/Weewar.pm

%changelog
* Thu Sep 24 2009 Steve Huff <shuff@vecna.org> - 0.01-1
- Initial package
