# $Id$
# Authority: dries
# Upstream: David Huggins-Daines <dhd$pobox,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Audio-OSS

Summary: Interface to OSS (open sound system) audio devices
Name: perl-Audio-OSS
Version: 0.0501
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Audio-OSS/

Source: http://search.cpan.org/CPAN/authors/id/D/DJ/DJHD/Audio-OSS-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker), perl

%description
This module provides a pure-Perl, no-nonsense, filehandle-based
interface to the Open Sound System.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Audio/OSS.pm
%{perl_vendorlib}/Audio/OSS

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.0501-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.0501-1
- Initial package.
