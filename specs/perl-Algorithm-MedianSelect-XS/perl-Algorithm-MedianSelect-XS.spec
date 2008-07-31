# $Id$
# Authority: dries
# Upstream: Steven Schubiger <schubiger$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Algorithm-MedianSelect-XS

Summary: Median finding algorithm
Name: perl-Algorithm-MedianSelect-XS
Version: 0.21
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Algorithm-MedianSelect-XS/

Source: http://www.cpan.org/modules/by-module/Algorithm/Algorithm-MedianSelect-XS-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(Module::Build)
BuildRequires: perl(Test::More)

%description
Algorithm::MedianSelect::XS finds the item which is smaller than half of
the integers and bigger than half of the integers.

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
%doc Changes INSTALL MANIFEST META.yml README
%doc %{_mandir}/man3/Algorithm::MedianSelect::XS.3pm*
%dir %{perl_vendorarch}/auto/Algorithm/
%dir %{perl_vendorarch}/auto/Algorithm/MedianSelect/
%{perl_vendorarch}/auto/Algorithm/MedianSelect/XS/
%dir %{perl_vendorarch}/Algorithm/
%dir %{perl_vendorarch}/Algorithm/MedianSelect/
%{perl_vendorarch}/Algorithm/MedianSelect/XS.pm

%changelog
* Sat Jul 26 2008 Dag Wieers <dag@wieers.com> - 0.21-1
- Updated to release 0.21.

* Wed Jan 23 2008 Dag Wieers <dag@wieers.com> - 0.20-1
- Updated to release 0.20.

* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 0.18-1
- Updated to release 0.18.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 0.16-1
- Updated to release 0.16.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.14-1
- Initial package.
