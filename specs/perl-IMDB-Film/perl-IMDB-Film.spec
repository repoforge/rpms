# $Id$
# Authority: dries
# Upstream: Michael Stepanov <stepanov,michael$gmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name IMDB-Film

Summary: Interface to IMDB
Name: perl-IMDB-Film
Version: 0.38
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/IMDB-Film/

Source: http://www.cpan.org/authors/id/S/ST/STEPANOV/IMDB-Film-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
IMDB::Film is OO Perl interface to the database of films
IMDB (www.imdb.com). It allows to retrieve information
about movies by its IMDB code or title. Also, there is a
possibility to get information about IMDB persons (actors,
actresses, directors etc) by their name of code.

%prep
%setup -n %{real_name}-%{version}

%build
echo | %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
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
%doc ChangeLog LICENSE MANIFEST MANIFEST.SKIP META.yml README Todo
%doc %{_mandir}/man3/IMDB::*.3pm*
%dir %{perl_vendorlib}/IMDB/
%{perl_vendorlib}/IMDB/

%changelog
* Sun Jul  5 2009 Christoph Maser <cmr@financial.com> - 0.38-1
- Updated to version 0.38.

* Wed Oct 08 2008 Dag Wieers <dag@wieers.com> - 0.35-1
- Updated to release 0.35.

* Mon Jun 23 2008 Dag Wieers <dag@wieers.com> - 0.33-1
- Updated to release 0.33.

* Fri Jan 04 2008 Dag Wieers <dag@wieers.com> - 0.32-1
- Updated to release 0.32.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 0.31-1
- Updated to release 0.31.

* Tue Nov 13 2007 Dag Wieers <dag@wieers.com> - 0.30-1
- Updated to release 0.30.

* Mon Jun 18 2007 Dries Verachtert <dries@ulyssis.org> - 0.28-1
- Updated to release 0.28.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.27-1
- Updated to release 0.27.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.22-1
- Updated to release 0.22.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.20-1
- Updated to release 0.20.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.18-1.2
- Rebuild for Fedora Core 5.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 0.18-1
- Updated to release 0.18.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.15-1
- Initial package.
