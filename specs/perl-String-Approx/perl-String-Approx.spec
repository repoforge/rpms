# $Id$
# Authority: dries
# Upstream: Jarkko Hietaniemi <jhi$iki,fi>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name String-Approx

Summary: Perl extension for approximate matching (fuzzy matching)
Name: perl-String-Approx
Version: 3.25
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/String-Approx/

Source: http://search.cpan.org/CPAN/authors/id/J/JH/JHI/String-Approx-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
The most important change was that the underlying algorithm was
changed completely.  Instead of doing everything in Perl using regular
expressions we now do the matching in C using the so-called Manber-Wu
k-differences algorithm shift-add.  You have met this algorithm if you
have used the agrep utility or the Glimpse indexing system.

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
%doc ChangeLog README
%doc %{_mandir}/man3/*
%{perl_vendorarch}/String/Approx.pm
%{perl_vendorarch}/auto/String/Approx

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 3.25-1.2
- Rebuild for Fedora Core 5.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 3.25-1
- Updated to release 3.25.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 3.24-1
- Initial package.
