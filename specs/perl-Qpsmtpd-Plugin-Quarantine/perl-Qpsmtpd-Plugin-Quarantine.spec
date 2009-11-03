# $Id$
# Authority: dag
# Upstream: David Muir Sharnoff <muir$idiom,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Qpsmtpd-Plugin-Quarantine

Summary: Perl module to filter outbound email to prevent blacklisting
Name: perl-Qpsmtpd-Plugin-Quarantine
Version: 1.02
Release: 1%{?dist}
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Qpsmtpd-Plugin-Quarantine/

Source: http://www.cpan.org/authors/id/M/MU/MUIR/modules/Qpsmtpd-Plugin-Quarantine-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Qpsmtpd-Plugin-Quarantine is a Perl module to filter outbound email
to prevent blacklisting.

This package contains the following Perl module:

    Qpsmtpd::Plugin::Quarantine

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
%doc CHANGELOG COPYING MANIFEST META.yml README
%doc %{_mandir}/man3/Qpsmtpd::Plugin::Quarantine.3pm*
%dir %{perl_vendorlib}/Qpsmtpd/
%dir %{perl_vendorlib}/Qpsmtpd/Plugin/
%{perl_vendorlib}/Qpsmtpd/Plugin/Quarantine/
%{perl_vendorlib}/Qpsmtpd/Plugin/Quarantine.pm
%{perl_vendorlib}/Qpsmtpd/Plugin/Quarantine.pod

%changelog
* Thu Oct 11 2007 Dag Wieers <dag@wieers.com> - 1.02-1
- Initial package. (using DAR)
