# $Id$
# Authority: dag
# Upstream: Olivier Thauvin <nanardon$nanardon,zarb,org>

# rpm on el4 is too odl
# EcludeDist: el4

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name RPM4

Summary: Perl module to access and manipulate RPM files
Name: perl-RPM4
Version: 0.23
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/RPM4/

Source: http://www.cpan.org/authors/id/N/NA/NANARDON/RPM4/RPM4-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
Perl module to access and manipulate RPM files.

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

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog MANIFEST META.yml README examples/
%doc %{_mandir}/man1/hrpmreb.1*
%doc %{_mandir}/man1/rpmresign.1*
%doc %{_mandir}/man3/RPM4.3pm*
%doc %{_mandir}/man3/RPM4::*.3pm*
%{_bindir}/hrpmreb
%{_bindir}/rpm_produced
%{_bindir}/rpmresign
%{perl_vendorarch}/auto/RPM4/
%{perl_vendorarch}/RPM4/
%{perl_vendorarch}/RPM4.pm

%changelog
* Fri Nov 23 2007 Dag Wieers <dag@wieers.com> - 0.23-1
- Initial package. (using DAR)
