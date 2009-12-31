# $Id$
# Authority: dag
# Upstream: Adam Kennedy <adamk@cpan.org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define rname Crypt-DSA

Summary: Crypt-DSA module for perl
Name: perl-Crypt-DSA
Version: 1.16
Release: 1%{?dist}
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Crypt-DSA/

Source: http://search.cpan.org/CPAN/authors/id/A/AD/ADAMK/Crypt-DSA-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Data::Buffer) >= 0.01
BuildRequires: perl(Digest::SHA1)
#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Spec)
BuildRequires: perl(File::Which) >= 0.05
BuildRequires: perl(IPC::Open3)
BuildRequires: perl(MIME::Base64)
BuildRequires: perl(Math::BigInt) >= 1.78
BuildRequires: perl(Test::More) >= 0.42
BuildRequires: perl >= 5.005
Requires: perl(Data::Buffer) >= 0.01
Requires: perl(Digest::SHA1)
Requires: perl(File::Spec)
Requires: perl(File::Which) >= 0.05
Requires: perl(IPC::Open3)
Requires: perl(MIME::Base64)
Requires: perl(Math::BigInt) >= 1.78
Requires: perl >= 5.005

%filter_from_requires /^perl*/d
%filter_setup

%description
Crypt-DSA module for perl

%prep
%setup -n %{rname}-%{version}

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
%doc MANIFEST README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/Crypt/
%{perl_vendorlib}/Crypt/DSA.pm
%{perl_vendorlib}/Crypt/DSA/

%changelog
* Thu Dec 31 2009 Christoph Maser <cmr@financial.com> - 1.16-1
- Updated to version 1.16.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.14-1
- Updated to release 0.14.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.13-1.2
- Rebuild for Fedora Core 5.

* Thu Jan 12 2006 Dag Wieers <dag@wieers.com> - 0.13-1
- Initial package. (using DAR)
