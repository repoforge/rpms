# $Id$
# Authority: dries
# Upstream: Michael Stepanov <stepanov,michael$gmail,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name WWW-Yahoo-Movies

Summary: Get Yahoo Movies information
Name: perl-WWW-Yahoo-Movies
Version: 0.03
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/WWW-Yahoo-Movies/

Source: http://search.cpan.org/CPAN/authors/id/S/ST/STEPANOV/WWW-Yahoo-Movies-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 5.8.6

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
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/WWW/Yahoo/Movies.pm

%changelog
* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 0.03-1
- Updated to release 0.03.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.02-1.2
- Rebuild for Fedora Core 5.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.02-1
- Initial package.
