# $Id$
# Authority: dries
# Upstream: Mark Overmeer <perl$overmeer,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name User-Identity

Summary: Maintains info about a physical person
Name: perl-User-Identity
Version: 0.93
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/User-Identity/

Source: http://search.cpan.org/CPAN/authors/id/M/MA/MARKOV/User-Identity-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::Pod) >= 1
Requires: perl(Test::Pod) >= 1

%filter_from_requires /^perl*/d
%filter_setup


%description
Maintains info about a physical person.

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
%doc %{_mandir}/man3/Mail::Identity.3pm*
%doc %{_mandir}/man3/User::Identity.3pm*
%doc %{_mandir}/man3/User::Identity::*.3pm*
%dir %{perl_vendorlib}/Mail/
%{perl_vendorlib}/Mail/Identity.pm
%{perl_vendorlib}/Mail/Identity.pod
%dir %{perl_vendorlib}/User/
%{perl_vendorlib}/User/Identity/
%{perl_vendorlib}/User/Identity.pm
%{perl_vendorlib}/User/Identity.pod

%changelog
* Mon Dec 28 2009 Christoph Maser <cmr@financial.com> - 0.93-1
- Updated to version 0.93.

* Tue Nov 13 2007 Dag Wieers <dag@wieers.com> - 0.92-1
- Updated to release 0.92.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.91-1
- Initial package.
