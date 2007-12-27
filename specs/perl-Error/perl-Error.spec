# $Id$
# Authority: dag
# Upstream: Shlomi Fish <shlomif$iglu,org,il>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Error

Summary: Error/exception handling in an OO-ish way
Name: perl-Error
Version: 0.17011
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Error/

Source: http://www.cpan.org/modules/by-module/Error/Error-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 2:5.8.0
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl >= 2:5.8.0

%description
The Error package provides two interfaces. Firstly Error provides a procedural
interface to exception handling. Secondly Error is a base class for
errors/exceptions that can either be thrown, for subsequent catch, or can
simply be recorded.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog MANIFEST META.yml README examples/
%doc %{_mandir}/man3/Error.3pm*
%doc %{_mandir}/man3/Error::Simple.3pm*
%{perl_vendorlib}/Error/
%{perl_vendorlib}/Error.pm

%changelog
* Thu Dec 27 2007 Dag Wieers <dag@wieers.com> - 0.17011-1
- Updated to release 0.17011.

* Sat Nov 24 2007 Dag Wieers <dag@wieers.com> - 0.17010-1
- Updated to release 0.17010.

* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 0.17009-1
- Updated to release 0.17009.

* Tue Aug 07 2007 Dag Wieers <dag@wieers.com> - 0.17008-2
- Disabled auto-requires for examples/.

* Mon Apr 16 2007 Dries Verachtert <dries@ulyssis.org> - 0.17008-1
- Updated to release 0.17008.

* Fri Mar 19 2004 Matthias Saou <http://freshrpms.net/> 0.15-1
- Initial RPM release.
