# $Id$
# Authority: dag
# Upstream: Faycal CHRAIBI <fays$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Digest-Crc32

Summary: Cyclic Redundency Check digests implementation 
Name: perl-Digest-Crc32
Version: 0.01
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Digest-Crc32/

Source: http://www.cpan.org/modules/by-module/Digest/Digest-Crc32-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Digest-Crc32 is a Cyclic Redundency Check digests implementation.

%prep
%setup -n %{real_name}-001

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc MANIFEST META.yml README
%doc %{_mandir}/man3/Digest::Crc32.3pm*
%dir %{perl_vendorlib}/Digest/
#%{perl_vendorlib}/Digest/Crc32/
%{perl_vendorlib}/Digest/Crc32.pm

%changelog
* Wed Feb 16 2011 Dag Wieers <dag@wieers.com> - 0.01-1
- Initial package. (using DAR)
