# $Id$
# Authority: dries
# Upstream: Dave Paris <a-mused$pobox,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Crypt-IDEA

Summary: IDEA block cipher
Name: perl-Crypt-IDEA
Version: 1.08
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Crypt-IDEA/

Source: http://search.cpan.org/CPAN/authors/id/D/DP/DPARIS/Crypt-IDEA-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
Perl interface to IDEA block cipher.

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
#%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorarch}/Crypt/IDEA.p*
%{perl_vendorarch}/Crypt/._test.pl
%{perl_vendorarch}/auto/Crypt/IDEA

%changelog
* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 1.08-1
- Updated to release 1.08.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 1.07-1
- Updated to release 1.07.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.06-1.2
- Rebuild for Fedora Core 5.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 1.06-1
- Updated to release 1.06.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.02-1
- Initial package.
