# $Id$
# Authority: dag
# Upstream: Shevek <cpan$anarres,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Mail-SRS

Summary: Interface to Sender Rewriting Scheme
Name: perl-Mail-SRS
Version: 0.31
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Mail-SRS/

Source: http://www.cpan.org/modules/by-module/Mail/Mail-SRS-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Interface to Sender Rewriting Scheme.

%prep
%setup -n %{real_name}-%{version}

%build
echo | %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find eg/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc MANIFEST MANIFEST.SKIP README README.pobox TODO eg/
%doc %{_mandir}/man1/srs.1*
%doc %{_mandir}/man1/srsc.1*
%doc %{_mandir}/man1/srsd.1*
%doc %{_mandir}/man3/Mail::SRS.3pm*
%doc %{_mandir}/man3/Mail::SRS::*.3pm*
%{_bindir}/srs
%{_bindir}/srsc
%{_bindir}/srsd
%dir %{perl_vendorlib}/Mail/
%{perl_vendorlib}/Mail/SRS/
%{perl_vendorlib}/Mail/SRS.pm

%changelog
* Thu Dec 06 2007 Dag Wieers <dag@wieers.com> - 0.31-1
- Initial package. (using DAR)
