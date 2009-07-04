# $Id$
# Authority: dag
# Upstream: Maurice Aubrey <maurice$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name IPC-ShareLite

Summary: Simple shared memory interface module for perl
Name: perl-IPC-ShareLite
Version: 0.17
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/IPC-ShareLite/

Source: http://www.cpan.org/modules/by-module/IPC/IPC-ShareLite-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 2:5.8.0
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl >= 2:5.8.0

%description
IPC::ShareLite provides a simple interface to shared memory, allowing data to
be efficiently communicated between processes.  Your operating system must
support SysV IPC (shared memory and semaphores) in order to use this module.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}" << 'EOF'



y




EOF
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
%doc Changes MANIFEST META.yml README SIGNATURE
%doc %{_mandir}/man3/IPC::ShareLite.3pm*
%dir %{perl_vendorarch}/auto/IPC/
%{perl_vendorarch}/auto/IPC/ShareLite/
%dir %{perl_vendorarch}/IPC/
%{perl_vendorarch}/IPC/ShareLite.pm

%changelog
* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 0.17-1
- Updated to version 0.17.

* Fri Mar 14 2008 Dag Wieers <dag@wieers.com> - 0.13-1
- Updated to release 0.13.

* Thu Feb 28 2008 Dag Wieers <dag@wieers.com> - 0.12-1
- Updated to release 0.12.

* Mon Feb 25 2008 Dag Wieers <dag@wieers.com> - 0.10-1
- Updated to release 0.10.

* Wed May 26 2004 Matthias Saou <http://freshrpms.net/> 0.09-2
- Rebuild for Fedora Core 2.

* Fri Mar 19 2004 Matthias Saou <http://freshrpms.net/> 0.09-1
- Initial RPM release.
