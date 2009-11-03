# $Id$
# Authority: dag
# Upstream: Kurt Stephens <ks,perl$kurtstephens,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name UMMF
%define real_version 1.003

Summary: Perl module that implements a UML Meta-Model Framework
Name: perl-UMMF
Version: 1.02
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/UMMF/

Source: http://www.cpan.org/authors/id/K/KS/KSTEPHENS/UMMF-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-UMMF is a Perl module that implements a UML Meta-Model Framework.

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

### Clean up docs
find doc/ example/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYRIGHT.txt Changes LICENSE.txt MANIFEST README.txt doc/ example/
%doc %{_mandir}/man1/files2dirs.1*
%doc %{_mandir}/man1/files2dirs.pl.1*
%doc %{_mandir}/man1/ummf.1*
%doc %{_mandir}/man1/ummf.pl.1*
%doc %{_mandir}/man3/UMMF.3pm*
%doc %{_mandir}/man3/UMMF::*.3pm*
%{_bindir}/argo2xmi
%{_bindir}/argo2xmi.pl
%{_bindir}/files2dirs
%{_bindir}/files2dirs.pl
%{_bindir}/uml2xmi
%{_bindir}/uml2xmi.pl
%{_bindir}/ummf
%{_bindir}/ummf.pl
%{perl_vendorlib}/use_alias.pm
%{perl_vendorlib}/UMMF/
%{perl_vendorlib}/UMMF.pm

%changelog
* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 1.02-1
- Initial package. (using DAR)
