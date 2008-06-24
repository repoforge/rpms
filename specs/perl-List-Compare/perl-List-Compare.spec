# $Id$
# Authority: dries
# Upstream: James E Keenan <jkeenan$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name List-Compare

Summary: Compare elements of two or more lists
Name: perl-List-Compare
Version: 0.37
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/List-Compare/

Source: http://www.cpan.org/modules/by-module/List/List-Compare-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Compare elements of two or more lists.

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
%doc Changes FAQ MANIFEST MANIFEST.SKIP META.yml README
%doc %{_mandir}/man3/List::Compare.3pm*
%doc %{_mandir}/man3/List::Compare::*.3pm*
%dir %{perl_vendorlib}/List/
%{perl_vendorlib}/List/Compare/
%{perl_vendorlib}/List/Compare.pm

%changelog
* Tue Jun 24 2008 Dag Wieers <dag@wieers.com> - 0.37-1
- Updated to release 0.37.

* Tue Nov 13 2007 Dag Wieers <dag@wieers.com> - 0.35-1
- Updated to release 0.35.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.33-1
- Updated to release 0.33.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.32-1
- Updated to release 0.32.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.31-1
- Initial package.
