# $Id$
# Authority: dries
# Upstream: Steffen M&#252;ller <u4ezf9v02$sneakemail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Math-Random-Cauchy

Summary: Random numbers following a Cauchy PDF
Name: perl-Math-Random-Cauchy
Version: 0.02
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-Random-Cauchy/

Source: http://search.cpan.org/CPAN/authors/id/S/SM/SMUELLER/Math-Random-Cauchy-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
Random numbers following a Cauchy PDF.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/Math::Random::Cauchy*
%{perl_vendorlib}/Math/Random/Cauchy.pm
%dir %{perl_vendorlib}/Math/Random/

%changelog
* Wed May 02 2007 Dries Verachtert <dries@ulyssis.org> - 0.02-1
- Updated to release 0.02.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.01-1
- Initial package.
