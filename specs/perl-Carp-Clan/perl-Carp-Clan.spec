# $Id$
# Authority: dries
# Upstream: Joshua ben Jore <jjore$cpan,org>

### EL6 ships with perl-Carp-Clan-6.03-2.el6
%{?el6:# Tag: rfx}
### EL5 ships with perl-Carp-Clan-5.3-1.2.1
%{?el5:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Carp-Clan

Summary: Report errors from perspective of caller of a "clan" of modules
Name: perl-Carp-Clan
Version: 6.04
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Carp-Clan/

Source: http://search.cpan.org/CPAN/authors/id/S/ST/STBEY/Carp-Clan-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module reports errors from the perspective of the caller of a
"clan" of modules, similar to "Carp.pm" itself. But instead of giving
it a number of levels to skip on the calling stack, you give it a
pattern to characterize the package names of the "clan" of modules
which shall never be blamed for any error.

%prep
%setup -n %{real_name}-%{version}

%build
echo | %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
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
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/Carp/Clan.pm
%{perl_vendorlib}/Carp/Clan.pod

%changelog
* Thu Dec 31 2009 Christoph Maser <cmr@financial.com> - 6.04-1
- Updated to version 6.04.

* Fri Feb 22 2008 Dag Wieers <dag@wieers.com> - 6.00-2
- add ExcludeDist el4

* Fri Feb 22 2008 Dag Wieers <dag@wieers.com> - 6.00-1
- Updated to release 6.00.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 5.9-1
- Updated to release 5.9.

* Tue Nov 14 2006 Dries Verachtert <dries@ulyssis.org> - 5.8-1
- Updated to release 5.8.

* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 5.4-1
- Updated to release 5.4.

* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 5.3-1
- Initial package.
