# $Id$
# Authority: dries
# Upstream: Abhijit Menon-Sen <ams$wiw,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Crypt-TEA

Summary: Tiny Encryption Algorithm
Name: perl-Crypt-TEA
Version: 1.25
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Crypt-TEA/

Source: http://search.cpan.org/CPAN/authors/id/A/AM/AMS/Crypt-TEA-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
TEA is a 64-bit symmetric block cipher with a 128-bit key
and a variable number of rounds (32 is recommended). It has a
low setup time, and depends on a large number of rounds for
security, rather than a complex algorithm. It was developed
by David J. Wheeler and Roger M. Needham, and is described at
http://www.ftp.cl.cam.ac.uk/ftp/papers/djw-rmn/djw-rmn-tea.html.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorarch}/Crypt/TEA.pm
%{perl_vendorarch}/auto/Crypt/TEA

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.25-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.25-1
- Initial package.
