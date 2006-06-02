# $Id$

# Authority: dries
# Upstream: Jarkko Hietaniemi <jhi@iki,fi>

%define real_name BSD-Resource
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: BSD process resource limit and priority functions
Name: perl-BSD-Resource
Version: 1.28
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/BSD-Resource/

Source: http://www.cpan.org/modules/by-module/BSD/BSD-Resource-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

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
%{__perl} Makefile.PL \
	INSTALLDIRS="vendor" \
	PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
                %{buildroot}%{perl_vendorarch}/auto/*{,/*{,/*}}/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog README
%doc %{_mandir}/man3/*
%{perl_vendorarch}/BSD/Resource.pm
%{perl_vendorarch}/auto/BSD/Resource/*

%changelog
* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 1.28-1
- Updated to release 1.28.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.24-1.2
- Rebuild for Fedora Core 5.

* Sun Dec 19 2004 Dries Verachtert <dries@ulyssis.org> - 1.24-1
- Initial package.
