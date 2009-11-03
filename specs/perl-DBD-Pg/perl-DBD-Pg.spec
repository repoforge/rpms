# $Id$
# Authority: dag
# Upstream: Greg Sabino Mullane <greg$turnstep,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DBD-Pg

Summary: DBI PostgreSQL interface
Name: perl-DBD-Pg
Version: 2.15.1
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DBD-Pg/

Source: http://www.cpan.org/modules/by-module/DBD/DBD-Pg-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

# From yaml build_requires
BuildRequires: perl(DBI) >= 1.52
#BuildRequires: perl(Test::More) >= 0.61   <- kills el4 build
BuildRequires: perl(Test::More)
BuildRequires: perl(version)
# From yaml requires
BuildRequires: perl(DBI) >= 1.52
BuildRequires: perl >= 5.006001
BuildRequires: perl(version)
# From yaml recommends
BuildRequires: perl(Cwd)
BuildRequires: perl(Encode)
#BuildRequires: perl(File::Comments)             <- missing
#BuildRequires: perl(File::Comments::Plugin::C)  <- missing
BuildRequires: perl(File::Temp)
BuildRequires: perl(Module::Signature)
BuildRequires: perl(Perl::Critic)
BuildRequires: perl(Pod::Spell)
BuildRequires: perl(Test::Pod)
BuildRequires: perl(Test::Pod::Coverage)
#BuildRequires: perl(Test::Warn)		<- kills el4 build
#BuildRequires: perl(Test::YAML::Meta)		<- missing
#BuildRequires: perl(Text::SpellChecker)	<- missing
BuildRequires: perl(Time::HiRes)
BuildRequires: postgresql-devel
Requires: postgresql

%description
DBI PostgreSQL interface.

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
%doc Changes MANIFEST MANIFEST.SKIP META.yml README README.dev README.win32 SIGNATURE TODO
%doc %{_mandir}/man3/DBD::Pg.3pm*
%doc %{_mandir}/man3/Bundle::DBD::Pg.3pm*
%dir %{perl_vendorarch}/auto/DBD/
%{perl_vendorarch}/auto/DBD/Pg/
%dir %{perl_vendorarch}/Bundle/
%dir %{perl_vendorarch}/Bundle/DBD/
%{perl_vendorarch}/Bundle/DBD/Pg.pm
%dir %{perl_vendorarch}/DBD/
%{perl_vendorarch}/DBD/Pg.pm

%changelog
* Mon Sep 14 2009 Christoph Maser <cmr@financial.com> - 2.15.1-1
- Updated to version 2.15.1.

* Sat Aug 22 2009 Christoph Maser <cmr@financial.com> - 2.14.1-1
- Updated to version 2.14.1.

* Tue Jul  7 2009 Christoph Maser <cmr@financial.com> - 2.13.1-1
- Updated to version 2.13.1.

* Thu Dec 18 2008 Dag Wieers <dag@wieers.com> - 2.11.5-1
- Updated to release 2.11.5.

* Wed Oct 15 2008 Dag Wieers <dag@wieers.com> - 2.11.1-1
- Updated to release 2.11.1.

* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 2.10.7
- Updated to release 2.10.7.

* Sun Jun 22 2008 Dag Wieers <dag@wieers.com> - 2.8.1-1
- Updated to release 2.8.1.

* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 2.7.1-1
- Updated to release 2.7.1.

* Mon May 05 2008 Dag Wieers <dag@wieers.com> - 2.6.4-1
- Updated to release 2.6.4.

* Sat May 03 2008 Dag Wieers <dag@wieers.com> - 2.6.1-1
- Updated to release 2.6.1.

* Thu Mar 06 2008 Dag Wieers <dag@wieers.com> - 2.2.2-1
- Updated to release 2.2.2.

* Sun Mar 02 2008 Dag Wieers <dag@wieers.com> - 2.2.0-1
- Updated to release 2.2.0.

* Sun Feb 24 2008 Dag Wieers <dag@wieers.com> - 2.1.3-1
- Updated to release 2.1.3.

* Tue Feb 19 2008 Dag Wieers <dag@wieers.com> - 2.0.0-1
- Updated to release 2.0.0.

* Sat Aug 04 2007 Dag Wieers <dag@wieers.com> - 1.49-1
- Initial package. (using DAR)
