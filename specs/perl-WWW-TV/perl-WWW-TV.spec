# $Id$
# Authority: dries
# Upstream: Danial Pearce <cpan$tigris,id,au>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name WWW-TV

Summary: Parse TV.com for information about TV shows
Name: perl-WWW-TV
Version: 0.14
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/WWW-TV/

Source: http://www.cpan.org/modules/by-module/WWW/WWW-TV-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Parse TV.com for information about TV shows.

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
%doc %{_mandir}/man3/WWW::TV.3pm*
%doc %{_mandir}/man3/WWW::TV::*.3pm*
%dir %{perl_vendorlib}/WWW/
%{perl_vendorlib}/WWW/TV/
%{perl_vendorlib}/WWW/TV.pm

%changelog
* Mon Jun  8 2009 Christoph Maser <cmr@financial.com> - 0.14-1
- Updated to version 0.14.

* Fri Mar 14 2008 Dag Wieers <dag@wieers.com> - 0.09-1
- Updated to release 0.09.

* Mon Nov 19 2007 Dag Wieers <dag@wieers.com> - 0.08-1
- Updated to release 0.08.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.07-1
- Initial package.
