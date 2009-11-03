# $Id$
# Authority: dag
# Upstream: NOKUBI Takatsugu <knok$daionet,gr,jp>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name File-MMagic

Summary: Perl module to guess file type
Name: perl-File-MMagic
Version: 1.27
Release: 1%{?dist}
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/File-MMagic/

Source: http://www.cpan.org/modules/by-module/File/File-MMagic-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
File-MMagic is a Perl module to guess file type.

This package contains the following Perl module:

    File::MMagic

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
find contrib/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING ChangeLog MANIFEST META.yml README.en README.ja contrib/
%doc %{_mandir}/man3/File::MMagic.3pm*
%dir %{perl_vendorlib}/File/
%{perl_vendorlib}/File/MMagic.pm

%changelog
* Tue May 01 2007 Dag Wieers <dag@wieers.com> - 1.27-1
- Initial package. (using DAR)
