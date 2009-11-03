# $Id$
# Authority: dag
# Upstream: Rob Brown <bbb$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name File-NFSLock

Summary: Perl module to do NFS (or not) locking
Name: perl-File-NFSLock
Version: 1.20
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/File-NFSLock/

Source: http://www.cpan.org/modules/by-module/File/File-NFSLock-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl

%description
File-NFSLock is a Perl module to do NFS (or not) locking.

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
%doc Changes MANIFEST README
%doc %{_mandir}/man3/File::NFSLock.3pm*
%dir %{perl_vendorlib}/File/
%{perl_vendorlib}/File/NFSLock.pm

%changelog
* Tue May 01 2007 Dag Wieers <dag@wieers.com> - 1.20-1
- Initial package. (using DAR)
