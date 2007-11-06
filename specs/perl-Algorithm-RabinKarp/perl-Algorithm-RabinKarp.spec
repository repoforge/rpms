# $Id$
# Authority: dries
# Upstream: Norman Nunley, Jr <nnunley$gmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Algorithm-RabinKarp

Summary: Rabin-Karp streaming hash
Name: perl-Algorithm-RabinKarp
Version: 0.40
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Algorithm-RabinKarp/

Source: http://search.cpan.org//CPAN/authors/id/N/NN/NNUNLEY/Algorithm-RabinKarp-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker), perl

%description
Rabin-Karp streaming hash.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog
%doc %{_mandir}/man3/Algorithm::RabinKarp*
%{_bindir}/rabin.pl
%{perl_vendorlib}/Algorithm/RabinKarp.pm
%{perl_vendorlib}/Algorithm/RabinKarp/
%{perl_vendorlib}/Algorithm/rabin.pl

%changelog
* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.40-1
- Initial package.
