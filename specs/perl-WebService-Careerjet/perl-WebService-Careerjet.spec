# $Id$
# Authority: dries
# Upstream: Jerome Eteve <jeromeAteteveDotnet>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name WebService-Careerjet

Summary: Perl interface to Careerjet's public search API
Name: perl-WebService-Careerjet
Version: 0.05
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/WebService-Careerjet/

Source: http://www.cpan.org/modules/by-module/WebService/WebService-Careerjet-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Perl interface to Careerjet's public search API.

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
%doc %{_mandir}/man3/WebService::Careerjet.3pm*
%{_bindir}/jobsearch
%dir %{perl_vendorlib}/WebService/
#%{perl_vendorlib}/WebService/Careerjet/
%{perl_vendorlib}/WebService/Careerjet.pm

%changelog
* Fri Mar 07 2008 Dag Wieers <dag@wieers.com> - 0.05-1
- Updated to release 0.05.

* Mon Nov 19 2007 Dag Wieers <dag@wieers.com> - 0.04-1
- Updated to release 0.04.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.03-1
- Initial package.
