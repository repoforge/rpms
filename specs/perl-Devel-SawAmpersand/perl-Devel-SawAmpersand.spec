# $Id$
# Authority: dries
# Upstream: Andreas J. K&#246;nig <andreas,koenig$anima,de>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Devel-SawAmpersand

Summary: Perl extension querying sawampersand variable
Name: perl-Devel-SawAmpersand
Version: 0.31
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Devel-SawAmpersand/

Source: http://search.cpan.org/CPAN/authors/id/A/AN/ANDK/Devel-SawAmpersand-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
There's a global variable in the perl source, called sawampersand. It
gets set to true in that moment in which the parser sees one of $`, $',
and $&. It never can be set to false again. Trying to set it to false
breaks the handling of the $`, $&, and $' completely.

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
%doc %{_mandir}/man3/*
%{perl_vendorarch}/B/FindAmpersand.pm
%{perl_vendorarch}/Devel/SawAmpersand.pm
%{perl_vendorarch}/Devel/FindAmpersand.pm
%{perl_vendorarch}/auto/Devel/SawAmpersand

%changelog
* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 0.31-1
- Updated to release 0.31.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.30-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.30-1
- Initial package.
