# $Id$
# Authority: dries
# Upstream: Tom Zoerner <Tom,Zoerner$informatik,uni-erlangen,de>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Quota
%define real_version 1.006000

Summary: Perl interface to file system quotas
Name: perl-Quota
Version: 1.6.0
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Quota/

Source: http://www.cpan.org/modules/by-module/Quota/Quota-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: quota

%description
The Quota module provides access to file system quotas.  The
quotactl system call or ioctl is used to query or set quotas
on the local host, or queries are submitted via RPC to a
remote host.  Mount tables can be parsed with getmntent and
paths can be translated to device files (or whatever the
actual quotactl implementations needs as argument) of the
according file system.

%prep
%setup -n %{real_name}-%{version}

%build
export CFLAGS="-fPIC"
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find contrib/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES INSTALL MANIFEST README contrib/
%doc %{_mandir}/man3/Quota.3pm*
%{perl_vendorarch}/auto/Quota/
%{perl_vendorarch}/Quota.pm

%changelog
* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 1.6.0-1
- Updated to release 1.6.0.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.5.1-1
- Updated to release 1.5.1.

* Wed Dec 08 2004 Dries Verachtert <dries@ulyssis.org> - 1.5.0
- Initial package.
