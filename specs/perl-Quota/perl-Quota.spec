# $Id$

# Authority: dries
# Upstream: Tom Zoerner <Tom,Zoerner$informatik,uni-erlangen,de>

%define real_name Quota
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Perl interface to file system quotas
Name: perl-Quota
Version: 1.5.0
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Quota/

Source: http://www.cpan.org/modules/by-module/Quota/Quota-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, quota

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
%{__perl} Makefile.PL INSTALLDIRS="vendor" destdir=%{buildroot}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README CHANGES
%doc %{_mandir}/man3/*
%{perl_vendorarch}/Quota.pm
%{perl_vendorarch}/auto/Quota
%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/.packlist

%changelog
* Wed Dec 08 2004 Dries Verachtert <dries@ulyssis.org> - 1.5.0
- Initial package.
