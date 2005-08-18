# $Id$
# Authority: dries
# Upstream: Ilya Zakharevich <cpan$ilyaz,org>

%define pari_version 2.1.6

%define real_name Math-Pari
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Perl interface to PARI
Name: perl-Math-Pari
Version: 2.010601
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-Pari/

Source0: http://search.cpan.org/CPAN/authors/id/I/IL/ILYAZ/modules/Math-Pari-%{version}.tar.gz
Source1: pari-%{pari_version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
Math::Pari is the PERL interface to the PARI part of GP/PARI (version 2.*).
More info can be found at http://www.parigp-home.de/

%prep
%setup -n %{real_name}-%{version} -a 1

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" destdir=%{buildroot}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README Changes
%doc %{_mandir}/man3/*
%{perl_vendorarch}/Math/Pari*
%{perl_vendorarch}/Math/libPARI*
%{perl_vendorarch}/auto/Math/Pari/Pari.*
%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Mon Dec 27 2004 Dries Verachtert <dries@ulyssis.org> - 2.010601-1
- Initial package.
