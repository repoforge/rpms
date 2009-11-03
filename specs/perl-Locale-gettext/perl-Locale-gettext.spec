# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name gettext

Summary: Internationalization for Perl
Name: perl-Locale-gettext
Version: 1.05
Release: 1%{?dist}
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/gettext/

Source: http://www.cpan.org/modules/by-module/Locale/gettext-%{version}.tar.gz
Patch1: gettext-1.01-includes.patch
Patch2: gettext-1.01-add-iconv.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 0:5.00503
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl >= 0:5.00503

%description
The gettext module permits access from perl to the gettext() family of
functions for retrieving message strings from databases constructed to
internationalize software.

It provides gettext(), dgettext(), dcgettext(), textdomain() and
bindtextdomain().

%prep
%setup -n %{real_name}-%{version}
#patch1 -p1 -b .includes
#patch2 -p0

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"
#%{__make} test

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man3/*.3*
%{perl_vendorarch}/Locale/
%{perl_vendorarch}/auto/Locale/

%changelog
* Sat Nov 05 2005 Dries Verachtert <dries@ulyssis.org> - 1.05-1
- Updated to release 1.05.

* Thu Oct 23 2003 Dag Wieers <dag@wieers.com> - 1.01-0
- Initial package. (using DAR)
