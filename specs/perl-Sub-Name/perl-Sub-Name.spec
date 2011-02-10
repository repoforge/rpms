# $Id$
# Authority: dag
# Upstream: Florian Ragwitz <rafl@debian.org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Sub-Name

Summary: Perl module to (re)name a sub
Name: perl-Sub-Name
Version: 0.05
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Sub-Name/

Source: http://search.cpan.org/CPAN/authors/id/F/FL/FLORA/Sub-Name-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Sub-Name is a Perl module to (re)name a sub.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"
%{__make} test

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Sub::Name.3pm*
%dir %{perl_vendorarch}/auto/Sub/
%{perl_vendorarch}/auto/Sub/Name/
%dir %{perl_vendorarch}/Sub/
%{perl_vendorarch}/Sub/Name.pm

%changelog
* Thu Feb 10 2011 Christoph Maser <cmaser@gmx.de> - 0.05-1
- Updated to version 0.05.

* Wed Nov 26 2008 Dag Wieers <dag@wieers.com> - 0.04-1
- Updated to release 0.04.

* Mon Feb 25 2008 Dag Wieers <dag@wieers.com> - 0.03-1
- Updated to release 0.03.

* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 0.02-1
- Initial package. (using DAR)
