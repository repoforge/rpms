# $Id$

# Problem: this needs an older mod_perl (< 1.99)

# Authority: dries
# Upstream: Stas Bekman <stas$stason,org>

%define real_name libapreq
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Apache Request C Library
Name: perl-libapreq
Version: 1.33
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/libapreq/

Source: http://search.cpan.org/CPAN/authors/id/S/ST/STAS/libapreq-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, httpd-devel

%description
This package contains modules for manipulating client request data via
the Apache API with Perl and C.  Functionality includes:
 - parsing of application/x-www-form-urlencoded data
 - parsing of multipart/form-data 
 - parsing of HTTP Cookies


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
%doc README Changes
%doc %{_mandir}/man3/*
#%{perl_vendorlib}/libapreq.pm
#%{perl_vendorlib}/libapreq/*
#%exclude %{perl_archlib}/perllocal.pod
#%exclude %{perl_vendorarch}/auto/*/*/.packlist

# perl_vendorlib: /usr/lib/perl5/vendor_perl/5.8.0
# perl_vendorarch: /usr/lib/perl5/vendor_perl/5.8.0/i386-linux-thread-multi
# perl_archlib: /usr/lib/perl5/5.8.0/i386-linux-thread-multi
# perl_privlib: /usr/lib/perl5/5.8.0

%changelog
* Fri Jan  7 2005 Dries Verachtert <dries@ulyssis.org> - 1.33-1
- Initial package.

