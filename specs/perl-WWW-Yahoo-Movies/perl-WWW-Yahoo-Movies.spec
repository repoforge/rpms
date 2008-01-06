# $Id$
# Authority: dries
# Upstream: Michael Stepanov <stepanov,michael$gmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name WWW-Yahoo-Movies

Summary: Get Yahoo Movies information
Name: perl-WWW-Yahoo-Movies
Version: 0.05
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/WWW-Yahoo-Movies/

Source: http://www.cpan.org/modules/by-module/WWW/WWW-Yahoo-Movies-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 3:5.8.6
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl >= 3:5.8.6

%description
WWW-Yahoo-Movies is OO Perl interface to the Yahoo! Movies.
It allows to retrieve information about movies by its ID Yahoo!
Movies or title.

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
%doc Changes LICENSE MANIFEST MANIFEST.SKIP META.yml README
%doc %{_mandir}/man3/WWW::Yahoo::Movies.3pm*
%dir %{perl_vendorlib}/WWW/
%dir %{perl_vendorlib}/WWW/Yahoo/
#%{perl_vendorlib}/WWW/Yahoo/Movies/
%{perl_vendorlib}/WWW/Yahoo/Movies.pm

%changelog
* Fri Jan 04 2008 Dag Wieers <dag@wieers.com> - 0.05-1
- Updated to release 0.05.

* Mon Jun 18 2007 Dries Verachtert <dries@ulyssis.org> - 0.04-1
- Updated to release 0.04.

* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 0.03-1
- Updated to release 0.03.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.02-1
- Initial package.
