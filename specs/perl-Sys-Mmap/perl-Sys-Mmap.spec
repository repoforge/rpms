# $Id$
# Authority: dag
# Upstream: Todd Rinaldo <toddr@cpan.org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Sys-Mmap

Summary: Perl module to use mmap to map in a file as a Perl variable
Name: perl-Sys-Mmap
Version: 0.14
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Sys-Mmap/

Source: http://search.cpan.org/CPAN/authors/id/T/TO/TODDR/Sys-Mmap-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl(DynaLoader)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More)
BuildRequires: perl(XSLoader)
Requires: perl(DynaLoader)
Requires: perl(Test::More)
Requires: perl(XSLoader)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
perl-Sys-Mmap is a Perl module to use mmap to map in a file as a Perl variable.

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
%doc Artistic Changes Copying MANIFEST META.yml README
%doc %{_mandir}/man3/Sys::Mmap.3pm*
%dir %{perl_vendorarch}/Sys/
%{perl_vendorarch}/Sys/Mmap.pm
%dir %{perl_vendorarch}/auto/Sys/
%{perl_vendorarch}/auto/Sys/Mmap/

%changelog
* Thu Feb 10 2011 Christoph Maser <cmaser@gmx.de> - 0.14-1
- Updated to version 0.14.

* Sun Oct 07 2007 Dag Wieers <dag@wieers.com> - 0.13-1
- Initial package. (using DAR)
