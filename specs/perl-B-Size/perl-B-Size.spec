# $Id$
# Authority: dries
# Upstream: Doug MacEachern <dougm$pobox,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name B-Size

Summary: Measure size of Perl OPs and SVs
Name: perl-B-Size
Version: 0.09
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/B-Size/

Source: http://search.cpan.org/CPAN/authors/id/P/PG/PGOLLUCCI/B-Size-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
Tools to measure size of Perl OPs and [SAV]Vs.

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
%{perl_vendorarch}/B/*Size.pm
%{perl_vendorarch}/auto/B/Size

%changelog
* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 0.09-1
- Updated to release 0.09.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 0.08-1
- Updated to release 0.08.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.06-1.2
- Rebuild for Fedora Core 5.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 0.06-1
- Updated to release 0.06.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.05-1
- Initial package.
