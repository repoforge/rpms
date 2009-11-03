# $Id$
# Authority: dag
# Upstream: Eric Rybski (rybskej$yahoo,com)

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name forks

Summary: forks - emulate threads with fork
Name: perl-forks
Version: 0.33
Release: 2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/forks/

Source: http://www.cpan.org/authors/id/R/RY/RYBSKEJ/forks-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
### FIXME: Find out why this provides it missing ?
Provides: perl(forks::Devel::Symdump) = %{version}

%description
forks - emulate threads with fork.

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
%doc CHANGELOG CREDITS MANIFEST MANIFEST.skip META.yml README SIGNATURE TODO VERSION
%doc %{_mandir}/man3/forks.3pm*
%doc %{_mandir}/man3/forks::*.3pm*
%doc %{_mandir}/man3/threads::shared::*.3pm*
%{perl_vendorarch}/auto/forks/
%{perl_vendorarch}/forks/
%{perl_vendorarch}/forks.pm
%{perl_vendorarch}/threads/

%changelog
* Wed May 06 2009 Dag Wieers <dag@wieers.com> - 0.33-2
- Added missing perl(forks::Devel::Symdump) provide.

* Wed May 06 2009 Dag Wieers <dag@wieers.com> - 0.33-1
- Updated to release 0.33.

* Mon May 04 2009 Dag Wieers <dag@wieers.com> - 0.32-1
- Initial package. (using DAR)
