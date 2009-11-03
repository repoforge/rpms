# $Id$
# Authority: dag
# Upstream: Paul Prince <princep$charter,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Qmail-Control

Summary: Perl module for interfacing with Qmail's control files
Name: perl-Qmail-Control
Version: 0.01
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Qmail-Control/

Source: http://www.cpan.org/authors/id/T/TE/TECH/Qmail-Control-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Qmail-Control is a Perl module for interfacing with Qmail's control files.

This package contains the following Perl modules:

    Qmail::Control
    Qmail::Control::Lock

%prep
%setup -n Qmail/Control

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
%doc 
%doc %{_mandir}/man3/Qmail::Control.3pm*
%doc %{_mandir}/man3/Qmail::Control::Lock.3pm*
%dir %{perl_vendorlib}/Qmail/
%{perl_vendorlib}/Qmail/Control/
%{perl_vendorlib}/Qmail/Control.pm

%changelog
* Thu Oct 11 2007 Dag Wieers <dag@wieers.com> - 0.01-1
- Initial package. (using DAR)
