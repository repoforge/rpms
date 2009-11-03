# $Id$
# Authority: dries
# Upstream: Julian Mehnle <julian$mehnle,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Mail-SPF-Query
%define real_version 1.999001

Summary: Query a Sender Policy Framework
Name: perl-Mail-SPF-Query
Version: 1.999.1
Release: 2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Mail-SPF-Query/

Source: http://www.cpan.org/modules/by-module/Mail/Mail-SPF-Query-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
With this module, you can use a Sender Policy Framework.

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
find bin/ examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES MANIFEST META.yml README bin/ examples/
%doc %{_mandir}/man3/Mail::SPF::Query*
%dir %{perl_vendorlib}/Mail/
%dir %{perl_vendorlib}/Mail/SPF/
%{perl_vendorlib}/Mail/SPF/Query.pm
%exclude %{_bindir}/spfd
%exclude %{_bindir}/spfquery
%exclude %{_mandir}/man1/spfd.1*
%exclude %{_mandir}/man1/spfquery.1*

%changelog
* Thu Oct 04 2007 Dag Wieers <dag@wieers.com> - 1.999.1-2
- Excluded spfd and spfquery, included them as documentation.

* Fri Mar  3 2006 Dries Verachtert <dries@ulyssis.org> - 1.999.1-1
- Initial package.
