# $Id$

# Authority: dries
# Upstream: Jochen Wiedmann <jwied$cpan,org>


%define real_name PlRPC
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Perl extension for writing PlRPC servers and clients
Name: perl-PlRPC
Version: 0.2018
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/PlRPC/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/J/JW/JWIED/PlRPC-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
PlRPC (Perl RPC) is a package for implementing servers and clients that
are written in Perl entirely. The name is borrowed from Sun's RPC
(Remote Procedure Call), but it could as well be RMI like Java's "Remote
Method Interface), because PlRPC gives you the complete power of Perl's
OO framework in a very simple manner.
    
%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README ChangeLog
%{_mandir}/man3/*
%{perl_vendorlib}/Bundle/PlRPC.pm
%{perl_vendorlib}/RPC

%changelog
* Wed Dec 29 2004 Dries Verachtert <dries@ulyssis.org> - 0.2018-1
- Updated to release 0.2018.

* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 0.2017-1
- Initial package.
