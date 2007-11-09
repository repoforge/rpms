# $Id$
# Authority: dries
# Upstream: Dan Sugalski <dan$sidhe,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Devel-Size

Summary: Find the memory usage of perl variables
Name: perl-Devel-Size
Version: 0.69
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Devel-Size/

Source: http://www.cpan.org/modules/by-module/Devel/Devel-Size-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More) >= 0.42

%description
Perl extension for finding the memory usage of Perl variables.

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
%doc CHANGES MANIFEST MANIFEST.SKIP META.yml README SIGNATURE
%doc %{_mandir}/man3/Devel::Size.3pm*
%dir %{perl_vendorarch}/Devel/
%{perl_vendorarch}/Devel/Size.pm
#%{perl_vendorarch}/Devel/Size/
%dir %{perl_vendorarch}/auto/Devel/
%{perl_vendorarch}/auto/Devel/Size/

%changelog
* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 0.69-1
- Updated to release 0.69.

* Wed Jan  4 2006 Dries Verachtert <dries@ulyssis.org> - 0.64-1
- Initial package.
