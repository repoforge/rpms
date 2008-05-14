# $Id$
# Authority: matthias
# Upstream: Marc Lehmann <pcg$goof,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name IO-AIO

Summary: Asynchronous Input/Output
Name: perl-IO-AIO
Version: 3.02
Release: 1
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/IO-AIO/

Source: http://www.cpan.org/modules/by-module/IO/IO-AIO-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

### Provided by either perl or perl-devel
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module implements asynchronous I/O using whatever means your operating
system supports.

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
%doc COPYING Changes MANIFEST META.yml README
%doc %{_mandir}/man3/IO::AIO.3pm*
%dir %{perl_vendorarch}/auto/IO/
%{perl_vendorarch}/auto/IO/AIO/
%dir %{perl_vendorarch}/IO/
%{perl_vendorarch}/IO/AIO.pm

%changelog
* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 3.02-1
- Updated to release 3.02.

* Sat May 03 2008 Dag Wieers <dag@wieers.com> - 2.62-1
- Updated to release 2.62.

* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 2.51-1
- Updated to release 2.51.

* Thu May 31 2007 Matthias Saou <http://freshrpms.net/> 2.33-1
- Update to 2.33.
- Build require perl(ExtUtils::MakeMaker) for F7.

* Wed Apr 19 2006 Matthias Saou <http://freshrpms.net/> 1.73-1
- Initial RPM release.
- Not sure if the autoconf.pm should be included or not...
