# $Id$
# Authority: dries
# Upstream: Jarkko Hietaniemi <jhi$iki,fi>
# RFX: el6

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name BSD-Resource

Summary: BSD process resource limit and priority functions
Name: perl-BSD-Resource
Version: 1.2903
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/BSD-Resource/

Source: http://search.cpan.org/CPAN/authors/id/J/JH/JHI/BSD-Resource-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This Perl extension implements the BSD process resource limit functions
	getrusage()	getrlimit()	setrlimit()
and the BSD process priority functions.  These are available also via
core Perl but here we do more tricks so that the PRIO_* are available.
	getpriority()	setpriority()
Also is provided
	times()
which provides the same functionality as the one in core Perl, only
with better time resolution.

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
%doc ChangeLog INSTALL MANIFEST META.yml README
%doc %{_mandir}/man3/BSD::Resource.3pm*
%dir %{perl_vendorarch}/auto/BSD/
%{perl_vendorarch}/auto/BSD/Resource/
%dir %{perl_vendorarch}/BSD/
%{perl_vendorarch}/BSD/Resource.pm

%changelog
* Thu Jan  7 2010 Christoph Maser <cmr@financial.com> - 1.2903-1
- Updated to version 1.2903.

* Mon Feb 18 2008 Dag Wieers <dag@wieers.com> - 1.2901-1
- Updated to release 1.2901.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 1.28-1
- Updated to release 1.28.

* Sun Dec 19 2004 Dries Verachtert <dries@ulyssis.org> - 1.24-1
- Initial package.
