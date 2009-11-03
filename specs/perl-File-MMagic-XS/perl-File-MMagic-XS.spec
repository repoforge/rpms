# $Id$
# Authority: dag
# Upstream: Daisuke Maki <daisuke$endeworks,jp>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name File-MMagic-XS

Summary: Perl module to guess File Type With XS (a la mod_mime_magic)
Name: perl-File-MMagic-XS
Version: 0.09003
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/File-MMagic-XS/

Source: http://www.cpan.org/modules/by-module/File/File-MMagic-XS-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl

%description
File-MMagic-XS is a Perl module to guess File Type With XS
(a la mod_mime_magic).

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
%doc %{_mandir}/man3/File::MMagic::XS.3pm*
#%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/File/
%dir %{perl_vendorarch}/File/MMagic/
%{perl_vendorarch}/File/MMagic/XS.pm
%{perl_vendorarch}/File/MMagic/benchmark.pl
%{perl_vendorarch}/File/MMagic/magic
%dir %{perl_vendorarch}/auto/File/
%dir %{perl_vendorarch}/auto/File/MMagic/
%{perl_vendorarch}/auto/File/MMagic/XS/

%changelog
* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 0.09003-1
- Updated to release 0.09003.

* Tue May 01 2007 Dag Wieers <dag@wieers.com> - 0.08-1
- Initial package. (using DAR)
