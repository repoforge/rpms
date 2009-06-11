# $Id$
# Authority: cmr
# Upstream: Iain Truskett <spoon$cpan,org>
# Upstream: Based on WWW::MakeAShorterLink by Dave Cross <dave$mag-sol,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name WWW-Shorten
%define real_version 1.98

Summary: Interface to URL shortening sites
Name: perl-WWW-Shorten
Version: 2.03
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/WWW-Shorten/

Source: http://www.cpan.org/modules/by-module/WWW/WWW-Shorten-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.006
BuildRequires: perl(Test::More) >= 0.47
Requires: perl >= 0:5.006

%description
Interface to URL shortening sites.

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
%doc AUTHORS Artistic COPYING CREDITS ChangeLog.SPOON Changes INSTALL LICENCE MANIFEST MANIFEST.SKIP META.yml README TODO
%doc %{_mandir}/man3/WWW::Shorten*.3pm*
%doc %{_mandir}/man1/shorten.1*
%dir %{perl_vendorlib}/WWW/
%{perl_vendorlib}/WWW/Shorten/
%{perl_vendorlib}/WWW/Shorten.pm
%{_bindir}/shorten

%changelog
* Thu Jun 11 2009 Unknown - 2.03-1
- Initial package. (using DAR)
