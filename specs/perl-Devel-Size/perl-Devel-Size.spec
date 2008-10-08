# $Id$
# Authority: dries
# Upstream: Tels <nospam-abuse$bloodgate,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Devel-Size

Summary: Perl extension for finding the memory usage of Perl variables
Name: perl-Devel-Size
Version: 0.71
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Devel-Size/

Source: http://www.cpan.org/modules/by-module/Devel/Devel-Size-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 0:5.006
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More) >= 0.42
Requires: perl >= 0:5.006

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
%dir %{perl_vendorarch}/auto/Devel/
%{perl_vendorarch}/auto/Devel/Size/
%dir %{perl_vendorarch}/Devel/
#%{perl_vendorarch}/Devel/Size/
%{perl_vendorarch}/Devel/Size.pm

%changelog
* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 0.71-1
- Updated to release 0.71.

* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 0.69-1
- Updated to release 0.69.

* Wed Jan  4 2006 Dries Verachtert <dries@ulyssis.org> - 0.64-1
- Initial package.
