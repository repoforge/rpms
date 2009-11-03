# $Id$
# Authority: dries
# Upstream: Alexey Tourbin <at$altlinux,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name RPM-Payload

Summary: Perl module for in-memory access to an RPM cpio archive
Name: perl-RPM-Payload
Version: 0.10
Release: 1%{?dist}
License: GPLv2+
Group: Applications/CPAN
URL: http://search.cpan.org/dist/RPM-Payload/

Source: http://search.cpan.org/CPAN/authors/id/A/AT/ATOURBIN/RPM-Payload-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl

%description
The Perl module RPM::Payload provides in-memory access to an RPM cpio archive.

%prep
%setup -n %{real_name}-%{version}

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
%doc MANIFEST META.yml
%doc %{_mandir}/man3/RPM::Payload.3pm*
%{perl_vendorlib}/RPM/Payload.pm

%changelog
* Sun Apr 19 2009 Dries Verachtert <dries@ulyssis.org> - 0.10-1
- New package.
