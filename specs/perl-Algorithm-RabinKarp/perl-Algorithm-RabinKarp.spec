# $Id$
# Authority: dries
# Upstream: Norman Nunley, Jr <nnunley$gmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Algorithm-RabinKarp

Summary: Rabin-Karp streaming hash
Name: perl-Algorithm-RabinKarp
Version: 0.41
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Algorithm-RabinKarp/

Source: http://www.cpan.org/modules/by-module/Algorithm/Algorithm-RabinKarp-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Temp)
BuildRequires: perl(Test::More)

%description
An implementation of the Rabin-Karp rolling hash algorithm.

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
%doc ChangeLog MANIFEST META.yml
%doc %{_mandir}/man3/Algorithm::RabinKarp.3pm*
%doc %{_mandir}/man3/Algorithm::RabinKarp::Util.3pm*
%{_bindir}/rabin.pl
%dir %{perl_vendorlib}/Algorithm/
%{perl_vendorlib}/Algorithm/RabinKarp/
%{perl_vendorlib}/Algorithm/RabinKarp.pm
%{perl_vendorlib}/Algorithm/rabin.pl

%changelog
* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 0.41-1
- Updated to release 0.41.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.40-1
- Initial package.
