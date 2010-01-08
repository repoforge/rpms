# $Id$
# Authority: shuff
# Upstream: Marc Lehmann <schmorp@schmorp.de>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name AnyEvent-HTTP

Summary: a simple but non-blocking HTTP/HTTPS client
Name: perl-%{real_name}
Version: 1.44
Release: 1%{?dist}
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/AnyEvent-HTTP/

Source: http://www.cpan.org/authors/id/M/ML/MLEHMANN/AnyEvent-HTTP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(AnyEvent) >= 5.0
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl(AnyEvent) >= 5.0

%filter_from_requires /^perl*/d
%filter_setup

%description
AnyEvent provides a framework for multiple event loops.

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
%doc COPYING Changes MANIFEST META.yml README 
%doc %{_mandir}/man3/AnyEvent::HTTP.3pm*
%dir %{perl_vendorlib}/AnyEvent/
%{perl_vendorlib}/AnyEvent/HTTP.pm

%changelog
* Fri Jan  8 2010 Christoph Maser <cmr@financial.com> - 1.44-1
- Updated to version 1.44.

* Thu Sep 17 2009 Steve Huff <shuff@vecna.org> - 1.43-1
- Initial package.
