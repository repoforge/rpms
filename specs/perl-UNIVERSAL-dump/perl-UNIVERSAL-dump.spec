# $Id$
# Authority: dag
# Upstream: Elizabeth Mattijsen <liz$dijkmat,nl>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name UNIVERSAL-dump

Summary: Perl module to add dump methods to all classes and objects
Name: perl-UNIVERSAL-dump
Version: 0.04
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/UNIVERSAL-dump/

Source: http://www.cpan.org/modules/by-module/UNIVERSAL/UNIVERSAL-dump-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-UNIVERSAL-dump is a Perl module to add dump methods
to all classes and objects.

This package contains the following Perl module:

    UNIVERSAL::dump

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
%doc CHANGELOG MANIFEST META.yml README TODO VERSION
%doc %{_mandir}/man3/UNIVERSAL::dump.3pm*
%dir %{perl_vendorlib}/UNIVERSAL/
#%{perl_vendorlib}/UNIVERSAL/dump/
%{perl_vendorlib}/UNIVERSAL/dump.pm

%changelog
* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.04-1
- Initial package. (using DAR)
