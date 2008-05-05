# $Id$
# Authority: dag
# Upstream: Paul Johnson <pjcj$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Devel-Cover

Summary: Code coverage metrics for Perl
Name: perl-Devel-Cover
Version: 0.64
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Devel-Cover/

Source: http://www.cpan.org/modules/by-module/Devel/Devel-Cover-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(Digest::MD5)
BuildRequires: perl(Pod::Coverage) >= 0.06
BuildRequires: perl(PPI::HTML) >= 1.07
BuildRequires: perl(Storable)
BuildRequires: perl(Template) >= 2.00
BuildRequires: perl(Test::Differences)
BuildRequires: perl-Tidy >= 20060719
#BuildRequires: perl(Tidy) >= 20060719

%description
Devel-Cover module for perl.

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
%doc BUGS CHANGES MANIFEST MANIFEST.SKIP META.yml README TODO
%doc %{_mandir}/man1/cover.1*
%doc %{_mandir}/man1/cpancover.1*
%doc %{_mandir}/man1/gcov2perl.1*
%doc %{_mandir}/man3/Devel::Cover.3pm*
%doc %{_mandir}/man3/Devel::Cover::*.3pm*
%{_bindir}/cover
%{_bindir}/cpancover
%{_bindir}/gcov2perl
%dir %{perl_vendorarch}/Devel/
%{perl_vendorarch}/Devel/Cover/
%{perl_vendorarch}/Devel/Cover.pm
%dir %{perl_vendorarch}/auto/Devel/
%{perl_vendorarch}/auto/Devel/Cover/

%changelog
* Fri May 02 2008 Dag Wieers <dag@wieers.com> - 0.64-1
- Updated to release 0.64.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 0.63-1
- Updated to release 0.63.

* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 0.62-1
- Updated to release 0.62.

* Tue May 01 2007 Dag Wieers <dag@wieers.com> - 0.61-1
- Initial package. (using DAR)
