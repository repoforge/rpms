# $Id$
# Authority: dries
# Upstream: Daniel Schroeer <schroeer$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Lingua-DE-Wortschatz

Summary: Wortschatz.uni-leipzig.de webservice client
Name: perl-Lingua-DE-Wortschatz
Version: 1.25
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Lingua-DE-Wortschatz/

Source: http://www.cpan.org/modules/by-module/Lingua/Lingua-DE-Wortschatz-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Module::Build)

%description
Wortschatz.uni-leipzig.de webservice client.

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
%doc MANIFEST META.yml README
%doc %{_mandir}/man1/wsws.pl.1*
%doc %{_mandir}/man3/Lingua::DE::Wortschatz.3pm*
%{_bindir}/wsws.pl
%dir %{perl_vendorlib}/Lingua/
%dir %{perl_vendorlib}/Lingua/DE/
#%{perl_vendorlib}/Lingua/DE/Wortschatz/
%{perl_vendorlib}/Lingua/DE/Wortschatz.pm

%changelog
* Sun Mar 02 2008 Dag Wieers <dag@wieers.com> - 1.25-1
- Updated to release 1.25.

* Sat Jan 26 2008 Dag Wieers <dag@wieers.com> - 1.24-1
- Updated to release 1.24.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.23-1
- Initial package.
