# $Id$
# Authority: shuff
# Upstream: Damien Stuart <dstuart$dstuart,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Authen-Krb5-Simple

Summary: Basic user authentication using Kerberos 5
Name: perl-%{real_name}
Version: 0.42
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Authen-Krb5-Simple/

Source: http://search.cpan.org/CPAN/authors/id/D/DS/DSTUART/Authen-Krb5-Simple-0.42.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
#BuildArch: noarch

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More)
BuildRequires: rpm-macros-rpmforge
Requires: perl


### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
The Authen::Krb5::Simple module provides a means to authenticate a
user/password using Kerberos 5 protocol. The module's authenticate function
takes a username (or user@kerberos_realm) and a password, and authenticates
that user using the local Kerberos 5 installation. It was initially created to
allow perl scripts to perform authentication against a Microsoft Active
Directory (AD) server configured to accept Kerberos client requests.

It is important to note: This module only performs simple authentication. It
does not get, grant, use, or retain any kerberos tickets. It will check user
credentials against the Kerberos server (as configured on the local system)
each time the authenticate method is called.

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
%doc %{_mandir}/man3/*
%dir %{perl_vendorarch}/Authen/Krb5/
%{perl_vendorarch}/Authen/Krb5/*
%{perl_vendorarch}/auto/Authen/Krb5/*

%changelog
* Fri Nov 13 2009 Steve Huff <shuff@vecna.org> - 0.42-1
- Initial package.
