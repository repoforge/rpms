# $Id$
# Authority: dries
# Upstream: Ray Finch <rdf$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Clone

Summary: Recursively copy Perl datatypes
Name: perl-Clone
Version: 0.31
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Clone/

Source: http://www.cpan.org/modules/by-module/Clone/Clone-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
With this module, you can recursively copy Perl datatypes.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml
%doc %{_mandir}/man3/Clone.3pm*
%{perl_vendorarch}/auto/Clone/
%{perl_vendorarch}/Clone.pm

%changelog
* Wed Jul 15 2009 Christoph Maser <cmr@financial.com> - 0.31-1
- Updated to version 0.31.

* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 0.29-1
- Updated to release 0.29.

* Wed Nov 07 2007 Dag Wieers <dag@wieers.com> - 0.28-1
- Updated to release 0.28.

* Tue Nov 14 2006 Dries Verachtert <dries@ulyssis.org> - 0.22-1
- Updated to release 0.22.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.20-1
- Updated to release 0.20.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 0.18-1
- Updated to release 0.18.

* Tue Dec 07 2004 Dries Verachtert <dries@ulyssis.org> - 0.15-1
- Initial package.
